# Stick Box contributor context

This is the standalone Stick Box repository, extracted from Project Aero.
`index.html`, `watch.html`, `library.js`, `player.js` and `style.css` live at root.
There is no dependency on a parent Aero checkout. Keep website paths relative so
GitHub Pages repository subpaths work. Back to Aero links use its absolute URL.

## Archive and scope

`catalog.json` records 269 unique unchanged SWFs, their metadata/hashes and
collection ordering: 19 Fights collections plus only Animator vs. Animation
1, 2, and 3 under Humor. Do not expand Humor without the user's request.
Groups with `category: "humor"` render under Humor; missing category means Fights.
Reuse originals shared by collections; include the collection ID in watch links.
Retain unavailable listings and their errors, and keep source HTML snapshots
as unexecuted `.html.txt` files. Render metadata as text, never source HTML.

## Player

The local `ruffle/` bundle is pinned to 0.6.0 with both upstream licenses.
Preserve `backgroundColor: null`: movies control their own stage colors and can
change them during playback. `stageBackground` is audit metadata only.
Keep `allowNetworking: 'none'`, `allowScriptAccess: false`, `openUrlMode: 'deny'`.
Use Ruffle V1 `resume`, `suspend`, `suspended` and master `volume`. Preserve the
generation guard and destroy the previous runtime on restart. Pause on page hide.
`stickbox.volume` remains independent of Aero preferences. The homepage must not
load Ruffle or SWFs. Confirmed external-video launchers show an explanation/link
without starting the obsolete Flash wrapper. Keep original file bytes intact.

## Tools and publication

Run tools from this root: `python -B tools/verify_archive.py`,
`python -B tools/test_swf_metadata.py`. Importers resolve paths relative to their
own location. `expand_fights.py` preserves unrelated catalog groups. Run
`audit_dependencies.py --write` after future archive expansions.

The full archive exceeds GitHub Pages' published-size limit. `tools/build_site.py`
requires an actual public HTTPS R2 base address and builds only the lightweight
`dist/` site, rewriting generated media URLs. Source catalog paths remain local
for preservation checks. Publish only dist using `.github/workflows/pages.yml`;
never upload the complete archive as the Pages artifact. No credentials in Git.
Refer to README for R2 object-key layout and CORS setup. Do not guess the final
Stick Box domain, move media to Aero, rewrite history, or publish without scope.
