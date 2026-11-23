---
title: "Mass Storage, Disk Scheduling & RAID"
type: concept
source_type: mixed
raw_file:
  - "raw/docs/OS-ch08.pdf"
  - "raw/docs/Abraham-Silberschatz-Operating-System-Concepts-10th-2018.pdf"
  - "raw/docs/The Data Center as a Computer Designing Warehouse-Scale Machines Book Open Access © 2026.pdf"
source_url: ""
source_date: "2026-01-01"
ingested_at: "2026-11-23"
status: active
tags:
  - mass-storage
  - raid
  - disk-scheduling
  - zfs
  - nvme
---

# Mass Storage, Disk Scheduling & RAID

## 核心結論（Key Takeaways）

1. **機械硬碟延遲公式決定排程設計**：HDD 的隨機存取受制於 Seek Time 與 Rotational Latency（$\approx 9\text{–}10\text{ ms}$），因此傳統 OS 發展出 SSTF、SCAN、C-SCAN 與 C-LOOK 來最小化磁頭移動距離。
2. **NVM/SSD 改變排程邏輯**：因無機械移動部件，SSD/NVM 消除 Seek 與旋轉延遲，第十版教科書（[[Silberschatz2018-OS-10thEd]]）將硬碟排程精簡並新增 NVM Scheduling。
3. **從傳統 RAID 到分散式糾刪碼**：單機依賴 RAID（0/1/5/6/1+0）與 ZFS 樹狀 Checksums 防錯；而在 [[warehouse-scale-computers|WSC]] 中則演進為 [[colossus|Colossus]] Client-Side Reed-Solomon $RS(k,m)$ 與 Diskless + Flash Appliances。

## 核心公式

- **HDD 平均 I/O 時間**（[[Silberschatz2013-OS-Ch08-MassStorage]]）：
  $$\text{Average I/O Time} = \text{Avg Seek} + \text{Avg Rotational Latency} + \frac{\text{Transfer Size}}{\text{Transfer Rate}} + \text{Controller Overhead}$$
- **RAID 1 鏡像雙碟 MTTDL**：
  $$\text{MTTDL} = \frac{\text{MTTF}^2}{2 \times \text{MTTR}}$$

## 相關頁面

- 來源：[[Silberschatz2013-OS-Ch08-MassStorage]]、[[Silberschatz2018-OS-10thEd]]、[[Barroso2026-WSC-4thEd]]
- 跨文比較：[[os-9thed-vs-10thed-evolution]]、[[single-node-os-vs-wsc-storage-and-scheduling]]
- 相關實體：[[colossus]]
