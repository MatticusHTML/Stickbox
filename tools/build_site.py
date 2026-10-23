"""Build a small static publish directory while retaining local originals."""
import argparse
import copy
import json
import os
from pathlib import Path, PurePosixPath
import shutil
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--media-base-url', default=os.environ.get('STICKBOX_MEDIA_BASE_URL', ''))
    args = parser.parse_args()
    base = args.media_base_url.rstrip('/')
    url = urlsplit(base)
    if url.scheme != 'https' or not url.hostname or url.username or url.password or url.query or url.fragment:
        parser.error('Set STICKBOX_MEDIA_BASE_URL or --media-base-url to your public HTTPS media base URL.')
    catalog = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
    published = copy.deepcopy(catalog)
    thumbnails = set()
    for group in published['series']:
        for episode in group['episodes']:
            path = PurePosixPath(episode['file'])
            if path.is_absolute() or '..' in path.parts or path.parts[0] != 'archive' or path.suffix != '.swf':
                raise ValueError('Unexpected original file path: ' + str(path))
            episode['file'] = base + '/' + quote(str(path), safe='/')
            if episode.get('thumbnail'):
                thumb = PurePosixPath(episode['thumbnail'])
                if thumb.is_absolute() or '..' in thumb.parts or thumb.parts[0] != 'archive' or thumb.suffix != '.jpg':
                    raise ValueError('Unexpected thumbnail path')
                thumbnails.add(str(thumb))
    # Only this fixed, generated directory can be replaced; never follow a link outside the project.
    output = (ROOT / 'dist').resolve()
    if output.parent != ROOT.resolve() or output.name != 'dist' or (ROOT / 'dist').is_symlink():
        raise ValueError('Unsafe build output path')
    if output.exists():
        shutil.rmtree(output)
    output.mkdir()
    for name in ('index.html', 'watch.html', 'library.js', 'player.js', 'style.css', 'mark.svg', '.nojekyll'):
        shutil.copy2(ROOT / name, output / name)
    shutil.copytree(ROOT / 'ruffle', output / 'ruffle')
    for name in sorted(thumbnails):
        target = output / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / name, target)
    (output / 'catalog.json').write_text(json.dumps(published, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    total = sum(path.stat().st_size for path in output.rglob('*') if path.is_file())
    print(f'Publish directory: {output}; {total:,} bytes. Originals remain unchanged outside dist/.')


if __name__ == '__main__':
    main()
