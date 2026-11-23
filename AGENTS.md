# AGENTS.md — 跨文 LLM Wiki 知識庫運作規範

本專案參考 Andrej Karpathy 的 LLM Wiki 模式，打造一個**分軌收納、跨文整合、支援全自動批次增量更新**的個人研究知識庫。Agent 為 `wiki/` 層的唯一維護者，負責閱讀 `raw/` 原始資料並持續編譯、交叉比對與維護知識結構。

---

## 1. 核心架構與目錄邊界

```text
LLM Wiki 2/
├── AGENTS.md                  # 本規範文件
├── SLIDES_WORKFLOW.md         # HTML 簡報產製 Graph 規範
├── .gitignore                 # Git 忽略規則
├── .agents/
│   └── workflows/             # Workflow 定義與 Check 1–3 驗證腳本
├── assets/                    # 簡報圖貼總庫（Ingest / Lint 一律略過）
├── slides/                    # 產製中繼檔（outline.md / slide-spec.md）與 16:9 HTML 簡報
├── raw/                       # 唯讀原始資料層（嚴禁修改或刪除）
│   ├── docs/                  # PDF（論文、簡報、報告）
│   ├── web/                   # 網頁剪藏 Markdown（Web Clipper）
│   ├── notes/                 # 個人筆記、逐字稿、純文字
│   └── data/                  # 數據表格（CSV/XLSX）與程式碼
└── wiki/                      # Agent 全權維護的知識層
    ├── index.md               # 全站分類總目錄（每次更新必同步）
    ├── log.md                 # 增量時間軸紀錄（append-only）
    ├── sources/               # 各原始檔的結構化摘要（對應 raw/ 四軌）
    │   ├── docs/
    │   ├── web/
    │   ├── notes/
    │   └── data/
    ├── concepts/              # 跨來源抽出的核心概念頁
    ├── entities/              # 模型、機構、工具、人物、資料集等實體頁
    └── comparisons/           # 跨文件比較矩陣、觀點演變與衝突盤點
```

### 邊界規則
1. **`raw/` 唯讀原則**：`raw/` 為唯一事實來源（Source of Truth），Agent 只能讀取，不可修改或覆寫裡面的原始檔案。
2. **`assets/` 排除原則**：`assets/` 內的圖片專供後續製作 HTML 簡報使用，執行 Batch Ingest 與 Lint 時一律忽略（不可當作待處理的 `raw/` 資料），僅在日後產生簡報時引用。
3. **忽略 `.gitkeep`**：各空資料夾內的 `.gitkeep` 僅用於 Git 目錄追蹤，掃描時一律略過。

---

## 2. 來源接收規則（從對話直接新增來源時）

當使用者在對話中直接提供新資料時，依下列規則自動歸檔至 `raw/`，再接續執行 Ingest：
- **對話直接提供 PDF 檔案**：將檔案存入 `raw/docs/`。
- **提供 arXiv 或論文 PDF 連結**：下載對應 PDF 至 `raw/docs/`（建議命名為 `<FirstAuthor><Year>-<ShortTitle>.pdf`，例如 `Vaswani2017-Transformer.pdf`）。
- **提供一般網頁文章連結**：擷取或轉換為乾淨 Markdown 後存入 `raw/web/`。
- **提供純文字筆記、逐字稿或數據／程式碼**：分別存入 `raw/notes/` 或 `raw/data/`。

---

## 3. 語言、數學公式與檔名規範

### 語言與術語
- 內文一律使用**繁體中文（台灣習慣用語）**撰寫。
- 關鍵技術術語、模型名稱、評估指標與論文標題**保留英文原文**（例如：`Self-Attention`、`Ablation Study`、`KV Cache`、`Perplexity`）。

### 數學與演算法保留原則
- 論文、技術報告或筆記中的**關鍵數學推導、Loss Function 與演算法虛擬碼（Pseudocode）必須完整保留**，不可僅用文字帶過。
- 數學式統一使用標準 LaTeX 語法：行內公式使用 `$...$`，獨立區塊公式使用 `$$...$$`。

### 檔名格式
- **`wiki/sources/docs/`（論文／報告）**：使用「簡潔代號＋簡稱」，格式為 `<FirstAuthor><Year>-<ShortTitle>.md`，例如：`Vaswani2017-Transformer.md`。
- **`wiki/sources/web/`、`notes/`、`data/`**：使用具辨識度的英文 kebab-case 或 `YYYY-MM-DD-<slug>.md`（例如：`2026-04-02-karpathy-llm-wiki.md`）。
- **`wiki/concepts/`、`entities/`、`comparisons/`**：使用語意明確的英文 kebab-case（例如：`self-attention.md`、`context-window.md`、`rag-vs-llm-wiki.md`）。

---

## 4. 頁面格式與 Obsidian / Dataview 規範

所有 `wiki/` 下的筆記（`index.md` 與 `log.md` 除外）必須包含統一的 YAML Frontmatter 與結構化區塊，以支援 Obsidian Graph View 與 Dataview 動態查詢。

### YAML Frontmatter 範本
```yaml
---
title: "頁面標題（可含英文原文）"
type: source # source | concept | entity | comparison
source_type: docs # docs | web | notes | data | mixed（comparisons 或跨來源概念用 mixed）
raw_file: "raw/docs/Vaswani2017-Transformer.pdf" # 若為 concept/comparison 可列主要來源或留空陣列
source_url: "" # 原文連結或 arXiv URL（無則留空）
source_date: "2017-06-12" # 原始資料發表／建立日期（YYYY-MM-DD）
ingested_at: "2026-11-22" # 寫入 Wiki 日期（YYYY-MM-DD）
status: active # active | draft | superseded
tags:
  - transformer
  - attention
---
```

### 頁面內容必備規範
1. **`## 核心結論（Key Takeaways）`**：每篇 `sources/`、`concepts/` 與 `comparisons/` 頁面**必須固定保留此區塊**（建議 3–5 點精煉條列），方便日後直接抽取製作 HTML 簡報。
2. **雙向連結**：提及任何已存在或值得獨立成頁的概念、模型、論文或實體時，一律使用 Obsidian `[[wikilink]]` 串聯（例如：`[[Vaswani2017-Transformer]]`、`[[self-attention]]`）。
3. **多軌道讀取重點**：
   - `docs/`：提煉研究問題、核心方法、數學推導／Loss Function、實驗設定與主要結論。
   - `web/`：過濾廣告與導覽雜訊，保留原出處 URL、核心觀點與實務洞察。
   - `notes/`：保留使用者的原始疑問、靈感脈絡與待驗證假設。
   - `data/`：萃取資料欄位結構（Schema）、統計摘要、關鍵實驗數據或核心程式邏輯（不整段貼入原始碼）。

---

## 5. 跨文比較與衝突處理（`wiki/comparisons/`）

1. **主題導向比較矩陣**：當兩份以上來源討論相同主題、技術路線或研究問題時，於 `wiki/comparisons/` 建立或更新以「主題／研究問題」為單位的比較矩陣表（Markdown Table），並列各來源的假設、方法、指標與適用條件。
2. **禁止靜默覆蓋（衝突標記規範）**：若新來源的數據、實驗結論或觀點與既有頁面矛盾，**嚴禁直接覆蓋舊內容**。必須保留雙方出處連結，並使用 Obsidian Callout 醒目標註：
   ```markdown
   > [!warning] 觀點衝突
   > - **來源 A（[[頁面A]]）**：主張……
   > - **來源 B（[[頁面B]]）**：指出……
   > - **差異脈絡**：可能源自資料集、前提假設或發表時間差異。
   ```
3. **觀點演變追蹤**：若同一主題橫跨不同時期或版本，在 `comparisons/` 或對應 `concepts/` 頁面中記錄論點隨時間的演進脈絡。

---

## 6. 核心操作流程

### Operation A：Batch Ingest（全自動批次增量掃描）
當使用者要求「掃描 `raw/`」、「更新 Wiki」或提供新檔案時，**全自動執行以下步驟**（無需逐篇停下詢問）：
1. **盤點未處理檔案**：掃描 `raw/docs/`、`raw/web/`、`raw/notes/`、`raw/data/`（略過 `.gitkeep` 與 `assets/`），比對 `wiki/sources/` 中所有頁面的 `raw_file` 欄位，找出尚未 Ingest 或內容有異動的檔案。
2. **分軌寫入摘要**：依序讀取未處理檔案，在對應的 `wiki/sources/<track>/` 建立結構化摘要頁（含完整數學推導／公式與 `## 核心結論（Key Takeaways）`）。
3. **跨文整合更新**：
   - 更新或新建相關的 `wiki/concepts/` 與 `wiki/entities/` 頁面，補上新來源的 `[[wikilink]]`。
   - 若與既有來源產生關聯、演變或矛盾，同步更新 `wiki/comparisons/` 並加上 `> [!warning] 觀點衝突` 標記。
4. **同步索引與日誌**：
   - 更新 `wiki/index.md` 的分類目錄與連結。
   - 在 `wiki/log.md` 尾端追加紀錄，每筆必須以固定格式開頭（方便 `grep` 檢索）：
     `## [YYYY-MM-DD] ingest | <檔案或批次標題>`
5. **回報 Git 風格變更摘要**：全部更新完成後，向使用者輸出結構化總結，條列本次**新增頁面**、**更新頁面**、**偵測到的跨文衝突**，以及建議的 **Git commit message**。

### Operation B：Query（跨文問答與知識沉澱）
1. 先讀取 `wiki/index.md` 定位相關頁面，再深入閱讀對應的 `sources/`、`concepts/`、`comparisons/` 與必要的 `raw/` 原文細節。
2. 回答時須附上 `[[wikilink]]` 來源依據與精確數據／公式。
3. 若該次問答產出了高價值的跨文件對比或綜合洞見，主動寫入（或建議寫入）`wiki/comparisons/`，並同步更新 `index.md` 與 `log.md`（前綴 `## [YYYY-MM-DD] query | <主題>`）。

### Operation C：Lint（知識庫健康檢查）
定期或依使用者指示執行以下檢查，並回報修復結果或建議清單：
- **漏掃檢查**：`raw/` 中是否有尚未對應到 `wiki/sources/` 的檔案。
- **孤島頁面**：`wiki/` 中沒有任何連入 `[[wikilink]]` 的頁面。
- **斷裂連結**：指向不存在頁面的 `[[wikilink]]`。
- **未解衝突**：列出目前標記為 `> [!warning] 觀點衝突` 且尚未釐清的項目。
- **Frontmatter 完整性**：檢查是否缺少 Dataview 所需的必要欄位。

### Operation D：HTML 簡報產製（Slides Graph Workflow）
當使用者要求將 `wiki/` 內容製作成 HTML 投影片時，一律遵循 [SLIDES_WORKFLOW.md](SLIDES_WORKFLOW.md) 定義的 **State Graph 流程**（`Node 1 大綱 → Gate 1 → Node 2 逐頁內容 → Gate 2 → Node 3 HTML 渲染與無頭瀏覽器逐頁截圖檢查`），並將 `outline.md` 與 `slide-spec.md` 保留於 `slides/` 作為可編輯中繼檔。
