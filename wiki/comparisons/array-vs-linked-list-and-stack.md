---
title: "Array vs. Linked List & Stack ADT 實作選擇比較"
type: comparison
source_type: mixed
raw_file:
  - "raw/docs/DS_Ch3.pdf"
  - "raw/docs/DS_Ch4.pdf"
  - "raw/docs/OS-ch06.pdf"
  - "raw/docs/OS-ch07.pdf"
source_url: ""
source_date: "2026-11-23"
ingested_at: "2026-11-23"
status: active
tags:
  - data-structures
  - array
  - linked-list
  - stack
  - memory-locality
---

# Array vs. Linked List & Stack ADT 實作選擇比較

本比較頁整合 [[Sue-DS-Ch03-LinkedLists]] 與 [[Sue-DS-Ch04-Stacks]] 對線性串列與堆疊底層結構的權衡，並連結至作業系統記憶體局部性（[[virtual-memory-and-paging]]）的底層視角。

## 核心結論（Key Takeaways）

1. **存取模式決定底層結構**：需要頻繁依索引隨機讀取或 Binary Search 時選 **Array**；需要頻繁在中間動態插入與刪除、且總量未知時選 **Linked List**。
2. **Stack 實作的空間與速度權衡**：Linked List 版 Stack 無預設容量限制且不浪費未用陣列空間，但每筆資料須多存一個 `next` 指標；若最大深度可預估，**Array 版 Stack 省去指標與動態 `allocate/recycle` 開銷，實務效能更佳**。
3. **跨領域連結（記憶體局部性）**：Array 採實體連續配置，天生具備極佳的 **Spatial Locality**（減少 TLB Miss 與 Page Fault，參見 [[virtual-memory-and-paging]]）；Linked List 的指標跳躍（Pointer Chasing）則較容易跨越多個 Page。

---

## 一、Array vs. Linked List（General List 層級）

| 比較維度 | Array（陣列） | Singly Linked List | Doubly Linked List |
| :--- | :--- | :--- | :--- |
| **記憶體配置** | 連續配置（Contiguous） | 動態非連續配置（`allocate`） | 動態非連續配置（`allocate`） |
| **隨機存取（Retrieval by Index）** | $O(1)$ 直接定址 | $O(n)$ 循序走訪 | $O(n)$ 循序走訪 |
| **搜尋（Ordered List）** | 支援 **Binary Search** $O(\log n)$ | 僅能 **Sequential Search** $O(n)$ | 僅能 **Sequential Search** $O(n)$ |
| **插入／刪除（已知位置）** | $O(n)$（須大量搬移後續元素） | $O(1)$ 改指標（須先知 `pPre`） | $O(1)$ 改雙向指標（免先查 `pPre`） |
| **額外空間開銷** | 預留未使用槽位（可能內部浪費） | 每節點多 1 個 `link` 指標 | 每節點多 `back` + `fore` 2 個指標 |
| **OS 記憶體局部性** | 連續位址，Spatial Locality 極佳 | 節點分散，易跨 Page | 節點分散且每筆體積較大 |

---

## 二、Stack ADT：Linked List 實作 vs. Array 實作

| 比較維度 | Linked List 實作（[[Sue-DS-Ch04-Stacks]] Ch 4-2） | Array 實作（[[Sue-DS-Ch04-Stacks]] Ch 4-5） |
| :--- | :--- | :--- |
| **Head Metadata** | `count`、`top`（`<node pointer>`） | `stackAry`、`count`、`stackMax`、`top`（`<index>`） |
| **容量彈性** | 動態成長，僅受限於系統可用動態記憶體 | 固定上限 `stackMax`，超出即 Overflow |
| **Push / Pop 成本** | $O(1)$，但每次需呼叫 `allocate` / `recycle` | $O(1)$，僅陣列索引加減與寫入，無配置開銷 |
| **適用場景** | 資料量變動劇烈、無法預估最大深度 | 最大深度可預先估算、追求極致執行效率 |

## 相關頁面

- 來源：[[Sue-DS-Ch03-LinkedLists]]、[[Sue-DS-Ch04-Stacks]]
- 關聯概念：[[linked-lists]]、[[stacks-and-backtracking]]、[[virtual-memory-and-paging]]
