---
title: "OS 9th Ed. (2013) vs. 10th Ed. (2018) 教材演進與差異比較"
type: comparison
source_type: mixed
raw_file:
  - "raw/docs/OS-ch06.pdf"
  - "raw/docs/OS-ch07.pdf"
  - "raw/docs/OS-ch08.pdf"
  - "raw/docs/Abraham-Silberschatz-Operating-System-Concepts-10th-2018.pdf"
source_url: ""
source_date: "2018-01-01"
ingested_at: "2026-11-23"
status: active
tags:
  - comparison
  - operating-systems
  - curriculum-evolution
---

# OS 9th Ed. (2013) vs. 10th Ed. (2018) 教材演進與差異比較

## 核心結論（Key Takeaways）

1. **淘汰過時硬體假設**：第十版（[[Silberschatz2018-OS-10thEd]]）正式移除 **Segmentation** 專節，並將 Swapping 從「整支 Process 換出」改為現代 OS 實際採用的 **Page Swapping**。
2. **儲存介面轉向 NVM 與雲端**：第九版投影片（[[Silberschatz2013-OS-Ch08-MassStorage]]）仍以 HDD Seek 排程為主角；第十版則大幅精簡傳統磁碟排程，新增 **NVM/SSD Scheduling**、**Cloud Storage** 與 **Object Storage**。
3. **擁抱現代多核心、容器與 ARM64**：第十版大幅擴充 ARMv8 64-bit、NUMA 記憶體配置、Compressed Memory、Docker / Kubernetes 與 Unikernels。

## 跨版本對照矩陣

| 主題領域 | 9th Edition (2013) 投影片（Ch 06–08） | 10th Edition (2018) 教科書 | 演進脈絡 |
| :--- | :--- | :--- | :--- |
| **記憶體管理** | 獨立講授 **Segmentation**（STBR/STLR）與 Process Swapping（[[Silberschatz2013-OS-Ch06-Memory]]） | **移除 Segmentation**；改講 Page Swapping 與 ARMv8 64-bit（Ch 9） | 現代 64-bit OS 全面以 Flat Paging 為主 |
| **虛擬記憶體** | 聚焦基本 Demand Paging、FIFO/OPT/LRU 與 Working-Set（[[Silberschatz2013-OS-Ch07-VirtualMemory]]） | 新增 **NUMA 配置**、**Compressed Memory**、Major/Minor Page Faults（Ch 10） | 因應多插槽伺服器與行動裝置記憶體壓縮 |
| **大量儲存** | 詳述 FCFS / SSTF / SCAN / C-SCAN / LOOK / C-LOOK 磁碟排程（[[Silberschatz2013-OS-Ch08-MassStorage]]） | **精簡 HDD 排程**；新增 **NVM Scheduling**、Cloud & Object Storage（Ch 11） | NVMe SSD 普及使機械磁頭尋道最佳化退居次要 |
| **虛擬化與雲端** | 偏重傳統 Type-1 / Type-2 VMs | 新增 **Containers、Docker、Kubernetes** 與 Unikernels（Ch 18） | 銜接 [[warehouse-scale-computers|WSC]] 容器化部署趨勢 |

> [!warning] 觀點衝突與版本取代
> - **來源 A（[[Silberschatz2013-OS-Ch06-Memory]]）**：將 Segmentation 與 Contiguous Allocation / Process Swapping 列為核心記憶體管理策略。
> - **來源 B（[[Silberschatz2018-OS-10thEd]] Ch 9）**：明確於改版序言指出已**淘汰 Segmentation 教學**，且 Swapping 改以 **Page** 為單位而非整個 Process。
> - **差異脈絡**：源自 2013 年至 2018 年間 64-bit 平坦定址與虛擬化硬體支援的普及，準備現代系統設計時應以第十版為準，考試或歷史對照則參考第九版投影片。

## 相關頁面

- 來源：[[Silberschatz2013-OS-Ch06-Memory]]、[[Silberschatz2013-OS-Ch07-VirtualMemory]]、[[Silberschatz2013-OS-Ch08-MassStorage]]、[[Silberschatz2018-OS-10thEd]]
- 概念：[[virtual-memory-and-paging]]、[[mass-storage-and-raid]]
