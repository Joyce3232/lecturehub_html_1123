---
title: "Spanner"
type: entity
source_type: mixed
raw_file:
  - "raw/docs/Barroso2026-WSC-4thEd.pdf"
source_url: "https://doi.org/10.1007/978-3-031-99489-0"
source_date: "2026-01-01"
ingested_at: "2026-11-22"
status: active
tags:
  - distributed-database
  - consistency
  - google
---

# Spanner

## 核心結論（Key Takeaways）

1. **全球分散式強一致性資料庫**：[[spanner|Spanner]] 結合關聯式 SQL 介面、跨洲水平擴展能力與外部強一致性（External Consistency），突破傳統關聯式資料庫與 NoSQL 的二分法。
2. **TrueTime 硬體時鐘同步**：透過 GPS 接收器與原子鐘提供具明確誤差上界的不確定時間區間 $[earliest, latest]$，使分散式交易無需跨區通訊即可確定全域順序。
3. **極致高可用性**：在跨 Region / Zone 部署與 Paxos 複製下，達成 `99.999%`（Five-nines）的服務等級目標（SLO）。

## 關鍵技術細節（依據 [[Barroso2026-WSC-4thEd]]）

- **CAP 理論定位**：理論上屬於 CP 系統（在網路分區時優先保證一致性），但仰賴 Google 私有廣域網路（B4）與高冗餘基礎設施，實務上表現接近 CA。
- **核心應用場景**：支撐 Gmail（超過 100 座 Spanner 資料庫搭配 Blobstore，使用 Paxos Leader Placement 與 Consistent Hashing）及 Google 內部核心交易與雲端服務。
- **底層儲存**：建構於 [[colossus|Colossus]] 之上，並透過加密與多區域複製確保資料耐久性。

## 相關頁面

- 來源：[[Barroso2026-WSC-4thEd]]
- 相關概念：[[warehouse-scale-computers]]
- 相關實體：[[colossus]]、[[borg]]
