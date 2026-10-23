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
saved originals work without R2. Only the movie selected by the visitor loads.
The two external-video launchers still depend on their external videos.
The local player bundle lives in `ruffle/`, including its licenses.

## Start the new GitHub repository

Create an empty GitHub repository, then add the **contents of this folder**.
Include hidden files: `.github/`, `.gitignore`, `.gitattributes`, `.nojekyll`.
This folder intentionally has no `.git` directory, remote or copied Aero history.
You can use GitHub Desktop's **Add local repository / Create a repository here**
or initialize Git here and add your new remote. No repository has been created
or pushed on your behalf.

The source repository includes the full preservation archive. Every current SWF
is smaller than GitHub's 100 MB per-file limit. Old Aero commits still contain
historical copies; moving working files does not rewrite that history.

## Publish the small website with R2 media

The complete local archive is about 1.71 GB, exceeding
[GitHub Pages' 1 GB published-site limit](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits).
The included workflow publishes **only `dist/`**, about 35 MB with the bundled
player and thumbnails. It does not publish SWFs or archival HTML snapshots there.

1. Upload the saved `.swf` files to a public R2 bucket, preserving keys such as
   `archive/shock/shock1.swf` and `archive/animator-vs-animation/animatorvsanimation.swf`.
   Keep the complete local archive and its hashes. The bucket base URL must resolve
   each catalog path appended to it. A custom media domain is suitable for production.
2. Set the bucket's [CORS policy](https://developers.cloudflare.com/r2/buckets/cors/)
   to allow `GET` and `HEAD` from your GitHub Pages **origin** (for example
   `https://matticushtml.github.io`, with no repository path), allow `Range`, and
   expose `Content-Length`, `Content-Range`, `Accept-Ranges`, and `ETag`.
3. In the new repository, create an Actions **repository variable** named
   `STICKBOX_MEDIA_BASE_URL` containing that public HTTPS media base URL. This is
   a public address, not an S3 API endpoint or credential. Keep credentials out of Git.
4. Under **Settings → Pages**, choose **GitHub Actions**. The included workflow
   runs on pushes to `main`, or manually from Actions. If you choose another
   default branch, update `.github/workflows/pages.yml` to match.

Build locally with the actual media address before publishing:

```sh
python -B tools/build_site.py --media-base-url https://YOUR-PUBLIC-MEDIA-DOMAIN
python -m http.server 8777 --bind 127.0.0.1 --directory dist
```

The builder changes **only the generated catalog's movie URLs**. It never changes
the source catalog or originals. The generated `dist/` is ignored by Git and can
be rebuilt. A missing media address stops the build instead of publishing broken
local movie links. Upload the originals and verify a real R2 movie before deploying;
no R2 uploads or public deployment have been performed during preparation.

## Connect back to Aero

Stick Box's Back to Aero links already point to <https://matticushtml.github.io/Aero/>.
When this site's final URL exists, set `STICKBOX_URL` in Aero's `index.html` to it.
Aero's stickman stays in the background, hides on wipeout!, and shows a coming-soon
invitation until that URL is configured. It has no dependency on this folder.

## Verify or maintain the archive

```sh
python -B tools/verify_archive.py
python -B tools/test_swf_metadata.py
```

Import tools retain their standard-library-only workflow and now run from this
repository root. `tools/import_animator.py` is restricted to the approved trilogy.
See [CLAUDE.md](CLAUDE.md) before changing preservation/player behavior.
