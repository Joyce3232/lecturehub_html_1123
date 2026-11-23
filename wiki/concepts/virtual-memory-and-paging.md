---
title: "Virtual Memory, Paging & TLB"
type: concept
source_type: mixed
raw_file:
  - "raw/docs/OS-ch06.pdf"
  - "raw/docs/OS-ch07.pdf"
  - "raw/docs/Abraham-Silberschatz-Operating-System-Concepts-10th-2018.pdf"
source_url: ""
source_date: "2018-01-01"
ingested_at: "2026-11-23"
status: active
tags:
  - virtual-memory
  - paging
  - tlb
  - page-replacement
  - thrashing
---

# Virtual Memory, Paging & TLB

## 核心結論（Key Takeaways）

1. **Paging 消除外部斷裂**：將實體記憶體切分為固定大小 Frames、邏輯記憶體切分為相同大小 Pages，徹底解決 Contiguous Allocation 的 External Fragmentation（50-Percent Rule 約浪費 $1/3$ 空間）。
2. **雙層 Effective Access Time (EAT) 主導效能**：記憶體階層效能同時受 **TLB 命中率 $\alpha$** 與 **Page Fault Rate $p$** 影響；即使 $p = 0.001$ 也會讓存取延遲暴跌 40 倍。
3. **Working-Set 與核心配置器**：透過 Working-Set Model（$D = \sum WSS_i$）與 PFF 防止 Thrashing；OS 核心則依賴 Buddy System 與 Slab Allocator 管理連續與高頻物件記憶體。

## 核心公式彙整

1. **TLB 有效存取時間**（[[Silberschatz2013-OS-Ch06-Memory]]）：
   $$\text{EAT}_{\text{TLB}} = (m + \epsilon)\alpha + (2m + \epsilon)(1 - \alpha)$$
2. **Demand Paging 有效存取時間**（[[Silberschatz2013-OS-Ch07-VirtualMemory]]）：
   $$\text{EAT}_{\text{VM}} = (1 - p) \times m + p \times (\text{Page Fault Service Time})$$
3. **比例頁框配置**（[[Silberschatz2013-OS-Ch07-VirtualMemory]]）：
   $$a_i = \frac{S_i}{\sum S_j} \times m$$

## 相關頁面

- 來源：[[Silberschatz2013-OS-Ch06-Memory]]、[[Silberschatz2013-OS-Ch07-VirtualMemory]]、[[Silberschatz2018-OS-10thEd]]
- 跨文比較：[[os-9thed-vs-10thed-evolution]]
