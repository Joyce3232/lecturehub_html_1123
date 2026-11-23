---
title: "Linked Lists（鏈結串列結構與演算法）"
type: concept
source_type: mixed
raw_file:
  - "raw/docs/DS_Ch3.pdf"
source_url: ""
source_date: "2026-11-23"
ingested_at: "2026-11-23"
status: active
tags:
  - data-structures
  - linked-list
  - pointers
  - algorithms
---

# Linked Lists（鏈結串列結構與演算法）

## 核心結論（Key Takeaways）

1. **非連續配置的動態彈性**：Linked List 透過 Self-referential Structure 將資料節點與指標（`link`）綁在一起，不需實體連續記憶體，因此插入與刪除只需 $O(1)$ 指標改向，免去 Array 搬移元素的成本（[[Sue-DS-Ch03-LinkedLists]]）。
2. **雙指標（`pPre`, `pLoc`）統一所有邊界**：Ordered Search 同時回傳目標位置 `pLoc` 與邏輯前驅 `pPre`，讓「空串列／首節點／中間／尾節點」四種插入或刪除情境收斂為 `pPre == null` 與 `pPre != null` 兩支邏輯。
3. **指標接線順序是正確性關鍵**：插入節點必先接後繼（`pNew->link = pPre->link`）再改前驅（`pPre->link = pNew`）；在 Circularly Linked List 搜尋時則須比對 `startAddress` 避免無限繞圈。
4. **變體結構各司其職**：Doubly Linked List 以額外 `back` 指標換取雙向走訪與 $O(1)$ 已知節點刪除；Multilinked List 則以多組指標實現「單份資料、多重排序視角」。

---

## 結構演化與演算法核心

| 結構類型 | 節點指標欄位 | Head Metadata | 核心優勢 | 注意事項 / 限制 |
| :--- | :--- | :--- | :--- | :--- |
| **Singly Linked List** | `link`（指向後繼） | `count`, `head`, (`pos`, `rear`) | 結構精簡、插入刪除免搬移資料 | 無法反向走訪、不可 Binary Search |
| **Circularly Linked List** | `link`（尾指回首） | `count`, `pos`, `rear`, `head` | 可從串列中間出發輪詢所有節點 | 增刪尾節點須更新 `rear`；搜尋須防無窮迴圈 |
| **Doubly Linked List** | `back`（前驅）+ `fore`（後繼） | `count`, `head`, `rear` | 雙向走訪、已知 `pDlt` 即可直接刪除 | 每筆節點多 1 指標空間、增刪需維護雙向指標 |
| **Multilinked List** | 多組獨立 `link`（如 `pres`, `spouse`） | 多組 `head` / `rear` | 一份資料支援多種排序鏈結、免重複儲存 | `allocate` 與 `count` 仍只執行一次 |

## 相關頁面

- 來源：[[Sue-DS-Ch03-LinkedLists]]
- 關聯概念：[[stacks-and-backtracking]]
- 跨文比較：[[array-vs-linked-list-and-stack]]
