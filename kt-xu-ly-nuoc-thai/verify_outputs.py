import os
import re

md_path = r"C:\antgravity workplace\hcmut-263\kt xu ly nuoc thai\indexes\test_branches_deep\wastewater_treatment_deep_branches.md"
html_path = r"C:\antgravity workplace\hcmut-263\kt xu ly nuoc thai\indexes\test_branches_deep\wastewater_treatment_deep_branches.html"

md_size = os.path.getsize(md_path)
html_size = os.path.getsize(html_path)

with open(md_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

headings = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
bullets = 0
tables = 0

for line in lines:
    stripped = line.strip()
    if stripped.startswith("# "):
        headings[1] += 1
    elif stripped.startswith("## "):
        headings[2] += 1
    elif stripped.startswith("### "):
        headings[3] += 1
    elif stripped.startswith("#### "):
        headings[4] += 1
    elif stripped.startswith("##### "):
        headings[5] += 1
    elif stripped.startswith("###### "):
        headings[6] += 1
    elif stripped.startswith("- ") or stripped.startswith("* "):
        bullets += 1
    elif stripped.startswith("|") and stripped.endswith("|"):
        tables += 1

text = "".join(lines)
math_inline = len(re.findall(r"\$[^$\n]+\$", text))
math_block = len(re.findall(r"\$\$[^$]+\$\$", text))

print("=== VERIFICATION SUMMARY ===")
print(f"Markdown Path: {md_path}")
print(f"Markdown Size: {md_size:,} bytes ({md_size / (1024*1024):.2f} MB)")
print(f"Total Lines: {len(lines):,}")
print(f"Level 1 (Document Root): {headings[1]}")
print(f"Level 2 (Chapters): {headings[2]}")
print(f"Level 3 (Main Sections): {headings[3]}")
print(f"Level 4 (Subsections): {headings[4]}")
print(f"Level 5 (Deep Concepts): {headings[5]}")
print(f"Level 6 (Granular Elements / Examples): {headings[6]}")
print(f"Total Headings (L1-L6): {sum(headings.values()):,}")
print(f"Total Bullet Points: {bullets:,}")
print(f"Total Information Nodes: {sum(headings.values()) + bullets:,}")
print(f"Inline Math Formulas ($...$): {math_inline:,}")
print(f"Block Math Formulas ($$...$$): {math_block:,}")
print("----------------------------")
print(f"HTML Path: {html_path}")
print(f"HTML Size: {html_size:,} bytes ({html_size / (1024*1024):.2f} MB)")
print(f"HTML Exists and Valid: {os.path.exists(html_path) and html_size > 1000000}")
