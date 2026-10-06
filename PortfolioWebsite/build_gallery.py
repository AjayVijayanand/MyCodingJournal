"""Build the website gallery from my full-size photos.

Put original photos in gallery-originals/ (which is not uploaded), then run:

    python3 build_gallery.py

For every original this writes a web-sized copy to gallery/, a small thumbnail
to gallery/thumbs/ and an entry in gallery/photos.json, which the page reads.
Copies of photos that are no longer in gallery-originals/ are removed.
Camera metadata, including location, is not carried over.

Needs Pillow:  pip install Pillow
"""

import argparse
import json
import os
import time

from PIL import Image, ImageOps

FULL_SIZE = 2000   # longest side of the copy opened when a photo is clicked
THUMB_SIZE = 640   # longest side of the copy shown in the grid
EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")


def save(image, path, size, quality, icc):
    copy = image.copy()
    copy.thumbnail((size, size), Image.LANCZOS)
    extra = {"icc_profile": icc} if icc else {}
    copy.save(path, "JPEG", quality=quality, optimize=True, progressive=True, **extra)
    return copy.size


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=os.path.dirname(os.path.abspath(__file__)))
    parser.add_argument("--seconds", type=float, default=0, help="stop after this long and finish on the next run")
    args = parser.parse_args()

    source = os.path.join(args.root, "gallery-originals")
    out = os.path.join(args.root, "gallery")
    thumbs = os.path.join(out, "thumbs")
    os.makedirs(thumbs, exist_ok=True)

    originals = sorted(f for f in os.listdir(source) if f.lower().endswith(EXTENSIONS))
    wanted = {os.path.splitext(f)[0] + ".jpg" for f in originals}

    # Remove copies whose original has gone
    for folder in (out, thumbs):
        for f in os.listdir(folder):
            if f.lower().endswith(".jpg") and f not in wanted:
                os.remove(os.path.join(folder, f))

    started = time.time()
    made = 0
    unfinished = 0
    for f in originals:
        name = os.path.splitext(f)[0] + ".jpg"
        full_path = os.path.join(out, name)
        thumb_path = os.path.join(thumbs, name)
        original = os.path.join(source, f)
        fresh = all(os.path.exists(p) and os.path.getmtime(p) >= os.path.getmtime(original) for p in (full_path, thumb_path))
        if fresh:
            continue
        if args.seconds and time.time() - started > args.seconds:
            unfinished += 1
            continue
        image = Image.open(original)
        icc = image.info.get("icc_profile")
        image.draft("RGB", (FULL_SIZE * 2, FULL_SIZE * 2))  # much faster for large JPEGs
        image = ImageOps.exif_transpose(image).convert("RGB")
        save(image, full_path, FULL_SIZE, 84, icc)
        save(image, thumb_path, THUMB_SIZE, 78, icc)
        made += 1

    photos = []
    for name in sorted(wanted):
        path = os.path.join(out, name)
        if os.path.exists(path):
            with Image.open(path) as image:
                photos.append({"file": name, "width": image.width, "height": image.height})
    with open(os.path.join(out, "photos.json"), "w") as handle:
        json.dump(photos, handle, indent=1)

    print(f"{made} photos processed, {len(photos)} in the gallery, {unfinished} still to do")


if __name__ == "__main__":
    main()
