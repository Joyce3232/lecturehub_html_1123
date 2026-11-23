# Wiki Index

> 本檔案由 Agent 於每次 Ingest、Query 沉澱或 Lint 後自動更新，作為全站導覽與快速檢索入口。

## Comparisons（跨文比較與綜合分析）
- [[os-9thed-vs-10thed-evolution|OS 9th Ed. (2013) vs. 10th Ed. (2018) 教材演進與差異比較]] — 盤點 Segmentation 淘汰、Page Swapping、NVM Scheduling 與 Containers 導入。
- [[single-node-os-vs-wsc-storage-and-scheduling|單機作業系統（Silberschatz）vs. 超大規模資料中心（WSC）架構對比]] — 比較單機 RAID/排程與 WSC Diskless、Colossus、Borg 的典範轉移。
- [[array-vs-linked-list-and-stack|Array vs. Linked List & Stack ADT 實作選擇比較]] — 比較隨機存取／Binary Search、動態增刪、Stack 雙實作與 OS 記憶體局部性。

## Concepts（核心概念）
- [[warehouse-scale-computers|Warehouse-Scale Computers (WSC)]] — 將整座資料中心視為單一計算實體的系統架構、故障率與自動化原則。
- [[scale-up-vs-scale-out|Scale-Up vs. Scale-Out]] — 跨節點延遲模型、超過 2,000 核心後的效能收斂與 Brawny/Wimpy Cores 權衡。
- [[tail-latency|Tail Latency 與 Hedged Requests]] — 大規模扇出查詢的長尾延遲放大效應（$63\%$ 案例推導）與緩解策略。
- [[software-defined-infrastructure|Software-Defined Infrastructure (SDI)]] — SDS、SDN、Software-Defined Storage 與動態電力封頂（Thunderbolt / Autopilot）。
- [[power-usage-effectiveness|PUE、TPUE 與 WUE 能源效率指標]] — 設施與伺服器能效公式、Power Oversubscription 容量增益與永續碳水指標。
- [[virtual-memory-and-paging|Virtual Memory, Paging & TLB]] — Paging 消除外部斷裂、TLB/VM 雙層 EAT 公式、Page Replacement 與 Thrashing 防治。
- [[mass-storage-and-raid|Mass Storage, Disk Scheduling & RAID]] — HDD 存取延遲、SSTF/SCAN/C-SCAN 排程、RAID 0–6、MTTDL 與 ZFS Checksum。
- [[process-synchronization-and-deadlocks|Process Synchronization & Deadlocks]] — Critical-Section 三條件、Peterson/Atomic/Mutex/Semaphore/Monitor 與 Banker's Algorithm。
- [[linked-lists|Linked Lists（鏈結串列結構與演算法）]] — 雙指標 `pPre`/`pLoc` 統一增刪邏輯、Circularly、Doubly 與 Multilinked Lists。
- [[stacks-and-backtracking|Stacks & Backtracking（堆疊、運算式轉換與回溯法）]] — LIFO ADT、Data Hiding、Infix 轉 Postfix 與迷宮／八皇后回溯。

## Entities（模型、機構與工具實體）
- [[borg|Borg]] — Google WSC 叢集排程與資源管理系統（Kubernetes 前身）。
- [[colossus|Colossus]] — Google 統一分散式檔案系統與 Client-side 糾刪碼儲存層。
- [[spanner|Spanner]] — 基於 TrueTime 的全球分散式外部強一致性資料庫（99.999% SLO）。
- [[tensor-processing-unit|Tensor Processing Unit (TPU)]] — Google 深度學習專用 ASIC、MXU 脈動陣列、3D Torus ICI 與 OCS 光學交換架構。

## Sources（原始資料摘要）

### Docs（論文、簡報、報告：`raw/docs/`）
- [[Barroso2026-WSC-4thEd|The Data Center as a Computer (4th Edition, 2026)]] — Barroso、Hölzle、Ranganathan 合著的 WSC 權威專書第四版（12 章完整技術摘要與核心公式）。
- [[Silberschatz2018-OS-10thEd|Operating System Concepts (10th Edition, 2018)]] — Silberschatz 等人合著作業系統經典教科書第十版（21 章完整架構、NVM/Cloud 與 Kubernetes 更新）。
- [[Silberschatz2013-OS-Ch06-Memory|OS Ch 06: Memory-Management Strategies (9th Ed. 投影片)]] — Contiguous Allocation、50-Percent Rule、Segmentation、Paging 與 TLB EAT（含課堂筆記）。
- [[Silberschatz2013-OS-Ch07-VirtualMemory|OS Ch 07: Virtual-Memory Management (9th Ed. 投影片)]] — Demand Paging、COW、FIFO/OPT/LRU、Belady's Anomaly、Working-Set 與 Slab/Buddy。
- [[Silberschatz2013-OS-Ch08-MassStorage|OS Ch 08 (Ch 12): Mass-Storage Systems (9th Ed. 投影片)]] — HDD 效能公式、Disk Scheduling (FCFS/SSTF/SCAN/C-SCAN/C-LOOK)、RAID 與 ZFS。
- [[Sue-DS-Ch03-LinkedLists|DS Ch 03: Linked Lists (資結課程投影片)]] — Linear List 分類、Singly/Circularly/Doubly/Multilinked Lists 與 26 個核心演算法（含課堂筆記）。
- [[Sue-DS-Ch04-Stacks|DS Ch 04: Stacks (資結課程投影片)]] — LIFO 操作、Linked List/Array 雙實作、括號剖析、Infix-to-Postfix 與回溯法（含課堂筆記）。

### Web（網頁剪藏：`raw/web/`）
- *尚無條目*

### Notes（個人筆記與逐字稿：`raw/notes/`）
- *尚無條目*

### Data（數據表格與程式碼：`raw/data/`）
- *尚無條目*
