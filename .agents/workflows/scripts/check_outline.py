#!/usr/bin/env python3
"""Check 1: Validate slides/outline.md structure, slide count, granularity, and wiki coverage."""

import argparse
import re
import sys
from pathlib import Path


def parse_slides(text: str) -> list[tuple[int, str, str]]:
    pattern = re.compile(r"^##\s+Slide\s+(\d+)\b(.*)$", re.MULTILINE)
    matches = list(pattern.finditer(text))
    result = []
    for i, m in enumerate(matches):
        num = int(m.group(1))
        header = m.group(0).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        result.append((num, header, text[start:end].strip()))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Check 1: Validate slides/outline.md")
    parser.add_argument("outline_path", help="Path to slides/outline.md")
    parser.add_argument("--min-chars", type=int, default=60, help="Min non-whitespace chars per outline slide")
    parser.add_argument("--max-chars", type=int, default=450, help="Max non-whitespace chars per outline slide")
    args = parser.parse_args()

    outline_path = Path(args.outline_path)
    if not outline_path.exists():
        print(f"[FAIL] 找不到大綱檔案：{outline_path}", file=sys.stderr)
        return 1

    text = outline_path.read_text(encoding="utf-8")
    slides = parse_slides(text)
    wikilinks = re.findall(r"\[\[([^\]]+)\]\]", text)

    errors = []
    if not (15 <= len(slides) <= 18):
        errors.append(f"投影片頁數須為 15–18 頁完整教學版（目前為 {len(slides)} 頁）。")

    expected = list(range(1, len(slides) + 1))
    actual_nums = [num for num, _, _ in slides]
    if actual_nums != expected:
        errors.append(f"投影片編號未連續遞增（偵測到：{actual_nums}）。")

    if "知識地圖" not in text and "Knowledge Map" not in text:
        errors.append("大綱中缺少「全簡報因果知識地圖（Knowledge Map）」。")

    if not wikilinks:
        errors.append("大綱中未包含任何 [[wikilink]] 來源溯源。")

    if "核心結論" not in text and "Key Takeaways" not in text:
        errors.append("大綱中未明確標註「核心結論 / Key Takeaways」涵蓋規劃。")

    total_slides = len(slides)
    for idx, (num, header, body) in enumerate(slides):
        char_len = len(re.sub(r"\s+", "", body))
        if char_len < args.min_chars:
            errors.append(f"{header}：大綱說明過於簡略（{char_len} 字元 < 下限 {args.min_chars}），請補充教學目標與重點。")
        elif char_len > args.max_chars:
            errors.append(f"{header}：單頁概念過多過載（{char_len} 字元 > 上限 {args.max_chars}），請拆分為兩頁。")

        if "一句話核心" not in body and "One-sentence Core" not in body:
            errors.append(f"{header}：缺少「一句話核心」。")

        if "[[" not in body or "]]" not in body:
            errors.append(f"{header}：缺少 [[wikilink]] 來源溯源。")

        if idx < total_slides - 1 and "銜接提問" not in body:
            errors.append(f"{header}：缺少引導下一頁的「銜接提問」。")

    if errors:
        print("[Check 1 FAIL] 大綱檢查未通過：")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(f"[Check 1 PASS] 共 {len(slides)} 頁投影片，通過知識地圖、粒度與 {len(set(wikilinks))} 個不重複 [[wikilink]] 檢查。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
