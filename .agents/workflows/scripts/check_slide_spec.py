#!/usr/bin/env python3
"""Check 2: Validate slides/slide-spec.md density (min/max), dual-track depth, formulas, assets, and wikilinks."""

import argparse
import re
import sys
from pathlib import Path


def parse_slides(text: str) -> list[tuple[str, str]]:
    pattern = re.compile(r"^(##\s+Slide\s+\d+.*)$", re.MULTILINE)
    matches = list(pattern.finditer(text))
    result = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        result.append((m.group(1).strip(), text[start:end].strip()))
    return result


def extract_field(body: str, field_names: tuple[str, ...]) -> str:
    """Extract content belonging to a bullet field like '- **白話入門**：...' until the next top-level field."""
    joined = "|".join(re.escape(name) for name in field_names)
    pattern = re.compile(
        rf"^-\s+\*\*(?:{joined})\*\*[：:]\s*(.*?)(?=^-\s+\*\*|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    m = pattern.search(body)
    return m.group(1).strip() if m else ""


def check_formula_balance(body: str) -> list[str]:
    """Pre-check LaTeX $ / $$ balance before Node 3 HTML/MathML conversion."""
    issues = []
    block_count = len(re.findall(r"(?<!\\)\$\$", body))
    if block_count % 2 != 0:
        issues.append("區塊公式 `$$` 未成對閉合。")

    stripped = re.sub(r"(?<!\\)\$\$.*?(?<!\\)\$\$", "", body, flags=re.DOTALL)
    stripped = stripped.replace(r"\$", "")
    for line in stripped.splitlines():
        # Remove standalone currency like $47,000 when no closing $ exists on the same line
        cleaned = re.sub(r"\$\d[\d,.]*(?=\s*(?:美元|元|USD|NTD|TWD|[，。；、）)]|$))(?!.*\$)", "", line)
        if cleaned.count("$") % 2 != 0:
            issues.append(f"行內公式 `$` 未成對閉合：{line.strip()[:40]}…")
            break
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Check 2: Validate slide-spec.md")
    parser.add_argument("spec_path", help="Path to slides/slide-spec.md")
    parser.add_argument("--assets-dir", default="slides/assets", help="Path to assets directory")
    parser.add_argument("--min-chars", type=int, default=260, help="Min non-whitespace chars per slide (prevent overly sparse slides)")
    parser.add_argument("--max-chars", type=int, default=1350, help="Max non-whitespace chars per full-width slide")
    parser.add_argument("--split-max-chars", type=int, default=1150, help="Max non-whitespace chars for Split/sticker slides")
    parser.add_argument("--min-track-chars", type=int, default=35, help="Min non-whitespace chars for each dual-track section")
    args = parser.parse_args()

    spec_path = Path(args.spec_path)
    if not spec_path.exists():
        print(f"[FAIL] 找不到逐頁規格檔：{spec_path}", file=sys.stderr)
        return 1

    text = spec_path.read_text(encoding="utf-8")
    slides = parse_slides(text)
    if not slides:
        print("[Check 2 FAIL] 未偵測到任何 '## Slide XX:' 區塊。")
        return 1

    assets_dir = Path(args.assets_dir)
    errors = []
    sticker_count = 0
    total_slides = len(slides)

    for idx, (header, body) in enumerate(slides):
        char_len = len(re.sub(r"\s+", "", body))
        has_sticker = bool(re.search(r"assets/[A-Za-z0-9._-]+\.(?:jpeg|jpg|png|webp|svg)", body, flags=re.IGNORECASE))
        is_split = bool(re.search(r"版面配置\*\*.*Split", body, flags=re.IGNORECASE))
        effective_max = args.split_max_chars if (is_split or has_sticker) else args.max_chars

        if char_len < args.min_chars:
            errors.append(
                f"{header}：內文過少（{char_len} 字元 < 下限 {args.min_chars}），請充實白話比喻與專業機制解說。"
            )
        if char_len > effective_max:
            layout_note = "Split/含圖貼版面" if (is_split or has_sticker) else "一般版面"
            errors.append(
                f"{header}：內文過長（{char_len} 字元 > {layout_note}上限 {effective_max}），請精簡或拆頁以防 16:9 爆框。"
            )

        # Dual-track check: both 白話入門 and 專業深入 must exist and be non-trivial
        beginner_text = extract_field(body, ("白話入門", "白話比喻", "白話解說"))
        pro_text = extract_field(body, ("專業深入", "專業解說", "專業機制"))
        if not beginner_text:
            errors.append(f"{header}：缺少「白話入門」區塊（須兼顧初學者直覺比喻）。")
        elif len(re.sub(r"\s+", "", beginner_text)) < args.min_track_chars:
            errors.append(f"{header}：「白話入門」過短（< {args.min_track_chars} 字元），請補充生活比喻或白話定義。")

        if not pro_text:
            errors.append(f"{header}：缺少「專業深入」區塊（須提供完整技術原理與細節）。")
        elif len(re.sub(r"\s+", "", pro_text)) < args.min_track_chars:
            errors.append(f"{header}：「專業深入」過短（< {args.min_track_chars} 字元），請補充硬體/演算法/公式細節。")

        # Transition question check (all slides except the final summary slide)
        if idx < total_slides - 1 and "過渡提問" not in body:
            errors.append(f"{header}：缺少引導下一頁的「過渡提問」。")

        # Formula balance pre-check
        for f_err in check_formula_balance(body):
            errors.append(f"{header}：{f_err}")

        if "[[" not in body or "]]" not in body:
            errors.append(f"{header}：缺少 [[wikilink]] 來源溯源。")

        for asset_ref in re.findall(r"assets/([A-Za-z0-9._-]+\.(?:jpeg|jpg|png|webp|svg))", body, flags=re.IGNORECASE):
            sticker_count += 1
            if assets_dir.exists() and not (assets_dir / asset_ref).exists():
                errors.append(f"{header}：引用的圖貼不存在於 {assets_dir / asset_ref}。")

    if sticker_count == 0:
        errors.append("整份規格書未配置任何 assets/ 圖貼。")

    if errors:
        print("[Check 2 FAIL] 逐頁規格檢查未通過：")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(
        f"[Check 2 PASS] 共 {len(slides)} 頁通過雙軌內容、字數上下限（{args.min_chars}–{args.max_chars}）、"
        f"公式平衡與溯源檢查，共配置 {sticker_count} 次圖貼。"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
