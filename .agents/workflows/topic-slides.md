---
description: 融合 example/ 教學法與 Graph 雙閘門檢查，根據指定範圍產出讓初學者也能看懂的 16:9 教學型 HTML 簡報（/topic-slides）
---

# `/topic-slides` — Graph 式教學型 HTML 簡報產製 Workflow

本工作流依循 `SLIDES_WORKFLOW.md` 的 **State Graph** 規範執行，融合 `example/` 筆記的**「一句話核心 ＋ 因果知識地圖 ＋ 先動機後機制 ＋ 直覺解讀 ＋ 跨頁銜接提問」**教學撰寫法，確保**原本不熟悉該主題的人也能理解基本概念**，並強制包含 **雙人工確認閘門（Human Gate 1 & 2）** 與 **三道獨立驗證腳本（Check 1–3）**。

---

## 執行步驟

### Step 0：鎖定範圍、盤點來源與圖貼資源
1. **確認內容範圍（Scope Lock）**：嚴格對齊使用者本次指定的章節、主題或頁面範圍，**不擅自塞入範圍外的艱深細節**。
2. 讀取 `wiki/index.md` 與範圍內相關的 `wiki/sources/`、`wiki/concepts/`、`wiki/entities/`、`wiki/comparisons/` 頁面。
3. 列出 `slides/assets/`（若無則從根目錄 `assets/` 同步）可用的圖貼檔名清單。

### Step 1：Node 1 — 生成教學型簡報大綱（`slides/outline.md`）
參考 `example/00-總索引與知識地圖.md` 的大綱設計法，於 `slides/outline.md` 包含：
1. **全簡報因果知識地圖（Knowledge Map）**：用流程圖或箭頭標註各頁之間的因果與演進關係（例如：`痛點動機 → 基本定義 → 核心機制 → 副作用／衝突 → 解法與實務`）。
2. 規劃 **15–18 頁完整教學版**，每頁標註編號（`## Slide 01:` …）、**一句話核心（One-sentence Core）**、**教學目標與銜接提問**、**核心結論／範圍涵蓋**與對應 `[[wikilink]]` 來源，寫入 `slides/outline.md`（保留為可編輯中繼檔）。
4. **執行 Check 1 腳本**：
   ```bash
   python3 .agents/workflows/scripts/check_outline.py slides/outline.md
   ```
   - 若腳本回傳非 0（未通過），依錯誤訊息自動修正 `slides/outline.md` 並重跑腳本，直到通過。
5. **Human Gate 1（停下等待確認）**：將 `slides/outline.md` 呈現給使用者，**未獲明確核准前嚴禁進入 Step 2**。

### Step 2：Node 2 — 生成教學型逐頁內容規格（`slides/slide-spec.md`）
融合 `example/` 深入解說版的寫法，並嚴格遵守**「雙軌並陳：白話入門 ＋ 專業深入（由淺入深）」**原則，依核准大綱逐頁編寫 `slides/slide-spec.md`（每頁以 `## Slide XX:` 開頭）：
1. **生活比喻先行（Analogy First）**：每頁先用**日常生活比喻**講懂觀念（例如：RAM = 書桌桌面、硬碟 = 書櫃、Page Table = 目錄清單、TLB = 桌角速查便利貼），建立直覺畫面。
2. **雙軌並陳（白話定義 ＋ 專業深入解說）**：每頁畫面內容必須同時包含「**白話口語解釋**」與「**專業技術深入解說**」（含完整英文術語、底層硬體機制、位元/暫存器細節、演算法步驟與實務代價），讓初學者看懂、進階者也能學到完整系統原理。
3. **先動機、再定義、後機制（Why → What → How）**：先點出「沒有這個技術會怎樣」，再給白話定義，最後展開專業機制與細節。
4. **公式逐字翻譯＋完整推導＋數字例**：每個數學公式旁必須逐一翻譯變數符號，並搭配「**直覺解讀**」與具體數值計算範例。
5. **對比表格、重點標記與過渡提問**：易混淆概念用表格對照，區分「🔑 核心直覺」與「⚠️ 常見誤區」，並在頁尾留一句銜接下一頁的提問。
6. **視覺、圖示、字數密度與溯源欄位**：講解程式碼、指標或演算法運作時**可以適當搭配 SVG 圖示**（標註 `圖示設計`），並指定版面配置、`assets/<檔名>.jpeg` 邊角或右側插畫，以及 `[[wikilink]]` 溯源；單頁須兼顧內容充實度（不可過少空洞）與不爆框（Split/含圖貼版面字數上限較緊）。
7. **執行 Check 2 腳本**（前置檢查字數上下限、`白話入門` + `專業深入` 雙軌、`過渡提問`、公式括號平衡與圖貼存在性）：
   ```bash
   python3 .agents/workflows/scripts/check_slide_spec.py slides/slide-spec.md --assets-dir slides/assets
   ```
   - 若腳本回傳非 0，僅針對未通過的單頁精簡或補齊，直到全數通過。
8. **Human Gate 2（停下等待確認）**：呈現 `slides/slide-spec.md` 給使用者確認，**未獲核准前嚴禁進入 Step 3**。

### Step 3：Node 3 — 渲染 16:9 HTML 簡報（`slides/<slug>-slides.html`）
1. 依 `slides/slide-spec.md` 產出 `slides/<slug>-slides.html`：
   - **互動模式**：16:9 單頁舞台，支援鍵盤 `←` / `→`、`PageUp` / `PageDown`、`Space` 翻頁、跳頁選單與底部進度條。
   - **視覺風格與圖示**：Warm Bento Pastel（暖米白畫布＋柔橘／抹茶綠／柔粉卡片），圖貼採 `mix-blend-mode: multiply` 與 Radial Mask 柔邊融合；指標與演算法頁面**可以適當內嵌 SVG 圖示**。
   - **數學公式**：一律使用瀏覽器原生 **MathML（`<math>`）**，不可依賴外部 CDN。
2. **執行 Check 3 腳本（靜態檢查 ＋ 無頭瀏覽器逐頁截圖）**：
   ```bash
   python3 .agents/workflows/scripts/check_html_slides.py slides/<slug>-slides.html --screenshot-dir /tmp/slides_check
   ```
   - 腳本檢查圖片路徑、`<math>` 與殘留 `$` LaTeX 語法，並以無頭瀏覽器（`1280x720`）逐頁按 `ArrowRight` 偵測溢位與產出截圖。
   - 若任一頁出現裁切、遮擋或排版異常，僅修正該頁 CSS／文案並重跑 Check 3，直到全數通過。
3. 交付最終 `slides/<slug>-slides.html` 連結（`slides/outline.md` 與 `slides/slide-spec.md` 保留於 `slides/`）。
