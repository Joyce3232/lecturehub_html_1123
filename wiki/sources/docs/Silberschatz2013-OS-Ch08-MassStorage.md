---
title: "OS Ch 08 (Ch 12): Mass-Storage Systems (9th Ed. 課程投影片)"
type: source
source_type: docs
raw_file: "raw/docs/OS-ch08.pdf"
source_url: ""
source_date: "2013-01-01"
ingested_at: "2026-11-23"
status: active
tags:
  - operating-systems
  - mass-storage
  - disk-scheduling
  - raid
  - zfs
---

# OS Ch 08 (Ch 12): Mass-Storage Systems (9th Ed. 課程投影片)

- **來源教材**：*Operating System Concepts – 9th Edition*（Silberschatz, Galvin & Gagne ©2013），投影片封面標示 Chapter 8（內頁對應原書 Chapter 12: Mass-Storage Systems），共 38 頁。

## 核心結論（Key Takeaways）

1. **機械硬碟受制於 Seek 與旋轉延遲**：HDD 存取延遲由 Seek Time（3–12 ms）與 Rotational Latency（$\frac{1}{2 \times \text{RPM}/60}$，7,200 RPM 約 4.17 ms）主導，促成 SSTF / SCAN / C-SCAN 等磁碟排程演算法與 SSD 的普及。
2. **網路儲存分流為 NAS 與 SAN**：NAS 透過 LAN/WAN 與 RPC（NFS/CIFS）提供檔案層存取；SAN 透過低延遲 Fibre Channel 連接儲存陣列提供區塊層存取。
3. **RAID 以冗餘換取可用度與效能**：透過 Striping（效能）與 Mirroring / Parity（容錯）組合，大幅拉長平均資料遺失時間（MTTDL）。
4. **ZFS 補足傳統 RAID 的靜默資料損毀盲點**：RAID 僅防硬碟壞軌而無法偵測 Silent Data Corruption；ZFS 以樹狀 Metadata Checksums 與 Pooled Storage 實現端到端資料完整性驗證。

---

## 核心技術細節與公式

### 1. 磁碟效能公式與實例
- **平均存取與 I/O 時間**：
  $$\text{Access Latency} = \text{Average Seek Time} + \text{Average Rotational Latency}$$
  $$\text{Average I/O Time} = \text{Access Latency} + \frac{\text{Transfer Size}}{\text{Transfer Rate}} + \text{Controller Overhead}$$
- **計算範例**（7,200 RPM、平均 Seek $5\text{ ms}$、有效傳輸率 $1\text{ Gb/s}$、Controller Overhead $0.1\text{ ms}$、讀取 $4\text{ KB}$）：
  $$\text{Average I/O Time} = 5 + 4.17 + \frac{4\text{ KB}}{1\text{ Gb/s}} + 0.1 = 9.27 + 0.12 = 9.39\text{ ms}$$

### 2. Disk Scheduling 演算法比較（請求佇列 `98, 183, 37, 122, 14, 124, 65, 67`，磁頭起始 `53`，範圍 `0–199`）
- **FCFS**：總磁頭移動 `640` cylinders。
- **SSTF（Shortest Seek Time First）**：總移動 `236` cylinders，具 SJF 特性但可能導致 Starvation。
- **SCAN（Elevator Algorithm）**：總移動 `208` cylinders，往返端點掃描。
- **C-SCAN / LOOK / C-LOOK**：C-SCAN 單向服務並快速折返以提供更均勻的等待時間；LOOK / C-LOOK 僅移動至各方向最後一個請求即折返，不必走到磁碟實體盡頭。

### 3. RAID 層級與 MTTDL 公式
- **MTTDL（Mean Time to Data Loss）計算**（兩顆鏡像硬碟獨立故障，MTTF $= 100,000\text{ hr}$，MTTR $= 10\text{ hr}$）：
  $$\text{MTTDL} = \frac{\text{MTTF}^2}{2 \times \text{MTTR}} = \frac{100,000^2}{2 \times 10} = 500 \times 10^6\text{ hours} \approx 57,000\text{ years}$$
- **RAID 層級與變體**：RAID 0（Striping）、RAID 1（Mirroring）、RAID 0+1 vs. RAID 1+0（單碟故障時 RAID 1+0 僅影響單一鏡像對，容錯較佳）、RAID 4（專用奇偶校驗碟）、RAID 5（分散式奇偶校驗）、RAID 6（$P+Q$ 雙奇偶校驗）。
- **Stable Storage 寫入協定**：每個邏輯區塊對應兩個實體區塊，依序寫入第 1 塊與第 2 塊（常搭配 NVRAM 加速），確保 Partial Failure 後可恢復一致狀態。

## 相關頁面

- 核心概念：[[mass-storage-and-raid]]
- 跨文比較：[[os-9thed-vs-10thed-evolution]]、[[single-node-os-vs-wsc-storage-and-scheduling]]
- 延伸閱讀：[[Silberschatz2018-OS-10thEd]]、[[Barroso2026-WSC-4thEd]]
