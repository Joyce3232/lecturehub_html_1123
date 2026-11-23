---
title: "Borg"
type: entity
source_type: mixed
raw_file:
  - "raw/docs/Barroso2026-WSC-4thEd.pdf"
source_url: "https://doi.org/10.1007/978-3-031-99489-0"
source_date: "2026-01-01"
ingested_at: "2026-11-22"
status: active
tags:
  - cluster-management
  - scheduling
  - google
---

# Borg

## 核心結論（Key Takeaways）

1. **Google WSC 的叢集作業系統**：[[borg|Borg]] 負責在 10–30 MW、數萬台伺服器的 Cluster / Cell 中進行任務排程、資源分配（Bin Packing）與故障自動重啟。
2. **混合工作負載共置提升利用率**：透過 SLO 分級與 Affinity / Anti-affinity 規則，將高優先級的 Online 服務與可搶占的 Batch 任務共置，支撐 Google 機隊約 50% 的平均 CPU 利用率。
3. **Kubernetes 與 Multi-Arena 安全的基石**：Borg 的設計經驗直接催生了 Kubernetes 與 Cloud Run，並在現代異質伺服器中負責對 CPU、GPU、BMC 與 SmartNIC 執行遠端認證（Attestation）。

## 核心機制（依據 [[Barroso2026-WSC-4thEd]]）

- **排程與裝箱（Bin Packing）**：在考量 CPU、記憶體、磁碟與加速器拓撲的同時，透過 Platform-aware 排程提升 7%–10% 效能與 $2\times$ 加速器利用率。
- **SLO 分級管理**：管理 HALO、HALS、HALT、MALS/MALT、WALS/WALT 到 BE（Best-Effort / Preemptible）等多層級服務品質。
- **電力與熱管理整合**：配合 [[software-defined-infrastructure|SDI]] 中的 Autopilot 與 Thunderbolt，在電力尖峰時動態調整低優先級任務。

## 相關頁面

- 來源：[[Barroso2026-WSC-4thEd]]
- 相關概念：[[warehouse-scale-computers]]、[[software-defined-infrastructure]]
