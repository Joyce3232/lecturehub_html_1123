# 簡報大綱：資料結構入門 — Linked Lists 與 Stacks（16 頁完整教學版）

- **內容範圍（Scope Lock）**：聚焦資料結構第三章 Linked Lists（Ch 3）與第四章 Stacks（Ch 4），涵蓋線性串列分類、單向／環狀／雙向／多重鏈結串列演算法、Stack ADT（Linked List vs. Array 實作）及四大經典應用。
- **目標讀者**：剛學過陣列（Array）、想從零看懂指標串列與堆疊原理及演算法的初學者。
- **來源頁面**：[[Sue-DS-Ch03-LinkedLists]]、[[Sue-DS-Ch04-Stacks]]、[[linked-lists]]、[[stacks-and-backtracking]]、[[array-vs-linked-list-and-stack]]

---

## 全簡報因果知識地圖（Knowledge Map）

```text
[1-3 動機與分類] 陣列插入刪除要整排搬家怎麼辦？ → Linear List 分類（General vs. Restricted）→ Array vs. Linked List 權衡
        │
        ▼
[4-8 Singly Linked List 核心演算法] Self-Referential Node 與 Head Metadata
        │   ├─► 雙指標搜尋 searchList (pPre, pLoc) 找出目標或「應插入位置」
        │   └─► 插入 insertNode / 刪除 deleteNode 四情境化簡為兩大類 → 走訪與銷毀
        ▼
[9 進階鏈結結構] 單向只能往前走怎麼辦？ → Circularly（防繞圈）/ Doubly（雙向修正）/ Multilinked（單份資料多排序）
        │
        ▼
[10-11 進入 Stack ADT] 把增刪限制在單一端點 Top → LIFO（Push/Pop/Top）→ Linked List 版 vs. Array 版實作權衡
        │
        ▼
[12-15 Stack 四大實戰應用]
        │   ├─► 反轉（十進位轉二進位）＆ 語法剖析（括號配對）
        │   ├─► 運算式處理：Infix 轉 Postfix（優先權比較）→ Postfix 求值
        │   └─► 回溯法（Backtracking）：記憶 Branch Point → 迷宮尋路與八皇后問題
        ▼
[16 全章核心結論] Array / Linked List / Stack 選型決策與 OS 記憶體局部性延伸
```

## 貫穿全簡報的教學主線索（Core Threads）

1. **雙指標邊界化簡（`pPre` & `pLoc`）**：在 Linked List 中只要同時掌握「前驅」與「目前節點」，所有看似複雜的頭尾邊界都能收斂為兩種情況。
2. **Data Hiding（資料隱藏）與 ADT 抽象**：呼叫端只需透過標準介面（`insertNode`、`pushStack`、`emptyStack`），不必知道底層是指標還是陣列。
3. **空間與時間的結構權衡**：連續陣列換來 $O(1)$ 隨機存取與 Binary Search；指標鏈結換來 $O(1)$ 動態增刪與彈性容量。

---

## 逐頁大綱清單（16 頁）

## Slide 01: 封面總覽 — 為什麼學會了 Array，還需要 Linked List 與 Stack？
- **一句話核心**：Array 像固定連號的電影院座位（好找但難插隊），Linked List 像可隨時加掛的火車車廂，Stack 則像只能從最上面拿放的一疊盤子。
- **教學目標**：用生活比喻建立整體學習地圖，點出「資料的擺放形狀決定了搜尋、插入與應用的效率」。
- **銜接提問**：在認識火車車廂之前，程式世界裡「排成一排的資料（Linear List）」到底分成哪幾種？
- **來源**：[[Sue-DS-Ch03-LinkedLists]]、[[Sue-DS-Ch04-Stacks]]

## Slide 02: Linear List 分類與四大基本操作 — General vs. Restricted
- **一句話核心**：線性串列依「能不能從中間插隊」分為任意增刪的 General List 與只能從端點進出的 Restricted List。
- **教學目標**：區分 Unordered (Random) 與 Ordered List、FIFO (Queue) 與 LIFO (Stack)，並說明 Insertion、Deletion、Retrieval、Traversal 四大操作。
- **銜接提問**：同樣是 General List，用 Array 和用 Linked List 來裝，各自擅長與不擅長什麼？
- **來源**：[[Sue-DS-Ch03-LinkedLists]]

## Slide 03: Array vs. Linked List 的核心權衡 — 隨機存取 vs. 動態增刪
- **一句話核心**：Array 連續存放支援 Binary Search 但插刪要整排搬移；Linked List 不連續存放插刪免搬移，卻只能循序搜尋。
- **教學目標**：透過對比表建立「為什麼 Linked List 不能用 Binary Search」的直覺與複雜度認知。
- **銜接提問**：既然 Linked List 不需要連續記憶體，那每個車廂（節點）裡面到底要記什麼，才能找得到下一節？
- **來源**：[[Sue-DS-Ch03-LinkedLists]]、[[array-vs-linked-list-and-stack]]

## Slide 04: Linked List 資料結構解剖 — Head Metadata 與 Self-Referential Node
- **一句話核心**：每個 Node 靠「資料欄位＋下一個節點指標」串成鏈條，再由一個 Head 結構統一記錄 `count` 與起點 `head`。
- **教學目標**：解釋 Self-Referential Structure、`pHead == null` 空串列狀態，以及可選指標 `pLoc`、`pLast (pRear)` 如何提升效率。
- **銜接提問**：要在一個已經依 `key` 排好序的 Linked List 中找資料或找插入點，指標該怎麼往前走？
- **來源**：[[Sue-DS-Ch03-LinkedLists]]、[[linked-lists]]

## Slide 05: Ordered Search（`searchList`）— 雙指標 `pPre` 與 `pLoc` 的設計藝術
- **一句話核心**：搜尋時讓 `pPre` 緊跟在 `pLoc` 身後一步，就算找不到目標，也剛好標定出「新資料該插在哪裡」。
- **教學目標**：圖解成功與失敗三種情境（Table 3-1：小於首節點、介於中間、大於尾節點）並解析 Algorithm 3-4 迴圈條件。
- **銜接提問**：拿到 `pPre` 和 `pLoc` 之後，要把新節點接進串列裡，有哪些順序絕對不能寫錯？
- **來源**：[[Sue-DS-Ch03-LinkedLists]]、[[linked-lists]]

## Slide 06: Linked List 插入（`insertNode`）— 四種情境如何化簡為「兩大類」？
- **一句話核心**：插入空串列、最前、中間與最後四種情況，在程式裡只需判斷 `pPre` 是否為 `null` 兩條路，且接線必須「先接後再接前」。
- **教學目標**：解析 Algorithm 3-2 偽碼、`allocate` 溢位處理，以及 `pNew->link = pPre->link` 不可與 `pPre->link = pNew` 顛倒的原因。
- **銜接提問**：反過來，如果要把串列裡的某個節點安全拿掉並還給系統記憶體，又該怎麼拆線？
- **來源**：[[Sue-DS-Ch03-LinkedLists]]、[[linked-lists]]

## Slide 07: Linked List 刪除（`deleteNode`）與記憶體回收（`recycle`）
- **一句話核心**：刪除同樣化簡為「刪第一顆（`pPre == null`）」與「刪其他顆」兩大類，取出 `dataOut` 後務必 `recycle` 釋放記憶體。
- **教學目標**：圖解圖 3-14 與 3-15 的指標跳過（Bypass）邏輯與 Algorithm 3-3，強調統一在條件外扣減 `count` 與回收節點。
- **銜接提問**：學會了單筆增刪之後，如果想把整條串列從頭讀一遍、或不再需要整條串列時該怎麼收尾？
- **來源**：[[Sue-DS-Ch03-LinkedLists]]、[[linked-lists]]

## Slide 08: 走訪（`getNext`）、銷毀（`destroyList`）與系統模組架構
- **一句話核心**：用 `list.pos` 記住目前走訪進度讓外部迴圈逐步取資料，最後用 `destroyList` 逐顆回收所有節點避免記憶體洩漏。
- **教學目標**：比較兩種 Traversal 設計、解析 Algorithm 3-9 / 3-10 與 `append`（Algorithm 3-18），以及 `buildLinkedList` 十模組階層圖。
- **銜接提問**：單向串列只能一路往後走，如果我們想「繞成一圈」、「往回走」或「同時依兩種欄位排序」呢？
- **來源**：[[Sue-DS-Ch03-LinkedLists]]

## Slide 09: 進階鏈結結構 — Circularly、Doubly 與 Multilinked Lists
- **一句話核心**：環狀串列讓尾端接回頭（須防搜尋無限繞圈）、雙向串列多加 `back` 指標方便雙向增刪、多重串列讓一份資料共用多條排序鏈。
- **教學目標**：重點說明 `startAddress` 防護、Algorithm 3-22 課堂手寫修正（`pPre->fore = pNew` 與 `pSucc null`），以及總統計畫圖 3-25。
- **銜接提問**：如果我們刻意「限制」串列只能從同一端放進與拿出資料，會變成什麼威力強大的結構？
- **來源**：[[Sue-DS-Ch03-LinkedLists]]、[[linked-lists]]

## Slide 10: 從 General 走向 Restricted — Stack（堆疊）與 LIFO 原則
- **一句話核心**：Stack 是「後進先出（LIFO）」的受限串列，所有進出都只發生在頂端 `Top`，支援 Push、Pop 與 Stack Top 三種操作。
- **教學目標**：用疊盤子／硬幣比喻建立直覺，釐清 `Pop`（刪除並回傳）vs. `Stack Top`（唯讀不刪除），以及 Overflow / Underflow 錯誤。
- **銜接提問**：想把 Stack 做成可重複呼叫的標準函式庫（ADT），底層可以用哪些結構來實作？
- **來源**：[[Sue-DS-Ch04-Stacks]]、[[stacks-and-backtracking]]

## Slide 11: Stack ADT、Data Hiding 與雙軌實作（Linked List vs. Array）
- **一句話核心**：透過八大 ADT 函式隱藏底層細節；容量未知時用 Linked List 版（指標），最大深度可預估時用 Array 版（索引）更快更省空間。
- **教學目標**：解析 `pushStack` / `popStack` 與 `emptyStack` 的 Data Hiding 意義，並對比 Algorithm 4-16 Array 實作（`stackAry`、`stackMax`、`top`）。
- **銜接提問**：看起來規則這麼簡單的「後進先出」堆疊，在真實程式問題裡究竟能解決哪些難題？
- **來源**：[[Sue-DS-Ch04-Stacks]]、[[array-vs-linked-list-and-stack]]

## Slide 12: Stack 應用一＆二 — 資料反轉與括號語法剖析
- **一句話核心**：利用「後進先出」天然特性，把十進位轉二進位反序餘數翻正，並用 Push/Pop 即時抓出少左括號或少右括號的語法錯誤。
- **教學目標**：解析 `decimalToBinary`（$26_{10} = 11010_2$）與 `parseParens`（Algorithm 4-11）的兩種錯誤偵測時機。
- **銜接提問**：除了檢查括號有沒有成對，編譯器怎麼靠 Stack 看懂「先乘除後加減」的數學算式？
- **來源**：[[Sue-DS-Ch04-Stacks]]、[[stacks-and-backtracking]]

## Slide 13: Stack 應用三（上）— Infix 轉 Postfix 運算式轉換
- **一句話核心**：把運算子暫存進 Stack 並依優先權（`*,/` = 2、`+,-` = 1、`(` = 0）決定何時彈出，就能把含括號的中序式轉為無歧義後序式。
- **教學目標**：對比 Prefix / Infix / Postfix，並逐步追蹤 `A + B * C - D / E` 轉為 `A B C * + D E / -` 的演算法步驟（Algorithm 4-12）。
- **銜接提問**：轉成沒有括號的 Postfix 算式之後，電腦只要再掃描一遍就能算出答案嗎？
- **來源**：[[Sue-DS-Ch04-Stacks]]、[[stacks-and-backtracking]]

## Slide 14: Stack 應用三（下）— Postfix 表達式求值（`postFixEvaluate`）
- **一句話核心**：掃描後序式時遇數字就 Push 數值、遇運算子就 Pop 兩數計算後再 Push 回去，但要注意「先 Pop 出來的是右運算元 `operand2`」。
- **教學目標**：以 `2 4 6 + *`（$= 20$）與減法／除法順序為例，解析 Algorithm 4-13 為何 Push 數值而非變數名，以及運算元順序陷阱。
- **銜接提問**：Stack 不只會算數學，當程式在迷宮或棋盤裡「走錯路想反悔」時，怎麼靠它回到上一個路口？
- **來源**：[[Sue-DS-Ch04-Stacks]]、[[stacks-and-backtracking]]

## Slide 15: Stack 應用四 — Backtracking（回溯法）與八皇后問題
- **一句話核心**：每逢分岔路口就把選擇 Push 進 Stack 留作退路，走到死胡同就 Pop 退回上一個分支點改試下一條路。
- **教學目標**：圖解迷宮尋路（Goal Seeking）的 `Branch Point` 運作，並逐步追蹤 4×4 簡化版八皇后問題的放置與 Pop 回退過程（Algorithm 4-15）。
- **銜接提問**：學完 Array、Linked List 與 Stack 的所有機制後，實務寫程式時該怎麼挑對資料結構？
- **來源**：[[Sue-DS-Ch04-Stacks]]、[[stacks-and-backtracking]]

## Slide 16: 全章總結、核心結論（Key Takeaways）與選型實戰
- **一句話核心**：資料結構沒有絕對好壞——要隨機查找與記憶體局部性選 Array，要動態中間插刪選 Linked List，要狀態回溯與算式解析選 Stack。
- **教學目標**：總結全份簡報的 **核心結論（Key Takeaways）**，並將 Array 連續配置連結至作業系統的 Spatial Locality 效能視角。
- **來源**：[[Sue-DS-Ch03-LinkedLists]]、[[Sue-DS-Ch04-Stacks]]、[[array-vs-linked-list-and-stack]]
