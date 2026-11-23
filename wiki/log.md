# Wiki Log

> Append-only 增量操作紀錄。每筆紀錄須以 `## [YYYY-MM-DD] <ingest|query|lint|init> | <標題>` 開頭，方便以 `grep "^## \[" wiki/log.md` 檢索。

## [2026-11-22] init | 建立跨文 LLM Wiki 知識庫架構與 AGENTS.md
- 建立 `raw/`（`docs/`、`web/`、`notes/`、`data/`）與 `wiki/`（`sources/`、`concepts/`、`entities/`、`comparisons/`）分軌目錄結構。
- 確立 `AGENTS.md` 核心規範：繁體中文（台灣習慣用語）+ 英文專業術語、標準 LaTeX 公式保留、Dataview YAML frontmatter、全自動 Batch Ingest，以及 `assets/` 簡報專用排除邊界。

## [2026-11-22] ingest | Barroso2026-WSC-4thEd
- **來源**：對話附件《The Data Center as a Computer: Designing Warehouse-Scale Machines (4th Edition, 2026)》（建議將原檔存入 `raw/docs/Barroso2026-WSC-4thEd.pdf`）。
- **新增頁面**：`wiki/sources/docs/Barroso2026-WSC-4thEd.md`；概念頁 `warehouse-scale-computers.md`、`scale-up-vs-scale-out.md`、`tail-latency.md`、`software-defined-infrastructure.md`、`power-usage-effectiveness.md`；實體頁 `borg.md`、`colossus.md`、`spanner.md`、`tensor-processing-unit.md`。
- **更新頁面**：`wiki/index.md`、`wiki/log.md`。

## [2026-11-23] ingest | Batch Ingest: Silberschatz OS 10th Ed. + OS-ch06/07/08
- **來源**：`Abraham-Silberschatz-Operating-System-Concepts-10th-2018.pdf`、`OS-ch06.pdf`、`OS-ch07.pdf`、`OS-ch08.pdf`（後三者為 9th Edition ©2013 課程投影片）。
- **新增頁面**：`Silberschatz2018-OS-10thEd.md`、`Silberschatz2013-OS-Ch06-Memory.md`、`Silberschatz2013-OS-Ch07-VirtualMemory.md`、`Silberschatz2013-OS-Ch08-MassStorage.md`；概念頁 `virtual-memory-and-paging.md`、`mass-storage-and-raid.md`、`process-synchronization-and-deadlocks.md`；比較頁 `os-9thed-vs-10thed-evolution.md`、`single-node-os-vs-wsc-storage-and-scheduling.md`。
- **更新頁面**：`Barroso2026-WSC-4thEd.md`（修正 `raw_file` 檔名）、`wiki/index.md`、`wiki/log.md`。
- **偵測衝突**：2 項（9th Ed. Segmentation vs. 10th Ed. 淘汰 Segmentation；單機 HDD 排程/RAID vs. WSC Diskless + Colossus 糾刪碼）。

## [2026-11-23] ingest | Batch Ingest: DS Ch3 (Linked Lists) & DS Ch4 (Stacks)
- **來源**：`raw/docs/DS_Ch3.pdf`（58 頁投影片）、`raw/docs/DS_Ch4.pdf`（42 頁投影片，授課教師：Kuen-Liang Sue，IM/NCU）。
- **新增頁面**：`wiki/sources/docs/Sue-DS-Ch03-LinkedLists.md`、`wiki/sources/docs/Sue-DS-Ch04-Stacks.md`；概念頁 `wiki/concepts/linked-lists.md`、`wiki/concepts/stacks-and-backtracking.md`；比較頁 `wiki/comparisons/array-vs-linked-list-and-stack.md`。
- **更新頁面**：`wiki/index.md`、`wiki/log.md`。
- **偵測衝突**：無（補充課堂手寫修正：Algorithm 3-22 Doubly Linked List Insert 第 4.9 行應調至 4.4.3 行，且第 4.6 行條件應為 `pSucc null`）。
