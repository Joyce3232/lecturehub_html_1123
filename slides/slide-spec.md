# 逐頁內容規格書：資料結構入門 — Linked Lists 與 Stacks（雙軌教學版：白話直覺 ＋ 專業詳解・16 頁）

> 貫穿全簡報的雙軌設計：**白話入門**（電影院連號座位＝Array、火車車廂＝Linked List、一疊盤子＝Stack）＋ **專業深入**（Self-referential 結構、雙指標 `pPre`/`pLoc`、時間複雜度、ADT 封裝與四大經典演算法）。

---

## Slide 01: 封面總覽 — 為什麼學會了 Array，還需要 Linked List 與 Stack？
- **版面配置**：Split（左側生活比喻＋3 張雙軌目標卡／右側橘子倉鼠插畫）
- **圖貼配置**：`assets/2811CFAF-EB2B-43CF-A63B-094EEF4BC53C.jpeg`
- **白話入門**：Array 就像電影院的連號座位——看座位號就能秒找到人，但中間想多塞一位朋友就得整排往後移！Linked List 改用「火車車廂＋掛勾」隨時加掛；Stack 則像「一疊盤子」，規定只能從最上面拿放，反而能解決算式與迷宮問題。
- **專業深入**：資料結構（Data Structure）的核心在於「記憶體佈局決定操作成本」。本簡報涵蓋 Linear List 的兩大分支：**General List（Linked List）** 如何以非連續動態配置消除搬移成本，以及 **Restricted List（Stack）** 如何透過嚴格的 LIFO（Last-In, First-Out）存取限制實現 Data Hiding、運算式轉換與回溯演算法（Backtracking）。
- **過渡提問**：在動手拆解火車車廂之前，程式世界裡的「線性串列（Linear List）」究竟分成哪幾大類、支援哪些基本操作？
- **溯源**：[[Sue-DS-Ch03-LinkedLists]]、[[Sue-DS-Ch04-Stacks]]

## Slide 02: Linear List 分類與四大基本操作 — General vs. Restricted
- **版面配置**：Bento 2x2 ＋ 四大操作比較表
- **白話入門**：把資料排成一列就是 Linear List。如果「排隊到一半可以任意插隊、抽出中間任何一人」，叫 **General List**；如果規定「只能從頭尾兩端進出」，像排隊買飲料（Queue）或疊盤子（Stack），就叫 **Restricted List**。
- **專業深入**：
  - **General List**：不限增刪位置，分為 **Unordered (Random) List**（實務應用較少）與 **Ordered List**（依 `key` 欄位維持遞增或遞減順序）。
  - **Restricted List**：僅允許在端點操作，包含 **FIFO（Queue）** 與 **LIFO（Stack）**。
  - **四大操作（Figure 3-2）**：`Insertion`（插入，Ordered 須維持順序）、`Deletion`（刪除）、`Retrieval`（讀取元素且不破壞串列，但 Queue/Stack 取出即破壞）、`List Traversal`（循序走訪全數元素，**不適用於 Restricted Lists**）。
- **過渡提問**：同屬 General List，用學過的 Array（陣列）和用 Linked List 來實作，兩者在效能上到底差在哪裡？
- **溯源**：[[Sue-DS-Ch03-LinkedLists]]

## Slide 03: Array vs. Linked List 的核心權衡 — 隨機存取 vs. 動態增刪
- **版面配置**：對比矩陣表 ＋ ⚠️ 常見誤區卡 ＋ 右下角邊角圖貼
- **圖貼配置**：`assets/A5308558-B20D-4FE2-81E6-15BA8A53D6DB.jpeg`
- **白話入門**：Array 把所有資料緊緊並排在連續記憶體裡，想知道第 50 格是誰一秒就算得出地址；Linked List 的節點分散在各地，靠「下一節點的地址小紙條」串起來，插隊只要換紙條，但找人必須從第一節車廂一節一節問過去。
- **專業深入**：
  - **搜尋複雜度**：Array 具連續記憶體位址，有序時可用 **Binary Search（$O(\log n)$）**；Linked List 節點間**沒有實體連續關係（No physical relationship）**，因此**無法使用 Binary Search**，僅能使用 Sequential Search（$O(n)$）。
  - **增刪複雜度**：Array 在中間插入或刪除後，須將後續元素逐一搬移（Shifting，$O(n)$）；Linked List 只要更新指標即可完成邏輯增刪（$O(1)$ 指標操作），徹底免除資料搬移成本。
- **過渡提問**：既然 Linked List 不需要連續記憶體，那每一節車廂（Node）和起點管理員（Head）到底要存哪些欄位？
- **溯源**：[[Sue-DS-Ch03-LinkedLists]]、[[array-vs-linked-list-and-stack]]

## Slide 04: Linked List 資料結構解剖 — Head Metadata 與 Self-Referential Node
- **版面配置**：雙欄（上方節點指標 SVG 圖示＋下方結構與偽碼宣告）
- **圖示設計**：繪製指標方塊 SVG，呈現 `Head (count, head)` 指向 `[data|link] → [data|link] → [data|null]`，並對照空串列 `head = null`。
- **白話入門**：一個完整的 Linked List 有兩種方塊：「火車頭管理表（Head）」只負責記車廂總數 `count` 與第一節在哪 `head`；「資料車廂（Node）」則一半裝貨物 `data`，另一半放指向下一節車廂的箭頭 `link`。沒有車廂時，`head` 就指著空符號 `null`。
- **專業深入**：
  - **Self-Referential Structure（自我參照結構）**：每個 `node` 包含 `data`（內含搜尋鍵 `key` 與多個資料欄位）以及一個指向同型別結構的指標 `link`（最後一節為 `null`）。
  - **Head Node Structure（Metadata）**：儲存 `count <integer>` 與 `head <pointer>`；實務上可擴充 `pos`（紀錄走訪位置）與 `rear / pLast`（指向尾節點，讓尾端操作與搜尋更有效率）。
  - **Create List（Algorithm 3-1）**：配置後必須主動初始化 `list.head = null` 與 `list.count = 0`，避免記憶體殘留垃圾值造成錯亂。
- **過渡提問**：如果要在一條已排序的 Linked List 中搜尋某個 `key`，或想知道新資料該插在哪裡，指標該怎麼移動？
- **溯源**：[[Sue-DS-Ch03-LinkedLists]]、[[linked-lists]]

## Slide 05: Ordered Search（`searchList`）— 雙指標 `pPre` 與 `pLoc` 的設計藝術
- **版面配置**：雙欄（雙指標步進 SVG 圖示＋Table 3-1 搜尋結果矩陣）
- **圖示設計**：繪製 `pPre` 與 `pLoc` 並進 SVG 圖，標示命中時（`pLoc` 指目標）與未命中插入點（`pPre` 指 `15`、`pLoc` 指 `20`，目標 `18` 落於兩者之間）。
- **白話入門**：想像兩個人一起走過火車車廂：`pLoc` 走在前面檢查車廂號碼，`pPre` 永遠慢一步跟在後面。一旦發現號碼已經「超過」目標（代表目標不在車上），`pPre` 與 `pLoc` 中間的縫隙，就剛好是新乘客應該插隊進來的位置！
- **專業深入**：
  - **Algorithm 3-4 核心迴圈**：初始 `pPre = null`、`pLoc = list.head`，執行 `loop (pLoc not null AND target > pLoc->data.key)`，每次將 `pPre = pLoc`、`pLoc = pLoc->link`。
  - **🔑 雙重保護與四種邊界回傳（Table 3-1）**：
    1. `target < first`：`pPre = null, pLoc = first`，回傳 `false`。
    2. `target == node`：`pPre = 前驅, pLoc = 目標`，回傳 `true`。
    3. `first < target < last`（未命中）：`pPre` 停在小於目標的最大節點、`pLoc` 停在大於目標的首個節點，回傳 `false`。
    4. `target > last`：`pPre = last, pLoc = null`，回傳 `false`。
- **過渡提問**：拿到了 `pPre` 和 `pLoc` 這兩個指標後，把新節點接進串列裡看似有四種位置，為什麼程式卻能寫得極簡？
- **溯源**：[[Sue-DS-Ch03-LinkedLists]]、[[linked-lists]]

## Slide 06: Linked List 插入（`insertNode`）— 四種情境如何化簡為「兩大類」？
- **版面配置**：Split（左側兩大類邏輯＋接線順序 SVG 圖示／右側嫩葉倉鼠插畫）
- **圖貼配置**：`assets/4F4E807E-05CE-4289-B1DC-C64E8077071F.jpeg`
- **圖示設計**：用編號箭頭 SVG 圖解 Before → After：`① pNew->link = pPre->link`（虛線新接後繼）、`② pPre->link = pNew`（實線改接新節點），對照 `pPre == null` 改動 `list.head`。
- **白話入門**：加掛新車廂看似有「空列車、最前面、中間、最後面」4 種狀況，但只要看前面有沒有車廂（`pPre` 是否為空）就只剩 2 類！而且掛勾一定要「先讓新車廂勾住後面的車，再讓前面的車改勾新車廂」，順序反了後面整串車廂會直接斷掉飛走！
- **專業深入**：
  - **四合一收斂（Algorithm 3-2）**：先 `allocate(pNew)`（若記憶體滿則回傳 `false` 表 Overflow），填入 `pNew->data = dataIn`：
    - **第一大類（`pPre == null`，空串列或插在最前）**：`pNew->link = list.head` → `list.head = pNew`。
    - **第二大類（`pPre != null`，插在中間或最後）**：`pNew->link = pPre->link` → `pPre->link = pNew`（插在尾端時 `pPre->link` 本身即 `null`，邏輯完全一致！）。
  - **⚠️ 關鍵禁忌**：兩行指標賦值順序**絕對不可顛倒**，否則 `list.head` 或 `pPre->link` 原先指向的後續鏈結會被覆寫遺失。最後執行 `list.count += 1`。
- **過渡提問**：新節點會接了，那如果要把串列裡的某個節點安全拆掉並把記憶體還給系統，指標又該怎麼改？
- **溯源**：[[Sue-DS-Ch03-LinkedLists]]、[[linked-lists]]

## Slide 07: Linked List 刪除（`deleteNode`）與記憶體回收（`recycle`）
- **版面配置**：雙欄（Bypass 拆線 SVG 圖示＋Algorithm 3-3 偽碼與分析）
- **圖示設計**：繪製 `pPre → [39]` 直接跨過 `(Recycled) [75]` 連向 `[134]` 的指標繞過 SVG，標示 `① pPre->link = pLoc->link` 與 `② recycle(pLoc)`。
- **白話入門**：要把中間一節車廂卸下來，只需讓「前一節車廂的掛勾直接跳過它、勾住下一節」，再把卸下的車廂報廢回收（`recycle`）就好。同樣四種位置（唯一一節、第一節、中間、最後一節）也只要判斷 `pPre` 是否為空兩條路！
- **專業深入**：
  - **Algorithm 3-3 核心步驟**：呼叫端須先透過 `searchList` 定位出 `(pPre, pLoc)`，先備份欲刪除資料 `dataOut = pLoc->data`：
    - **刪除首節點／唯一節點（`pPre == null`）**：`list.head = pLoc->link`（若為唯一節點則 `head` 自動變回 `null`）。
    - **刪除中間／尾節點（`pPre != null`）**：`pPre->link = pLoc->link`（跳過 `pLoc`，邏輯移除）。
  - **記憶體管理**：於 `if/else` 區塊外統一執行 `list.count -= 1` 與 `recycle(pLoc)`（實體歸還動態記憶體），避免重複程式碼與 Memory Leak。
- **過渡提問**：單筆搜尋、插入與刪除都掌握了，若想「從頭到尾印出整條串列」或「整條串列用完丟掉」，該怎麼設計模組？
- **溯源**：[[Sue-DS-Ch03-LinkedLists]]、[[linked-lists]]

## Slide 08: 走訪（`getNext`）、銷毀（`destroyList`）與系統模組架構
- **版面配置**：Bento 2x2（Traversal / Destroy / Append / 10 模組階層）
- **白話入門**：`getNext` 像書籤（`list.pos`），第一次翻開給旗標 `0` 從第一頁讀起，之後給 `1` 就自動翻到下一頁；用完整條串列時，`destroyList` 會像拆積木一樣從頭把每一塊拆下來回收，直到數量歸零。
- **專業深入**：
  - **外部控制走訪（Algorithm 3-9 `getNext`）**：在 Head 加入 `pos` 指標記錄當前位置；`fromWhere == 0` 時從 `list.head` 起算（須防 `count == 0`），否則檢查 `list.pos->link != null` 後推進 `list.pos` 並回傳 `dataOut`。
  - **銷毀與串接**：`destroyList`（3-10）於 `list.count != 0` 迴圈暫存 `dltPtr = list.head`、後移 `head`、遞減 `count` 並 `recycle(dltPtr)`；`append`（3-18）走訪至 `list1` 尾端接上 `list2.head` 並累加 `count`。
  - **整合架構（Figure 3-18）**：`buildLinkedList` 透過 `createList`、`addNode`、`removeNode`、`printList` 與 `destroyList` 協作完成 10 模組分工。
- **過渡提問**：單向串列只能一直往前走，如果實務上需要「頭尾相接繞圈」、「前後雙向移動」或「同時依多種欄位排序」呢？
- **溯源**：[[Sue-DS-Ch03-LinkedLists]]

## Slide 09: 進階鏈結結構 — Circularly、Doubly 與 Multilinked Lists
- **版面配置**：三欄結構對比卡（各附微型指標 SVG）＋ ⚠️ 課堂修正重點條
- **圖示設計**：三張 SVG 分別呈現：Circularly 尾節點迴圈指向首節點、Doubly 雙向 `B|data|F` 箭頭互指、Multilinked 雙色指標鏈共用同組節點。
- **白話入門**：**環狀串列**像旋轉壽司，最後一盤接回第一盤；**雙向串列**像雙向捷運，每站都能往前也能往後搭；**多重串列**則像同一本員工名冊，同時貼上「依姓名排」和「依年資排」兩條彩色線，不用影印兩份資料！
- **專業深入**：
  - **Circularly Linked List**：尾節點 `link` 指向首節點，增刪尾節點須更新 `rear`；自中間搜尋不存在目標時，迴圈必加 `pLoc->link != startAddress` 防止無窮迴圈。
  - **Doubly Linked List（Algorithm 3-22 / 3-23）**：節點含 `back` 與 `fore` 指標，Head 含 `count, head, rear`。**⚠️ 課堂修正（3-22）**：原偽碼第 4.9 行 `pPre->fore = pNew` 應移至 `else` 內的 4.4.3 行，且 4.6 行判斷尾端插入須改為 `if (pSucc null)`。刪除 `deleteDbl` 則分別檢查 `pDlt->back` 與 `pDlt->fore` 是否為空。
  - **Multilinked Lists**：單一節點只 `allocate` 與計數一次，內含多組指標鏈（如總統與配偶雙鏈，Figure 3-25）節省記憶體。
- **過渡提問**：看完了可以任意進出的 General List，如果我們刻意把增刪限制在「同一端」，會誕生什麼經典資料結構？
- **溯源**：[[Sue-DS-Ch03-LinkedLists]]、[[linked-lists]]

## Slide 10: 從 General 走向 Restricted — Stack（堆疊）與 LIFO 原則
- **版面配置**：Split（左側疊盤子比喻＋三大操作與異常卡／右側餅乾倉鼠插畫）
- **圖貼配置**：`assets/A5308558-B20D-4FE2-81E6-15BA8A53D6DB.jpeg`
- **白話入門**：Stack 就像洗好疊起來的一疊盤子（或一疊硬幣）：你只能把新盤子「疊在最上面（Push）」，要拿也只能「從最上面拿走（Pop）」，或者「偷看最上面那塊的花色（Stack Top）」。最後放上去的，一定最先被拿走！
- **專業深入**：
  - **LIFO（Last-In, First-Out）定義**：所有插入與刪除皆限制於同一端 `Top`；依序推入 `{5, 10, 15, 20}`，彈出順序必為 `{20, 15, 10, 5}`。
  - **三大核心操作與邊界異常**：
    1. `Push`：將資料放入 `Top`；若空間已滿則發生 **Overflow**。
    2. `Pop`：移除 `Top` 資料並回傳給呼叫端；若堆疊為空則發生 **Underflow**。
    3. `Stack Top`：複製回傳 `Top` 資料**但不刪除該節點**（空堆疊時同樣觸發 Underflow）。
- **過渡提問**：如果想把 Stack 做成可重複使用的標準函式庫（ADT），裡面要提供哪些介面？底層又有哪些實作方式？
- **溯源**：[[Sue-DS-Ch04-Stacks]]、[[stacks-and-backtracking]]

## Slide 11: Stack ADT、Data Hiding 與雙軌實作（Linked List vs. Array）
- **版面配置**：雙欄（Linked List vs. Array 實作指標／索引 SVG 圖示＋雙實作對比表）
- **圖示設計**：左右並排比較 `head(count, top)` 串接鏈結節點 vs. 連續陣列 `stackAry[0..4]` 與整數索引 `top = 2`。
- **白話入門**：使用 Stack 就像操作自動販賣機：你只需要按「投入（Push）」、「取出（Pop）」或問「空了沒（emptyStack）」，根本不用管機器內部是用「串接車廂（Linked List）」還是「固定格子（Array）」來裝東西！
- **專業深入**：
  - **Data Hiding（資料隱藏）與 8 大 ADT 操作**：除了 `createStack`、`pushStack`、`popStack`、`stackTop`、`destroyStack` 之外，特設 `emptyStack`、`fullStack`、`stackCount`（僅 1 行 `return stack.count`），嚴格禁止呼叫端直接讀寫 `stack` 內部欄位。
  - **Linked List 實作**：Head 含 `(count, top <node pointer>)`，節點含 `(data, next)`；容量動態彈性，但每次 Push/Pop 皆須 `allocate`/`recycle` 且多佔 1 個指標空間。
  - **Array 實作（Algorithm 4-16）**：Head 改為 `(stackAry, count, stackMax, top <index>)`；**若最大深度可於寫程式前估算，Array 實作無指標空間開銷且執行效率更高**。
- **過渡提問**：規則這麼單純的「後進先出」堆疊，在程式世界裡到底能解決哪四大類經典問題？
- **溯源**：[[Sue-DS-Ch04-Stacks]]、[[array-vs-linked-list-and-stack]]

## Slide 12: Stack 應用一＆二 — 資料反轉與括號語法剖析
- **版面配置**：雙欄（十進位轉二進位追蹤 vs. 括號配對狀態機）
- **白話入門**：十進位轉二進位時，一直除以 2 拿到的餘數剛好「頭尾顛倒」，先全丟進 Stack 再倒出來就變正了！檢查程式碼括號也是：看到左括號先收進口袋（Push），看到右括號就拿一個左括號出來配對（Pop）。
- **專業深入**：
  - **應用一：資料反轉（Reversing Data）**：
    - `reverseNumber`（4-9）與 `decimalToBinary`（4-10）：以 $26_{10}$ 為例，連續 $\bmod\ 2$ 依序得 `0, 1, 0, 1, 1`（低位到高位），Push 入棧後再依序 Pop 印出正確二進位 $11010_2$。
  - **應用二：語法剖析（Parsing — Algorithm 4-11 `parseParens`）**：
    - 遇 `(` 則 `pushStack`；遇 `)` 時若 `emptyStack(stack)` 代表**多出右括號（缺左括號）**，否則 `popStack` 配對。
    - 掃描整份檔案結束後，若 `!emptyStack(stack)` 代表**左括號未閉合（缺右括號）**。
- **過渡提問**：除了檢查括號有沒有成對，編譯器怎麼利用 Stack 看懂「先乘除後加減」的數學運算式？
- **溯源**：[[Sue-DS-Ch04-Stacks]]、[[stacks-and-backtracking]]

## Slide 13: Stack 應用三（上）— Infix 轉 Postfix 運算式轉換
- **版面配置**：優先權規則卡 ＋ `A+B*C-D/E` 步驟追蹤表 ＋ 右下角邊角圖貼
- **圖貼配置**：`assets/4F4E807E-05CE-4289-B1DC-C64E8077071F.jpeg`
- **白話入門**：我們平常寫的 `A + B * C`（中序）一定要靠括號才不會算錯；把運算子挪到後面的 `A B C * +`（後序）完全不需要括號！轉換時把運算子暫存進 Stack，誰優先權高就先留著，遇到「比自己大或一樣大」的就先請出來輸出。
- **專業深入**：
  - **三種表示法**：Prefix（`+ a b`）、Infix（`a + b`，須括號）、Postfix（`a b +`，無須括號且具單一求值規則）。
  - **優先權與演算法（Algorithm 4-12 `inToPostFix`）**：設定 `priority(*, /) = 2`、`priority(+, -) = 1`、棧內 `priority('(') = 0`（`(` 無條件入棧且不會被其他運算子誤彈）。
    - Operand 直接輸出；`)` 持續 Pop 輸出直到遇 `(` 丟棄。
    - Operator 須迴圈檢查 `!emptyStack AND priority(token) <= priority(topToken)`，不斷 Pop 輸出後再 Push 自己；最後清空 Stack。
  - **範例追蹤**：`A + B * C - D / E` 依序輸出為 `A B C * + D E / -`。
- **過渡提問**：拿到這串沒有括號的 Postfix 字串 `A B C * + D E / -` 後，電腦要怎麼一步步算出數值？
- **溯源**：[[Sue-DS-Ch04-Stacks]]、[[stacks-and-backtracking]]

## Slide 14: Stack 應用三（下）— Postfix 表達式求值（`postFixEvaluate`）
- **版面配置**：雙欄（Stack 推彈求值 SVG 圖解 vs. ⚠️ 運算元 Pop 順序陷阱）
- **圖示設計**：繪製 `2 4 6 + *` 五階段堆疊變化 SVG，標出遇 `+` 時先 Pop `6`（`operand2`）再 Pop `4`（`operand1`）推回 `10`。
- **白話入門**：計算後序式就像「把數字先放在盤子疊起來，看到加減乘除符號時，再從最上面抓兩塊數字出來算，算完把結果放回最上面」！但要小心：減法和除法有前後順序，先抓出來的是「右邊」的數字！
- **專業深入**：
  - **Algorithm 4-13 核心邏輯**：由左至右掃描 `expr`：
    1. 遇 Operand：將其**數值（而非變數名稱）**Push 進 Stack。
    2. 遇 Operator：**第一次 `popStack` 為 `operand2`（右運算元），第二次 `popStack` 為 `operand1`（左運算元）**，計算 `value = calculate(operand1, operator, operand2)` 後再 Push 回 Stack。
    3. 掃描結束後，Pop 出棧頂唯一剩餘值即為結果。
  - **範例追蹤（`A B C + *`，設 $a=2, b=4, c=6$）**：依序 Push `2, 4, 6` → 遇 `+` Pop `6` 與 `4` 得 $4+6=10$ 推回 → 遇 `*` Pop `10` 與 `2` 得 $2 \times 10 = 20$。
- **過渡提問**：Stack 不只能反轉資料和算數學，當程式在迷宮或棋盤裡「走錯路想反悔」時，怎麼靠它找回退路？
- **溯源**：[[Sue-DS-Ch04-Stacks]]、[[stacks-and-backtracking]]

## Slide 15: Stack 應用四 — Backtracking（回溯法）與八皇后問題
- **版面配置**：雙欄（Goal Seeking 迷宮退路 vs. 4×4 皇后回溯 SVG 棋盤）
- **圖示設計**：繪製 4×4 皇后棋盤與 Stack 狀態推演 SVG（標示 `(2,3)` 衝突 Pop 改推 `(2,4)`）。
- **白話入門**：走迷宮遇到岔路時，在路口插一支旗子記在 Stack 裡再往前走；萬一前面是死胡同，就照著 Stack 最上面那張紙條退回剛剛的路口，換另一條沒走過的岔路繼續試！
- **專業深入**：
  - **Goal Seeking（Algorithm 4-14 `seekGoal`）**：經過 `branchPoint` 時將候選分支 Push 進 Stack（如圖 4-14 的節點 `B12, B9, B8`）；遇死路（End）時不斷 Pop 退回最近的未探索分支點，直到抵達 `goal`（`1→2→3→12→13→14→15→16`）。
  - **Eight Queens Problem（Algorithm 4-15 `queens8`）**：在 $N \times N$ 棋盤逐列放置皇后使彼此不互相攻擊（同列、同行、斜線皆不可）。若某列所有欄位皆被防守（`guarded(row, col)`），便透過 `popStack` 退回上一列已放置的皇后位置並遞增 `col` 改試下一格（如 4×4 棋盤中 `(1,1)→(2,3)` 失敗後改試 `(2,4)`，最終收斂至 `(1,2),(2,4),(3,1),(4,3)`）。
- **過渡提問**：學完了 Array、Linked List 與 Stack 的所有細節後，實務開發時該如何挑對資料結構？
- **溯源**：[[Sue-DS-Ch04-Stacks]]、[[stacks-and-backtracking]]

## Slide 16: 全章總結、核心結論（Key Takeaways）與選型實戰
- **版面配置**：Split（左側三結構決策表＋4 點雙軌總結／右側橘子倉鼠插畫）
- **圖貼配置**：`assets/2811CFAF-EB2B-43CF-A63B-094EEF4BC53C.jpeg`
- **白話入門**：沒有哪一種資料結構是萬能的！資料量固定又常按編號查資料用 **Array**；常常從中間插隊或刪除用 **Linked List**；需要「先進後出」反轉、算式或走迷宮反悔就用 **Stack**。
- **專業深入**：
  - **跨領域效能視角（[[array-vs-linked-list-and-stack]]）**：Array 採連續配置，具備極佳的 **Spatial Locality**（有利 CPU Cache 與 OS 分頁減少 Page Fault，參見 [[virtual-memory-and-paging]]）；Linked List 的 Pointer Chasing 雖免搬移元素，但記憶體較分散。
  - **🔑 全章四大核心結論（Key Takeaways）**：
    1. Linked List 靠 `pPre` / `pLoc` 雙指標將所有插入／刪除邊界收斂為兩大類，且指標賦值順序不可顛倒。
    2. Circularly 須防搜尋無限繞圈（`startAddress`）；Doubly 須維護雙向 `back`/`fore`（留意 Algorithm 3-22 修正）。
    3. Stack 以 Data Hiding 封裝 LIFO 操作；最大深度可預估時，Array 實作比 Linked List 更快更省空間。
    4. Stack 四大應用（反轉、括號剖析、Infix→Postfix 與求值、Backtracking）皆仰賴「最近狀態優先恢復」特性。
- **溯源**：[[Sue-DS-Ch03-LinkedLists]]、[[Sue-DS-Ch04-Stacks]]、[[array-vs-linked-list-and-stack]]
