---
title: "OS Ch 06: Memory-Management Strategies (9th Ed. 課程投影片)"
type: source
source_type: docs
raw_file: "raw/docs/OS-ch06.pdf"
source_url: ""
source_date: "2013-01-01"
ingested_at: "2026-11-23"
status: active
tags:
  - operating-systems
  - memory-management
  - paging
  - segmentation
  - tlb
---

# OS Ch 06: Memory-Management Strategies (9th Ed. 課程投影片)

- **來源教材**：*Operating System Concepts – 9th Edition*（Silberschatz, Galvin & Gagne ©2013），共 60 頁投影片（含課堂手寫筆記）。

## 核心結論（Key Takeaways）

1. **位址綁定決定重定位彈性**：Address Binding 可發生於 Compile Time、Load Time 或 Execution Time；現代 OS 採 Execution-Time Binding，搭配 MMU 的 Relocation Register 與 Limit Register 動態保護記憶體。
2. **動態配置與 50-Percent Rule**：在 Contiguous Allocation 中，First-Fit 與 Best-Fit 優於 Worst-Fit；First-Fit 分析顯示每配置 $N$ 個區塊會產生 $0.5N$ 個不可用碎片（約 $1/3$ 記憶體因 External Fragmentation 浪費）。
3. **Segmentation vs. Paging**：Segmentation 貼合程式邏輯視角（Segment Table 含 `base`、`limit`），但仍存在 External Fragmentation；Paging 將實體切為固定 Frames、邏輯切為 Pages，徹底消除外部斷裂（僅留平均 $\frac{1}{2}$ Page 的 Internal Fragmentation）。
4. **TLB 大幅壓低雙倍記憶體存取開銷**：沒有 TLB 時每次存取需 2 次記憶體讀取（Page Table + Data）；導入高命中率 TLB（$\alpha = 99\%$）可將有效存取時間壓低至接近單次存取。

---

## 核心技術細節與公式

### 1. 記憶體保護與位址綁定
- **Base & Limit Registers**：CPU 存取位址必須滿足：
  $$\text{base} \le \text{address} < \text{base} + \text{limit}$$
  否則觸發 Addressing Error Trap 至作業系統。
- **Swapping 成本範例**：100 MB Process 透過 50 MB/s 硬碟進行 Swap out（2,000 ms）與 Swap in（2,000 ms），單次 Context Switch 的 Swapping 開銷高達 `4,000 ms`（4 秒）。

### 2. Contiguous Allocation 與斷裂計算
- **50-Percent Rule（First-Fit 碎片率）**：
  $$\text{Unusable Memory Ratio} = \frac{0.5N}{N + 0.5N} = \frac{1}{3}$$
- **External vs. Internal Fragmentation**：
  - External Fragmentation：總可用空間足夠但不連續，需仰賴 Dynamic Relocation + Compaction 解決。
  - Internal Fragmentation：配置區塊大於實際需求（例如 Page Size $= 2,048\text{ B}$，Process $= 72,766\text{ B} = 35\text{ pages} + 1,086\text{ B}$，最後一頁浪費 $2,048 - 1,086 = 962\text{ B}$）。

### 3. Paging 與 TLB Effective Access Time (EAT)
- **位址切分**：邏輯位址空間 $2^m$、Page Size $2^n$，則高 $m-n$ bits 為 Page Number $p$，低 $n$ bits 為 Page Offset $d$。
- **TLB 有效存取時間公式**（TLB 搜尋時間 $\epsilon$、記憶體存取時間 $m$、命中率 $\alpha$）：
  $$\text{EAT} = (m + \epsilon)\alpha + (2m + \epsilon)(1 - \alpha)$$
  - 若 $m = 100\text{ ns}$、$\epsilon = 20\text{ ns}$：當 $\alpha = 80\%$ 時 $\text{EAT} = 140\text{ ns}$；當 $\alpha = 99\%$ 時 $\text{EAT} = 121\text{ ns}$。
- **Shared Pages**：唯讀可重入程式碼（Reentrant Code）可跨行程共享同一份實體 Frame。

### 4. 大型 Page Table 結構（>32-bit 位址空間）
- **Hierarchical Paging**：2-Level / 3-Level Paging（如 64-bit 位址以 4 KB Page 需多層切分，否則單表達 $2^{52}$ 項目）。
- **Hashed Page Tables**：適用於稀疏 64-bit 位址空間（或 Clustered Page Tables）。
- **Inverted Page Table**：全系統僅維護一張表（每個實體 Frame 一筆 `<pid, p>` 紀錄），大幅節省記憶體但需搭配 Hash Table 與 TLB 加速查詢。

## 相關頁面

- 核心概念：[[virtual-memory-and-paging]]
- 跨文比較：[[os-9thed-vs-10thed-evolution]]（第十版已移除 Segmentation）
- 延伸閱讀：[[Silberschatz2018-OS-10thEd]]、[[Silberschatz2013-OS-Ch07-VirtualMemory]]
