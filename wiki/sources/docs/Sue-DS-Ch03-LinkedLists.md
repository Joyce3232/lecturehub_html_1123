---
title: "DS Ch 03: Linked Lists (資結課程投影片)"
type: source
source_type: docs
raw_file: "raw/docs/DS_Ch3.pdf"
source_url: ""
source_date: "2026-11-23"
ingested_at: "2026-11-23"
status: active
tags:
  - data-structures
  - linked-list
  - doubly-linked-list
  - circular-linked-list
  - algorithms
---

# DS Ch 03: Linked Lists (資結課程投影片)

- **來源教材**：Data Structures Chapter 3: *Linked Lists*（授課教師：Kuen-Liang Sue，IM/NCU），共 58 頁投影片（115 張投影片節次，含課堂手寫筆記與演算法偽碼）。

## 核心結論（Key Takeaways）

1. **Array 與 Linked List 的核心權衡**：Array 支援隨機存取與 Binary Search，但插入/刪除須搬移大量元素；Linked List 節點實體不連續（透過指標串聯），插入/刪除只需改指標，但**無法使用 Binary Search**（僅能循序搜尋 $O(n)$）。
2. **四種插入與刪除情境皆可化簡為「兩大類」**：無論是插入（空串列、最前、中間、最後）或刪除（唯一節點、首節點、中間、尾節點），只要先透過 `searchList` 取得前驅指標 `pPre` 與目標指標 `pLoc`，即可簡化為「`pPre == null`（處理 `list.head`）」與「`pPre != null`（一般操作）」兩支邏輯。
3. **指標賦值順序不可顛倒**：插入節點時必須先執行 `pNew->link = pPre->link`（或 `list.head`），再執行 `pPre->link = pNew`（或 `list.head = pNew`），否則會直接遺失後續鏈結。
4. **進階鏈結結構擴充應用**：Circularly Linked List 讓尾端接回首節點（搜尋須記錄 `startAddress` 防無窮迴圈）；Doubly Linked List 具 `back` / `fore` 雙向指標；Multilinked List 則讓同一份實體資料擁有多條邏輯排序鏈結（如同時依總統與配偶排序），節省資料重複儲存。

---

## 核心技術細節與演算法

### 1. Linear List 分類與基本操作
- **General List**：可在任意位置插入與刪除，分為 **Unordered (Random) List** 與 **Ordered List**（依 `key` 排序）。
- **Restricted List**：僅能在端點增刪，包含 **FIFO (Queue)** 與 **LIFO (Stack)**（見 [[Sue-DS-Ch04-Stacks]]）。
- **四大操作**：Insertion、Deletion、Retrieval（讀取不破壞內容；Restricted List 例外）、List Traversal（僅適用於 General List）。

### 2. Linked List 資料結構（Self-Referential Structure）
- **Head Structure（Metadata）**：儲存 `count`（節點數）、`head`（首節點指標），實務可擴充 `pos`（走訪目前位置指標）與 `rear`（尾節點指標，加速 Ordered Search 與尾端操作）。
- **Data Node Structure**：包含 `data`（含搜尋鍵 `key` 與多欄位資料）及 `link`（指向下一個同型別節點的指標）。

### 3. 核心演算法與偽碼邏輯
1. **Create List（Algorithm 3-1）**：初始化 `list.head = null`、`list.count = 0`。
2. **Insert Node（Algorithm 3-2）**：
   - 先 `allocate(pNew)`，若記憶體不足則回傳 `false`（Overflow）。
   - `if (pPre null)`：`pNew->link = list.head; list.head = pNew`（涵蓋空串列與最前端插入）。
   - `else`：`pNew->link = pPre->link; pPre->link = pNew`（涵蓋中間與尾端插入）。
   - 最後 `list.count = list.count + 1`。
3. **Delete Node（Algorithm 3-3）**：
   - 先保存 `dataOut = pLoc->data`。
   - `if (pPre null)`：`list.head = pLoc->link`；`else`：`pPre->link = pLoc->link`。
   - 統一在條件外執行 `list.count = list.count - 1` 與 `recycle(pLoc)`。
4. **Ordered Search List（Algorithm 3-4）**：
   ```text
   pPre = null
   pLoc = list.head
   loop (pLoc not null AND target > pLoc->data.key)
       pPre = pLoc
       pLoc = pLoc->link
   end loop
   ```
   - 找到時回傳 `true`（`pLoc` 指向目標，`pPre` 指向前驅）；找不到時回傳 `false`，此時 `(pPre, pLoc)` 剛好標定**應插入的邏輯位置**（如 `target < first` 時 `pPre = null`、`target > last` 時 `pLoc = null`）。
5. **輔助與整合模組**：`retrieveNode`（3-5）、`emptyList`（3-6）、`fullList`（3-7，試探性 `allocate` 再 `recycle`）、`listCount`（3-8）、`getNext`（3-9，利用 `fromWhere` 旗標與 `list.pos` 支援外部迴圈走訪）、`destroyList`（3-10，逐筆 `recycle` 並重置 `list.pos = null`），以及整合選單程式 `buildLinkedList`（3-11～3-15）。

### 4. 串接應用與複雜鏈結結構
- **Append Two Lists（Algorithm 3-18）**：若 `list1.count == 0`，令 `list1.head = list2.head`；否則走訪至 `list1` 最後一節點（`pLoc->link == null`），接上 `pLoc->link = list2.head` 並累加 `list1.count += list2.count`。
- **Array of Lists（Algorithm 3-19～3-21）**：以一維陣列存放多個 Head Structure，代表二維稀疏陣列的每一列。
- **Circularly Linked List**：尾節點指向首節點，插入/刪除尾節點須同步更新 `rear` 與尾節點 `link`；自中間搜尋時須檢查 `pLoc->link != startAddress` 以避免目標不存在時無限繞圈。
- **Doubly Linked List（Algorithm 3-22 / 3-23）**：
  - 每個節點有 `back`（前驅）與 `fore`（後繼），Head 含 `count`、`head`、`rear`。
  - **投影片課堂修正（Algorithm 3-22）**：原偽碼第 4.9 行 `pPre->fore = pNew` 應調至第 4.4.3 行，且第 4.6 行判斷尾端插入條件應為 `if (pSucc null)`。
  - **刪除節點（`deleteDbl`）**：同時處理 `pDlt->back`（更新前驅 `fore` 或 `list.head`）與 `pDlt->fore`（更新後繼 `back` 或 `list.rear`），最後 `recycle(pDlt)`。
- **Multilinked Lists（Algorithm 3-26）**：單一實體節點僅 `allocate` 一次、計數一次，但內含多組指標欄位（例如 `President link` 與 `Spouse link`），可支援多鍵值排序走訪而不複製資料。

## 相關頁面

- 核心概念：[[linked-lists]]、[[stacks-and-backtracking]]
- 跨文比較：[[array-vs-linked-list-and-stack]]
- 延伸閱讀：[[Sue-DS-Ch04-Stacks]]
