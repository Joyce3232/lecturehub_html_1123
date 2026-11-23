#!/usr/bin/env python3
"""Check 3: Static HTML validation + headless Playwright 16:9 per-slide screenshot & overflow check."""

import argparse
import re
import sys
from pathlib import Path


def static_checks(html_path: Path) -> list[str]:
    html = html_path.read_text(encoding="utf-8")
    errors = []

    # 1. Check asset image paths relative to html_path.parent
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    if not img_srcs:
        errors.append("HTML 中未嵌入任何 <img> 圖貼。")
    for src in img_srcs:
        if src.startswith(("http://", "https://", "data:")):
            continue
        target = (html_path.parent / src).resolve()
        if not target.exists():
            errors.append(f"圖片路徑不存在：{src}（預期位置：{target}）")

    # 2. Check for stray unrendered LaTeX delimiters outside <script>/<style>
    body_only = re.sub(r"<script\b[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    body_only = re.sub(r"<style\b[^>]*>.*?</style>", "", body_only, flags=re.DOTALL | re.IGNORECASE)
    if "$$" in body_only or re.search(r"\\frac\{|\\text\{|\\approx|\\longrightarrow", body_only):
        errors.append("偵測到疑似未轉譯為 MathML (<math>) 的原始 LaTeX 語法。")

    # 3. Check for MathML presence if formulas are expected
    if "<math" not in body_only:
        errors.append("未偵測到任何原生 MathML (<math>) 公式標籤。")

    return errors


def headless_browser_check(html_path: Path, screenshot_dir: Path) -> tuple[bool, list[str]]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False, [
            "尚未安裝 Python Playwright，無法執行無頭瀏覽器逐頁截圖檢查。",
            "請先執行：pip install playwright && playwright install chromium"
        ]

    screenshot_dir.mkdir(parents=True, exist_ok=True)
    issues = []
    file_url = html_path.resolve().as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        page.goto(file_url, wait_until="networkidle")

        total = page.locator(".slide").count()
        if total == 0:
            browser.close()
            return False, ["頁面中未找到任何 .slide 元素。"]

        for idx in range(total):
            page.wait_for_timeout(180)
            overflow = page.evaluate("""() => {
                const active = document.querySelector('.slide.active') || document.querySelectorAll('.slide')[0];
                if (!active) return { ok: false, reason: 'no active slide' };
                const vOverflow = active.scrollHeight > active.clientHeight + 4;
                const hOverflow = active.scrollWidth > active.clientWidth + 4;
                const brokenImgs = Array.from(active.querySelectorAll('img'))
                    .filter(img => !img.complete || img.naturalWidth === 0)
                    .map(img => img.getAttribute('src'));
                return { ok: !vOverflow && !hOverflow && brokenImgs.length === 0, vOverflow, hOverflow, brokenImgs };
            }""")
            shot_path = screenshot_dir / f"slide_{idx + 1:02d}.png"
            page.screenshot(path=str(shot_path))

            if not overflow["ok"]:
                issues.append(f"Slide {idx + 1:02d} 異常：{overflow}（截圖：{shot_path}）")

            if idx < total - 1:
                page.keyboard.press("ArrowRight")

        browser.close()

    return len(issues) == 0, issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Check 3: Validate HTML slides and capture screenshots")
    parser.add_argument("html_path", help="Path to slides/<slug>-slides.html")
    parser.add_argument("--screenshot-dir", default="/tmp/slides_check", help="Directory for slide screenshots")
    parser.add_argument("--static-only", action="store_true", help="Skip headless browser check")
    args = parser.parse_args()

    html_path = Path(args.html_path)
    if not html_path.exists():
        print(f"[FAIL] 找不到 HTML 檔案：{html_path}", file=sys.stderr)
        return 1

    static_errors = static_checks(html_path)
    if static_errors:
        print("[Check 3 FAIL] 靜態檢查未通過：")
        for err in static_errors:
            print(f"  - {err}")
        return 1
    print("[Check 3] 靜態檢查通過（圖片路徑、原生 MathML、無殘留 LaTeX）。")

    if args.static_only:
        return 0

    ok, browser_issues = headless_browser_check(html_path, Path(args.screenshot_dir))
    if not ok:
        print("[Check 3 FAIL] 無頭瀏覽器檢查未通過：")
        for issue in browser_issues:
            print(f"  - {issue}")
        return 1

    print(f"[Check 3 PASS] 無頭瀏覽器逐頁截圖與溢位檢查全數通過，截圖已存至 {args.screenshot_dir}。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
