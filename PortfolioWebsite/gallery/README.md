# Gallery photos

The photos shown in the Gallery section of the portfolio site. This folder is
generated, so don't edit it by hand.

## Adding or removing photos

1. Put the full-size photos in `../gallery-originals/` (that folder stays on
   my computer and is not uploaded). Delete a photo from there to remove it.
2. Run `python3 build_gallery.py` in the `PortfolioWebsite` folder.
3. Commit and push.

The script makes a web-sized copy of each photo here, a small thumbnail in
`thumbs/`, and `photos.json`, the list the page reads. Camera metadata,
including location, is left out of the copies.

## How it lays out

Photos appear in file-name order, so prefix names with `01-`, `02-` and so on
to choose the order. The page arranges them in rows that each fill the full
width, whatever mix of tall and wide photos there is, so there are no gaps.
The file name is also the photo's description for screen readers.
