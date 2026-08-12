#!/usr/bin/env python3
"""Derive the violet and gold editions from src/report-navy.html (the master).
Run from anywhere: python3 tools/build_editions.py"""
import re, os
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(HERE, "src") + os.sep
COLORMAP = {
 "#051C2C":"#231849", "#9AA6B2":"#9D96B4", "#2251FF":"#6C4CF1", "#1F2A36":"#2C2347",
 "#D6DDE4":"#DED8EC", "#6E7B87":"#6F6890", "#E3EAF1":"#EAE5F7", "#4B5A68":"#4F466E",
 "#B9C6D4":"#B9B0D0", "#3E6EC4":"#5D3BD8", "#C9DCF1":"#D8CCF7", "#A3C2E8":"#B4A3EE",
 "#6E9AD9":"#8B6FE4", "#1F4BA0":"#4527B8", "#EDF1F5":"#F1EEF9", "#C2CCD6":"#CCC5DE",
 "#E3EDF8":"#EFE9FC", "#B9C7D4":"#C8BEE3", "#C9D6E4":"#D2C9E6", "#F3F6F9":"#F7F4FC",
 "#7E97AC":"#9C8FC7", "#EDF2F8":"#F0EBFA", "#54708A":"#6F5F9E", "#DADFE4":"#E2DDEF",
 "#F7FAFD":"#FBF9FE", "#EFF5FB":"#F5F1FD", "#E4EEF8":"#EDE7FB", "#D8E7F6":"#E4DCF9",
 "#CBDFF4":"#DBD0F7", "#BFD7F2":"#D2C5F4", "#22384F":"#2F2453", "#3A536E":"#4A3C6E",
 "#DCE6F4":"#E4DCF6", "#B7C8E2":"#C0B3DE", "#24425C":"#3B2D6B", "#9FB2C4":"#B3A8D2",
 "#00A9F4":"#8FA8FF", "#F2F5F8":"#F5F1FB", "#0B2A47":"#33205F",
}
YBG, YF, YT = "#E8A800", "#DB9A00", "#9A6A00"
def transform(s, yellow=False):
    ed = "Violet-Gold Edition" if yellow else "Blue-Violet Edition"
    s = s.replace("<title>Enterprise Agentic AI Adoption Compass 2026</title>",
                  f"<title>Enterprise Agentic AI Adoption Compass 2026 ({ed})</title>")
    s = s.replace('font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;-webkit-print-color-adjust:exact;',
                  'font-family:"Avenir Next","Helvetica Neue",Arial,sans-serif;-webkit-print-color-adjust:exact;')
    s = s.replace('font-family:Georgia,"Times New Roman",serif', 'font-family:Charter,Georgia,serif')
    s = s.replace('font-family:Georgia,serif', 'font-family:Charter,Georgia,serif')
    s = s.replace('font-family="Helvetica Neue,Helvetica,Arial,sans-serif"',
                  'font-family="Avenir Next,Helvetica Neue,Arial,sans-serif"')
    s = s.replace("  .eyebrow{", '  .eyebrow::before{content:"\\2726  ";color:#8FA8FF;}\n  .eyebrow{', 1)
    s = s.replace(".exnum{font-size:8pt;font-weight:700;color:var(--blue);margin-bottom:1.3mm;}",
                  ".exnum{font-size:8pt;font-weight:700;color:var(--blue);margin-bottom:1.3mm;letter-spacing:0.06em;}")
    s = s.replace(".cbar{height:4.6mm;background:var(--navy);}",
                  ".cbar{height:4.6mm;background:var(--navy);border-radius:0 1.6mm 1.6mm 0;}")
    s = s.replace(".movebox{background:var(--tint);padding:2.2mm 3.2mm;margin-top:2mm;font-size:8.4pt;line-height:1.4;}",
                  ".movebox{background:var(--tint);padding:2.4mm 3.4mm;margin-top:2mm;font-size:8.4pt;line-height:1.4;border-radius:2.2mm;}")
    s = re.sub(r'\.ibn\{[^}]*\}',
               '.ibn{font-family:"Avenir Next",Arial,sans-serif;font-size:11pt;font-weight:700;color:#fff;background:#2251FF;width:6.6mm;height:6.6mm;flex:none;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-top:0.4mm;}',
               s, count=1)
    s = s.replace(".cov-art .c{width:14.8mm;height:9.2mm;border:0.26mm solid rgba(255,255,255,0.15);margin:-0.13mm;}",
                  ".cov-art .c{width:14.8mm;height:9.2mm;border:0.26mm solid rgba(255,255,255,0.15);margin:-0.13mm;border-radius:1mm;}")
    s = s.replace(".gt{border:0.5pt solid var(--hair);", ".gt{border-radius:2.4mm;border:0.5pt solid var(--hair);")
    s = s.replace(".bbar{height:3.6mm;background:var(--navy);}",
                  ".bbar{height:3.6mm;background:var(--navy);border-radius:0 1.3mm 1.3mm 0;}")
    s = s.replace(".btrk{position:relative;height:3.6mm;background:#F2F5F8;}",
                  ".btrk{position:relative;height:3.6mm;background:#F2F5F8;border-radius:0 1.3mm 1.3mm 0;}")
    s = s.replace("Blue marks 2026", "Gold marks 2026" if yellow else "Violet marks 2026")
    s = s.replace("blue marker", "gold marker" if yellow else "violet marker")
    s = s.replace("(blue: enterprise segment)", "(violet: enterprise segment)")
    s = s.replace("early 2026 (blue)", "early 2026 (violet)")
    s = s.replace("rgba(34,81,255,", "rgba(108,76,241,")
    for k, v in COLORMAP.items():
        s = s.replace(k, v)
    s = re.sub(r'(\.whynow \.wl\{[^}]*color:)#9C8FC7', r'\g<1>#8FA8FF', s)
    if yellow:
        s = s.replace("--cyan:#8FA8FF", f"--cyan:{YBG}")
        s = s.replace('.eyebrow::before{content:"\\2726  ";color:#8FA8FF;}',
                      f'.eyebrow::before{{content:"\\2726  ";color:{YF};}}')
        s = re.sub(r'(\.whynow \.wl\{[^}]*color:)#8FA8FF', r'\g<1>' + YF, s)
        s = s.replace(".bbar.hi{background:var(--blue);}", f".bbar.hi{{background:{YF};}}")
        s = s.replace("  .bmk{", f"  .cbar.hi{{background:{YF};}}\n  .bmk{{", 1)
        tl = re.search(r'<div class="exsub">Milestone events[\s\S]*?</svg>', s)
        if tl:
            t = tl.group(0)
            t = t.replace('<tspan font-weight="700" fill="#6C4CF1">', f'<tspan font-weight="700" fill="{YT}">')
            t = t.replace('r="4.2" fill="#6C4CF1"', f'r="4.2" fill="{YF}"')
            t = t.replace('r="7.6" fill="#6C4CF1"', f'r="7.6" fill="{YF}"')
            t = t.replace('height="8" fill="#6C4CF1"', f'height="8" fill="{YF}"')
            s = s[:tl.start()] + t + s[tl.end():]
        s = s.replace(".gt.bl{background:linear-gradient(150deg,#6C4CF1 0%,#4527B8 100%);border-color:var(--blue);}",
                      f".gt.bl{{background:linear-gradient(150deg,{YBG} 0%,#D08E00 100%);border-color:{YBG};}}")
        s = s.replace(".gt.bl .gk{color:#C9D6FF;}", ".gt.bl .gk{color:#7A5600;}")
        s = s.replace(".gt.bl .gnum{color:#fff;}", ".gt.bl .gnum{color:var(--navy);}")
        s = s.replace(".gt.bl .gcap{color:#DCE4FF;}", ".gt.bl .gcap{color:#4A3600;}")
        s = s.replace(".gt.bl .gcap b{color:#fff;}", ".gt.bl .gcap b{color:var(--navy);}")
        s = s.replace('fill="#DCE4FF"', 'fill="#6B4A00"')
        s = s.replace(".gt.dk .gk{color:#7F9BFF;}", f".gt.dk .gk{{color:{YBG};}}")
        star = re.search(r'<path d="M 210 10 l[^"]*" fill="#6C4CF1"/>', s)
        if star:
            s = s[:star.start()] + star.group(0).replace('#6C4CF1', YF) + s[star.end():]
        s = s.replace('text-anchor="end" fill="#6C4CF1" font-weight="700">9B specialist',
                      f'text-anchor="end" fill="{YT}" font-weight="700">9B specialist')
    return s
src = open(D + "report-navy.html").read()
open(D + "report-violet.html", "w").write(transform(src, False))
open(D + "report-gold.html", "w").write(transform(src, True))
print("editions rebuilt from master")
