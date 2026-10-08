#!/usr/bin/env python3
"""Stack the untouched source view above a completed gameplay image."""
import argparse
import json
from pathlib import Path

from PIL import Image, ImageOps


def read_rgb(path, background_color="white"):
    with Image.open(path) as image:
        image = ImageOps.exif_transpose(image)
        if image.mode in ("RGBA", "LA") or "transparency" in image.info:
            rgba = image.convert("RGBA")
            background = Image.new("RGBA", rgba.size, background_color)
            return Image.alpha_composite(background, rgba).convert("RGB")
        return image.convert("RGB")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--original", type=Path, required=True)
    parser.add_argument("--generated", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--preserve-canvas", action="store_true",
                        help="Only for an explicitly requested local edit of an accepted non-16:9 image.")
    args = parser.parse_args()
    original_path, generated_path, output_path = (
        path.resolve() for path in (args.original, args.generated, args.output))
    if output_path in (original_path, generated_path) or output_path.exists():
        parser.error("Output must be a new file; source and generated files cannot be overwritten.")
    if output_path.suffix.lower() != ".png":
        parser.error("Use a .png output to preserve the completed lower panel without lossy recompression.")
    original, generated = read_rgb(original_path, "black"), read_rgb(generated_path)
    width, height = generated.size
    if not args.preserve_canvas and width * 9 != height * 16:
        parser.error("Generated scene must be exactly 16:9; do not crop or stretch it in the layout step.")
    source_size = original.size
    original = ImageOps.contain(original, (width, height), Image.Resampling.LANCZOS)
    photo_x = (width - original.width) // 2
    photo_y = (height - original.height) // 2
    comparison = Image.new("RGB", (width, height * 2), "black")
    comparison.paste(original, (photo_x, photo_y))
    comparison.paste(generated, (0, height))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation also protects against a competing write after the check.
    with output_path.open("xb") as output:
        comparison.save(output, format="PNG")
    print(json.dumps({"output": str(output_path), "size": list(comparison.size),
                      "source_size": list(source_size),
                      "original_box": [0, 0, width, height],
                      "photo_box": [photo_x, photo_y, original.width, original.height],
                      "generated_box": [0, height, width, height]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
