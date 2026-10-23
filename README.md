# Stick Box

A standalone Stickpage tribute, originally a side door from Project Aero.
This folder is the **root of the new repository**: `index.html` is the homepage.
No Aero checkout, package installation, or external player CDN is required.
Do not nest these files inside another `stick-box/` directory.

## What is preserved

- 266 original SWFs across the 19 Stick Fights collections.
- Only Animator vs. Animation 1, 2, and 3 under Stick Humor.
- 269 unique original files / 1,706,610,417 bytes, unchanged, with SHA-256 hashes.
- Available thumbnails, creator credits, descriptions, source snapshots and tools.
- Four unavailable source listings and two preserved external-video launchers,
  honestly labeled. Stick Games remains empty.

The shared player has play/pause, volume/mute, restart, fullscreen and collection
navigation. Authored movie colors and original menus are preserved. Networking,
script access and outgoing links from the SWFs remain disabled.
See [archive provenance](archive/README.md) and [runtime credits](THIRD_PARTY.md).

## Preview everything locally

From this folder:

```sh
python -m http.server 8776 --bind 127.0.0.1
```

Open <http://127.0.0.1:8776/>. Root `catalog.json` uses the local archive, so all
saved originals work from the local archive. Only the movie selected by the visitor loads.
The two external-video launchers still depend on their external videos.
The local player bundle lives in `ruffle/`, including its licenses.

## Repository

The live site is <https://matticushtml.github.io/Stickbox/> and its source is
<https://github.com/MatticusHTML/Stickbox>. Keep all subfolders when cloning,
copying or uploading this project; the loose homepage files are not the archive.

The repository includes the full preservation archive. Every current SWF is
smaller than GitHub's 100 MB per-file limit. Old Aero commits still contain
historical copies; moving working files does not rewrite that history.

## Publish entirely through GitHub

All 269 original SWFs, thumbnails and the Ruffle runtime belong in this
repository, including their subfolders. Uploading only the loose root files
omits the movies and player. Do not use Git LFS for these originals: the current
files fit GitHub's per-file limit and the player needs the actual bytes.

The repository contains about 1.71 GB of movies. GitHub Pages has a separate
[1 GB published-site limit](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits).
The included Actions workflow publishes only the approximately 35 MB `dist/`
website and loads movies from `raw.githubusercontent.com` in this same repository.
No Cloudflare account, R2 bucket, access key or repository media variable is needed.

Under **Settings → Pages**, use **GitHub Actions**. The workflow runs on pushes
to `main` or manually from Actions. It pins each generated movie URL to that
build's commit SHA, while the source catalog keeps local paths for preservation
and offline HTTP previews. Thumbnails and Ruffle stay in the Pages artifact;
SWFs and original source snapshots do not. Never publish the full root as Pages.

To reproduce a build locally against the current GitHub branch:

```sh
python -B tools/build_site.py --media-base-url https://raw.githubusercontent.com/MatticusHTML/Stickbox/main
python -m http.server 8777 --bind 127.0.0.1 --directory dist
```

The builder changes only the generated catalog's movie URLs. Source originals
and their hashes remain untouched. The generated `dist/` is ignored by Git.
A published build must wait until its archive commit has finished uploading.

## Connect back to Aero

Stick Box's Back to Aero links point to <https://matticushtml.github.io/Aero/>.
Aero's `STICKBOX_URL` points back to this independent site. Aero keeps its waving
greeting and corner character; the corner character hides when wipeout! is
selected. The two websites have separate current files and repositories.

## Verify or maintain the archive

```sh
python -B tools/verify_archive.py
python -B tools/test_swf_metadata.py
```

Import tools retain their standard-library-only workflow and now run from this
repository root. `tools/import_animator.py` is restricted to the approved trilogy.
See [CLAUDE.md](CLAUDE.md) before changing preservation/player behavior.
