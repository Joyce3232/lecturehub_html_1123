---
title: "Stacks & Backtracking（堆疊、運算式轉換與回溯法）"
type: concept
source_type: mixed
raw_file:
  - "raw/docs/DS_Ch4.pdf"
source_url: ""
source_date: "2026-11-23"
ingested_at: "2026-11-23"
status: active
tags:
  - data-structures
  - stack
  - lifo
  - backtracking
  - parsing
---

# Stacks & Backtracking（堆疊、運算式轉換與回溯法）

## 核心結論（Key Takeaways）

1. **LIFO 與資料隱藏（Data Hiding）**：Stack 是受限於單一端點（`Top`）增刪的線性串列；透過 `emptyStack`、`fullStack`、`stackCount` 等封裝函式隔離底層為 Linked List 或 Array 的實作細節（[[Sue-DS-Ch04-Stacks]]）。
2. **時間順序反轉與語法配對**：凡是需要「後產生的先輸出」（如十進位轉二進位餘數序列）或「最近開啟的先閉合」（如括號配對 `parseParens`），皆天然對應 Stack 模型。
3. **中序轉後序（Infix → Postfix）消滅括號歧義**：透過運算子優先權比較（棧內 `(` 優先權設為 `0`，`+,-` 為 `1`，`*,/` 為 `2`），將人類習慣的 Infix 轉為電腦可直接單趟求值的 Postfix。
4. **回溯法（Backtracking）的狀態堆疊**：在迷宮尋路（Goal Seeking）與八皇后問題（Eight Queens）中，Stack 保存尚未嘗試的決策分支點，遇到死胡同即 `Pop` 退回重試。

---

## 核心機制速查

### 1. Infix 轉 Postfix 規則摘要
- **運算元**：直接輸出。
- **`(`**：無條件 Push 進 Stack（在 Stack 內優先權視為最低 `0`，避免誤彈出）。
- **`)`**：持續 Pop 輸出直到遇見 `(` 並將其丟棄。
- **運算子**：只要 Stack 頂端運算子優先權 $\ge$ 目前運算子，就 Pop 輸出後再把自己 Push 入棧；掃描結束後清空 Stack。

### 2. Postfix 求值注意順序
- 遇運算子時連續兩次 Pop：**第一次 Pop 是右運算元 `operand2`，第二次 Pop 才是左運算元 `operand1`**（對減法 `-` 與除法 `/` 順序至關重要）。

## 相關頁面

- 來源：[[Sue-DS-Ch04-Stacks]]
- 關聯概念：[[linked-lists]]
- 跨文比較：[[array-vs-linked-list-and-stack]]
