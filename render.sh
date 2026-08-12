#!/bin/zsh
# Render all three editions to dist/. Requires Google Chrome.
cd "$(dirname "$0")"
python3 tools/build_editions.py
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for f in report-navy:compass-2026-navy report-violet:compass-2026-blue-violet report-gold:compass-2026-violet-gold; do
  "$CHROME" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="dist/${f##*:}.pdf" "src/${f%%:*}.html"
done
python3 tools/margin_scan.py dist/compass-2026-blue-violet.pdf
echo done
