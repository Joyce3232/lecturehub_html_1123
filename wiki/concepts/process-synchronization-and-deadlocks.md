---
title: "Process Synchronization & Deadlocks"
type: concept
source_type: mixed
raw_file:
  - "raw/docs/Abraham-Silberschatz-Operating-System-Concepts-10th-2018.pdf"
source_url: ""
source_date: "2018-01-01"
ingested_at: "2026-11-23"
status: active
tags:
  - synchronization
  - deadlock
  - concurrency
  - operating-systems
---

# Process Synchronization & Deadlocks

## 核心結論（Key Takeaways）

1. **Critical-Section Problem 三大條件**：任何正確的同步解法必須同時滿足 **Mutual Exclusion**（互斥）、**Progress**（無行程在區內時不得無限延遲進入）與 **Bounded Waiting**（避免 Starvation）。
2. **同步原語的抽象演進**：從軟體解（Peterson's Solution）與硬體原子指令（`test_and_set`、`compare_and_swap`），演進至 OS 層級的 Mutex Locks、Semaphores 與高階語言支援的 Monitors / Transactional Memory。
3. **Deadlock 四大必要條件與對策**：必須同時成立 Mutual Exclusion、Hold and Wait、No Preemption 與 Circular Wait；OS 可採預防（破壞任一條件）、避免（Banker's Algorithm 確保 Safe State）或偵測後復原。

## 關鍵演算法概念（依據 [[Silberschatz2018-OS-10thEd]] Ch 6–8）

- **經典同步問題**：Bounded-Buffer Problem（生產者-消費者）、Readers-Writers Problem、Dining-Philosophers Problem。
- **Safe State 與 Banker's Algorithm**：系統存在至少一個 Safe Sequence $\langle P_1, P_2, \dots, P_n \rangle$，使每個 $P_i$ 的資源需求 $\text{Need}_i$ 皆可由當前可用資源 $\text{Available}$ 加上前面已完成行程釋放的資源 $\sum_{j<i}\text{Allocation}_j$ 滿足。

## 相關頁面

- 來源：[[Silberschatz2018-OS-10thEd]]
