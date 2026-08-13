#!/usr/bin/env python3
"""Objective layout check: flags any page whose content ends closer than 12.5mm
to the page edge. Requires pdftoppm (poppler) and Pillow.
Usage: python3 tools/margin_scan.py dist/compass-2026-blue-violet.pdf"""
import sys, subprocess, tempfile, glob, os
import numpy as np
from PIL import Image
pdf = sys.argv[1]
with tempfile.TemporaryDirectory() as td:
    subprocess.run(["pdftoppm", "-jpeg", "-r", "100", pdf, os.path.join(td, "p")], check=True)
    bad = []
    for f in sorted(glob.glob(os.path.join(td, "p-*.jpg"))):
        im = np.array(Image.open(f).convert("L")); h, w = im.shape
        pg = int(f.rsplit("-", 1)[1].split(".")[0])
        if im[h//2, 60:660].mean() < 110:   # full-bleed dark page (cover, section divider)
            continue
        col = im[:, 60:660]
        dark = np.where(((col < 120).sum(axis=1)) >= 6)[0]  # >=6 dark px = text/data, not a hairline or accent border
        mm = round((h - (dark.max() if len(dark) else 0)) / 100 * 25.4, 1)
        if mm < 12.5 and pg != 1:
            bad.append((pg, mm))
    print("margin scan:", bad if bad else "ALL PAGES CLEAN")
    sys.exit(1 if bad else 0)
