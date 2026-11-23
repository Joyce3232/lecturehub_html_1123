---
title: "Software-Defined Infrastructure (SDI)"
type: concept
source_type: mixed
raw_file:
  - "raw/docs/Barroso2026-WSC-4thEd.pdf"
source_url: "https://doi.org/10.1007/978-3-031-99489-0"
source_date: "2026-01-01"
ingested_at: "2026-11-22"
status: active
tags:
  - sdi
  - sdn
  - resource-management
  - optimization
---

# Software-Defined Infrastructure (SDI)

## 核心結論（Key Takeaways）

1. **計算、網路、儲存全面軟體定義化**：[[software-defined-infrastructure|SDI]] 將傳統靜態硬體配置轉變為可程式化、可動態調度的資源池，是 [[warehouse-scale-computers|WSC]] 提升整體效率的核心手段。
2. **軟硬體調優帶來顯著免費算力（Fleet-wide Gains）**：透過 AutoFDO（$+10\%\text{–}15\%$）、Hugepage-aware TCMalloc（效能 $+7.7\%$、碎片 $-26\%$）與平台感知排程（加速器利用率 $2\times$），無須更換硬體即可釋放大量資源。
3. **動態電力封頂釋放機房冗餘空間**：Thunderbolt 雙閾值 Power Capping 技術提供 9%–25% 的 Power Oversubscription 空間，讓資料中心在相同供電容量下容納更多伺服器。

## 四大支柱

依據 [[Barroso2026-WSC-4thEd]]（Chapter 7）：
1. **Software-Defined Servers (SDS)**：包含 Limoncello MSR 暫存器調校、Heracles 延遲敏感服務隔離、Tiered Memory（基於 MRC/MPKI 曲線）與 H2O-NAS。
2. **Software-Defined Networking (SDN)**：基於 OpenFlow、P4、OpenConfig、SAI 與 SONiC；在資料中心內部（Jupiter WCMP 流量工程）與廣域骨幹（BwE、B4、Protective ReRoute、Espresso）實現集中控制與快速繞道。
3. **Software-Defined Storage**：以 [[colossus|Colossus]] 統一儲存層為核心，將容量（Bytes）與 IOPS 計費解耦，並提供透明 SSD 快取與位置無關的冷儲存。
4. **AI 驅動資源與電力調度**：結合 Autopilot（自動垂直/水平資源調整）、Autocap 與 Thunderbolt 電力封頂，以及 AlphaChip 進行晶片實體佈局最佳化。

## 相關頁面

- 來源：[[Barroso2026-WSC-4thEd]]
- 相關概念：[[warehouse-scale-computers]]、[[tail-latency]]、[[power-usage-effectiveness]]
- 相關實體：[[borg]]、[[colossus]]
