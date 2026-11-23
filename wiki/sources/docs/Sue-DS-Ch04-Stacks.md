---
title: "DS Ch 04: Stacks (資結課程投影片)"
type: source
source_type: docs
raw_file: "raw/docs/DS_Ch4.pdf"
source_url: ""
source_date: "2026-11-23"
ingested_at: "2026-11-23"
status: active
tags:
  - data-structures
  - stack
  - lifo
  - infix-postfix
  - backtracking
---

# DS Ch 04: Stacks (資結課程投影片)

- **來源教材**：Data Structures Chapter 4: *Stacks*（授課教師：Kuen-Liang Sue，IM/NCU），共 42 頁投影片（84 張投影片節次，含課堂手寫筆記與演算法偽碼）。

## 核心結論（Key Takeaways）

1. **LIFO 受限線性串列**：Stack 僅允許在頂端（`Top`）進行 Push（推入）、Pop（彈出並刪除）與 Stack Top（讀取但不刪除）；誤對空堆疊執行 Pop 或 Top 會觸發 **Underflow**，空間不足時 Push 則觸發 **Overflow**。
2. **ADT 雙軌實作選擇**：Linked List 實作透過 `head (count, top)` 與動態節點配置，大小彈性無固定上限；Array 實作改用索引 `top` 與 `stackMax`，**當最大容量可預先計算時，Array 實作效能更佳且不需 `next` 指標空間**。
3. **運算式處理的核心工具**：Stack 能消除中序（Infix）對括號的依賴，依運算子優先權（`*,/` 權重 2、`+,-` 權重 1、`(` 棧內權重 0）將 Infix 轉為 Postfix（Algorithm 4-12），並以 Postfix 求值（Algorithm 4-13，注意 `operand2` 先 Pop、`operand1` 後 Pop）。
4. **回溯法（Backtracking）記憶分支點**：在迷宮尋路（Goal Seeking）與八皇后問題（Eight Queens）中，Stack 用來記錄每個決策分支點（Branch Point），走入死胡同時即可 Pop 退回上一步改選其他路徑。

---

## 核心技術細節與演算法

### 1. Stack 基本操作與 Linked List 實作
- **三大核心操作**：`Push`、`Pop`、`Stack Top`（僅複製頂端資料不刪除）。
- **八大 ADT 標準介面（Algorithm 4-1～4-8）**：
  1. `createStack`：初始化 `stack.count = 0`、`stack.top = null`。
  2. `pushStack`：若 `stack full` 回傳 `false`；否則 `allocate(newPtr)`、`newPtr->data = data`、`newPtr->next = stack.top`、`stack.top = newPtr`、`stack.count += 1`。
  3. `popStack`：若 `stack empty` 回傳 `false`；否則 `dltPtr = stack.top`、`dataOut = stack.top->data`、`stack.top = stack.top->next`、`stack.count -= 1`、`recycle(dltPtr)`。
  4. `stackTop`：檢查非空後回傳 `stack.top->data`（不修改 `stack.top`）。
  5. `emptyStack` / `fullStack` / `stackCount`：落實 **Data Hiding（資料隱藏）** 原則，避免呼叫端直接存取 `stack` 內部欄位。
  6. `destroyStack`：迴圈將所有節點 `recycle` 並將 `stack.count` 歸零。

### 2. Stack 四大類典型應用
1. **資料反轉（Reversing Data）**：
   - `reverseNumber`（Algorithm 4-9）：依序讀入整數 Push 進 Stack，再依序 Pop 印出達成反序。
   - `decimalToBinary`（Algorithm 4-10）：十進位轉二進位時，連續除以 2 取餘數（$number \bmod 2$）會先產生低位元；先 Push 進 Stack 再依序 Pop 即可正確由高位元印出（如 $26_{10} = 11010_2$）。
2. **語法剖析（Parsing — Algorithm 4-11 `parseParens`）**：
   - 遇到左括號 `(` 時 Push；遇到右括號 `)` 時若 Stack 為空代表「多出右括號 / 缺左括號」，否則 Pop 配對；迴圈結束後若 Stack 仍非空，代表「左括號未閉合」。
3. **延遲使用：Infix 轉 Postfix 與求值（Algorithm 4-12 & 4-13）**：
   - **三種表示法**：Prefix（`+ a b`）、Infix（`a + b`，需括號決定順序）、Postfix（`a b +`，無須括號且單一求值規則）。
   - **Infix → Postfix 優先權規則**（`priority(*, /) = 2`、`priority(+, -) = 1`、`priority('(') = 0`）：
     - 運算元（Operand）：直接輸出至 `postFix`。
     - 左括號 `(`：無條件 Push 進 Stack。
     - 右括號 `)`：持續 Pop 並輸出，直到遇到對應的 `(`（將 `(` 丟棄）。
     - 運算子：當 `!emptyStack(stack) AND priority(token) <= priority(topToken)` 時持續 Pop 輸出，最後再 Push `token`。
     - 掃描完畢後，將 Stack 剩餘運算子全數 Pop 輸出。
   - **Postfix 求值（Algorithm 4-13）**：遇運算元則 Push 其**數值**；遇運算子則依序 Pop 出 `operand2`（右運算元）與 `operand1`（左運算元），計算 `calculate(operand1, operator, operand2)` 後 Push 回 Stack，最後 Pop 出唯一結果。
4. **回溯法（Backtracking — Algorithm 4-14 & 4-15）**：
   - **Goal Seeking（迷宮／圖形尋路）**：經過分支點（Branch Point）時將候選分支 Push 進 Stack；遇到死路（End）時不斷 Pop 退回最近的分支點改走下一分支，直到抵達 `goal`。
   - **Eight Queens Problem（八皇后 / 四皇后問題）**：逐列嘗試放置皇后，若該列所有欄位皆被防守（Guarded），則 Pop 退回上一列皇后位置並將 `col` 遞增嘗試下一格。

### 3. Stack ADT 的 Array 實作（Algorithm 4-16）
- **資料結構定義**：`stackAry`（指向資料陣列的指標）、`count`（目前數量）、`stackMax`（最大容量）、`top`（整數索引而非指標，省去節點 `next` 欄位）。
- **適用時機**：若程式執行前即可估算 Stack 最大深度，Array 實作在時間與空間效率上皆優於 Linked List 實作。

## 相關頁面

- 核心概念：[[stacks-and-backtracking]]、[[linked-lists]]
- 跨文比較：[[array-vs-linked-list-and-stack]]
- 延伸閱讀：[[Sue-DS-Ch03-LinkedLists]]
