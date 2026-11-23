---
title: "OS Ch 07 (Ch 6 Essentials): Virtual-Memory Management (9th Ed. 課程投影片)"
type: source
source_type: docs
raw_file: "raw/docs/OS-ch07.pdf"
source_url: ""
source_date: "2013-01-01"
ingested_at: "2026-11-23"
status: active
tags:
  - operating-systems
  - virtual-memory
  - demand-paging
  - page-replacement
  - thrashing
---

# OS Ch 07 (Ch 6 Essentials): Virtual-Memory Management (9th Ed. 課程投影片)

- **來源教材**：*Operating System Concepts Essentials – 9th Edition*（Silberschatz, Galvin & Gagne ©2013），投影片封面標示 Chapter 7（內頁目錄標示 Chapter 6: Virtual-Memory Management），共 66 頁。

## 核心結論（Key Takeaways）

1. **邏輯與實體記憶體完全解耦**：Virtual Memory 透過 Demand Paging（搭配 Lazy Swapper / Pager），僅在頁面實際被存取時才載入實體記憶體，使程式規模不再受限於實體 RAM 容量。
2. **極微小的 Page Fault Rate 即導致效能雪崩**：由於磁碟 Page Fault 服務時間（ms 級）比 RAM 存取（ns 級）慢數萬倍，即使每 1,000 次存取僅發生 1 次 Page Fault（$p = 0.001$），有效存取時間仍會暴跌 40 倍。
3. **Copy-on-Write 與 Page Replacement**：`fork()` 搭配 COW 僅在寫入時複製頁面以加速行程建立；頁面置換演算法中，FIFO 存在 **Belady's Anomaly**，而 OPT 與 LRU 屬 Stack Algorithms 不受此異常影響。
4. **Thrashing 防治與核心記憶體配置**：當所有行程的 Working-Set 總需求 $D > m$ 時會發生 Thrashing；Kernel Memory 則另採 **Buddy System**（2 的冪次切分與快速合併）或 **Slab Allocator**（無內部斷裂、快速物件配置）。

---

## 核心技術細節與公式

### 1. Demand Paging 與 Effective Access Time (EAT)
- **Valid-Invalid Bit**：`v` 代表在實體記憶體中，`i` 代表無效或尚在 Backing Store（觸發 Page Fault Trap，共 6 步驟完成換頁並重啟指令）。
- **有效存取時間公式**（Page Fault Rate $0 \le p \le 1$、Memory Access $= 200\text{ ns}$、Page-Fault Service Time $= 8\text{ ms} = 8,000,000\text{ ns}$）：
  $$\text{EAT} = (1 - p) \times 200 + p \times 8,000,000 = 200 + 7,999,800p$$
  - 若 $p = 0.001$（千分之一）：$\text{EAT} = 8,199.8\text{ ns} \approx 8.2\ \mu\text{s}$（**效能下降 40 倍**）。
  - 若要求效能衰退 $< 10\%$（$\text{EAT} < 220\text{ ns}$）：必須滿足 $p < 0.0000025$（每 400,000 次存取少於 1 次 Page Fault）。

### 2. Page Replacement 演算法比較（測試字串 `7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1`，3 Frames）
- **FIFO**：產生 **15 次 Page Faults**，且在特定字串下增加 Frame 數反而使 Page Fault 上升（**Belady's Anomaly**）。
- **Optimal (OPT)**：預知未來最久不會被使用的頁面進行置換，產生 **9 次 Page Faults**（理論下界基準）。
- **LRU（Least Recently Used）**：產生 **12 次 Page Faults**，可用 Counter 或 Doubly-Linked Stack 實作。
- **Second-Chance (Clock) / Enhanced Second-Chance**：利用硬體 Reference Bit 與 Modify (Dirty) Bit，依 `(0,0) → (0,1) → (1,0) → (1,1)` 優先序挑選犧牲頁，減少磁碟寫回 I/O。

### 3. Frame Allocation、Thrashing 與 Working-Set Model
- **Proportional Allocation**：依行程大小 $S_i$ 比例分配總共 $m$ 個可用 Frames（$S = \sum S_i$）：
  $$a_i = \frac{S_i}{S} \times m$$
- **Working-Set Model**：定義視窗 $\Delta$ 內參考的不同頁面數為 $WSS_i$，系統總需求 $D = \sum WSS_i$。若 $D > m$ 則發生 **Thrashing**（CPU 利用率驟降），須暫停或換出部分行程；亦可採用 Page-Fault Frequency (PFF) 上下界控制。
- **程式結構對 Page Fault 的影響**：以列為主（Row-major）儲存的 `int[128][128]` 陣列（每列佔 1 Page），Column-major 存取會產生 $128 \times 128 = 16,384$ 次 Page Faults，改為 Row-major 存取僅需 `128` 次。

## 相關頁面

- 核心概念：[[virtual-memory-and-paging]]
- 跨文比較：[[os-9thed-vs-10thed-evolution]]
- 延伸閱讀：[[Silberschatz2018-OS-10thEd]]、[[Silberschatz2013-OS-Ch06-Memory]]
