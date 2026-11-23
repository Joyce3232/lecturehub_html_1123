---
title: "Colossus"
type: entity
source_type: mixed
raw_file:
  - "raw/docs/Barroso2026-WSC-4thEd.pdf"
source_url: "https://doi.org/10.1007/978-3-031-99489-0"
source_date: "2026-01-01"
ingested_at: "2026-11-22"
status: active
tags:
  - distributed-storage
  - file-system
  - google
---

# Colossus

## 核心結論（Key Takeaways）

1. **GFS 的次世代演進**：[[colossus|Colossus]] 是 Google [[warehouse-scale-computers|WSC]] 的統一分散式檔案系統，透過分散式 Metadata 架構消除早期 GFS 單一 Master 的擴展瓶頸。
2. **Client-Side 編碼與高可用儲存**：由客戶端直接執行 Reed-Solomon $RS(k, m)$ 糾刪碼或副本寫入網路連接磁碟層 `D`，兼顧高吞吐量與儲存成本。
3. **支撐全棧資料與雲端服務**：作為 BigQuery（搭配 Capacitor 欄式格式）、[[spanner|Spanner]] 與 Google Cloud Storage (GCS) 的底層儲存基石。

## 系統架構（依據 [[Barroso2026-WSC-4thEd]]）

- **Metadata 層**：由 MD1 / MD0 B-trees 搭配 Paxos Curators 管理中繼資料，支援高併發與低延遲的檔案系統操作。
- **資料層 `D`（Network-Attached Disk Layer）**：將儲存與計算解耦，配合 Diskless 伺服器與獨立 Disk/Flash Appliances（400 Gbps NIC 超額訂閱 16 顆 SSD）運作。
- **Software-Defined Storage**：在 [[software-defined-infrastructure|SDI]] 架構下，將容量（Bytes）與 IOPS 計費分離，並支援透明 SSD 快取與位置無關的冷儲存。

## 相關頁面

- 來源：[[Barroso2026-WSC-4thEd]]
- 相關概念：[[warehouse-scale-computers]]、[[software-defined-infrastructure]]
- 相關實體：[[spanner]]、[[borg]]
