#!/usr/bin/env python3
"""Place one bundled, unredrawn equipment graphic into a verified empty HUD slot.

Requires Pillow. The output is a new PNG; all pixels outside the slot are preserved.
"""
import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
# Outer left frame edge in the unmodified source image. Decorative glyphs can
# protrude beyond the frame, so the whole alpha bounding box is not this anchor.
FRAME_LEFT = {'camera': 11, 'detonator': 11, 'grenade': 2, 'flamethrower': 2,
              'fire-extinguisher': 5, 'vibrator': 5, 'thermal-vision': 2,
              'night-vision': 2, 'parachute': 2}


def load_catalog():
    catalog = json.loads((ROOT / 'references/equipment-catalog.json').read_text())
    return catalog, {item['id']: item for item in catalog['items']}


def main():
    catalog, items = load_catalog()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list', action='store_true', help='List available IDs and names.')
    parser.add_argument('--input', type=Path)
    parser.add_argument('--output', type=Path, help='New .png path; never overwrites input/output.')
    parser.add_argument('--equipment', choices=sorted(set(items) | set(catalog['aliases'])))
    parser.add_argument('--box', nargs=4, type=int, metavar=('X', 'Y', 'WIDTH', 'HEIGHT'),
                        help='Verified empty slot in actual input pixels; default scales 1920x1080 layout.')
    parser.add_argument('--align-left', type=int,
                        help='Measured left edge of the money dollar glyph; aligns the icon FRAME edge to it.')
    parser.add_argument('--blank-slot-confirmed', action='store_true',
                        help='Caller has inspected the slot and confirmed no old icon overlaps it.')
    args = parser.parse_args()
    if args.list:
        print(json.dumps([{'id': item['id'], 'name_en': item['name_en'], 'name_zh': item['name_zh']}
                          for item in items.values()], ensure_ascii=False, indent=2))
        return
    if not all([args.input, args.output, args.equipment]):
        parser.error('--input, --output and --equipment are required unless using --list')
    if args.align_left is None:
        parser.error('Pass --align-left with the measured dollar-glyph left edge; do not guess a fixed nudge')
    if not args.blank_slot_confirmed:
        parser.error('Inspect/clear the equipment slot first, then pass --blank-slot-confirmed; '
                     'a transparent icon cannot erase an existing icon.')
    if args.output.suffix.lower() != '.png':
        parser.error('Use .png to preserve pixels outside the equipment slot')
    if args.output.resolve() == args.input.resolve() or args.output.exists():
        parser.error('Choose a new output path; this script never overwrites existing images')
    try:
        from PIL import Image
    except ImportError:
        parser.error('Pillow is unavailable; do not silently substitute an AI-redrawn icon')
    equipment = catalog['aliases'].get(args.equipment, args.equipment)
    item = items[equipment]
    asset = (ROOT / item['asset']).resolve()
    if not asset.is_relative_to(ROOT):
        parser.error('Asset path must remain inside the skill')
    if hashlib.sha256(asset.read_bytes()).hexdigest() != item['sha256']:
        parser.error('Bundled asset checksum differs from its catalog; verify the asset first')
    with Image.open(args.input) as source:
        image = source.convert('RGBA')
        profile = source.info.get('icc_profile')
    width, height = image.size
    scale = min(width / 1920, height / 1080)
    box = args.box or [round(width - 315 * scale), round(34 * scale),
                       max(1, round(108 * scale)), max(1, round(96 * scale))]
    x, y, slot_width, slot_height = box
    if min(x, y) < 0 or min(slot_width, slot_height) <= 0 or x + slot_width > width or y + slot_height > height:
        parser.error('Equipment box must fit wholly inside the image')
    padding = min(max(1, round(4 * scale)), max(0, (min(slot_width, slot_height) - 1) // 2))
    if not x <= args.align_left < x + slot_width:
        parser.error('Dollar-glyph anchor exceeds the verified empty slot; inspect and pass its --box')
    with Image.open(asset) as source_icon:
        icon = source_icon.convert('RGBA')
    bounds = icon.getchannel('A').getbbox()
    if bounds is None:
        parser.error('Equipment asset is empty')
    icon = icon.crop(bounds)  # Remove only unused transparent margin, never any drawn border.
    frame_delta = FRAME_LEFT.get(equipment, 4) - bounds[0]
    right_room = x + slot_width - padding - args.align_left
    fit = min((slot_width - 2 * padding) / icon.width, (slot_height - 2 * padding) / icon.height,
              right_room / (icon.width - frame_delta))
    if frame_delta > 0:
        fit = min(fit, (args.align_left - x) / frame_delta)
    if fit <= 0:
        parser.error('Aligned source icon exceeds the verified empty slot; inspect and pass a wider --box')
    icon = icon.resize((max(1, int(icon.width * fit)), max(1, int(icon.height * fit))),
                       Image.Resampling.LANCZOS)
    frame_offset = round(frame_delta * icon.width / (bounds[2] - bounds[0]))
    left = args.align_left - frame_offset
    top = y + (slot_height - icon.height) // 2
    if left < x or left + icon.width > x + slot_width:
        parser.error('Aligned source icon exceeds the verified empty slot. Inspect/clear a wider slot '
                     'and pass its --box; do not crop the icon or shift accepted money automatically.')
    image.alpha_composite(icon, (left, top))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    image.save(args.output, format='PNG', **({'icc_profile': profile} if profile else {}))
    print(json.dumps({'output': str(args.output.resolve()), 'equipment': equipment,
                      'asset': item['asset'], 'canvas': [width, height], 'slot': box,
                      'drawn_bounds': [left, top, icon.width, icon.height],
                      'frame_left': left + frame_offset,
                      'method': 'source-asset-alpha-composite; no AI redraw'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
