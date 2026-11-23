---
title: "PUE、TPUE 與 WUE 能源效率指標"
type: concept
source_type: mixed
raw_file:
  - "raw/docs/Barroso2026-WSC-4thEd.pdf"
source_url: "https://doi.org/10.1007/978-3-031-99489-0"
source_date: "2026-01-01"
ingested_at: "2026-11-22"
status: active
tags:
  - energy-efficiency
  - sustainability
  - pue
  - wue
---

# PUE、TPUE 與 WUE 能源效率指標

## 核心結論（Key Takeaways）

1. **設施 PUE 已逼近物理極限**：Google 追蹤 12 個月平均 PUE 已達 `1.09`（新加坡熱帶氣候達 `1.13`），代表供電與冷卻損耗僅佔總用電不到 9%，未來節能重心轉向 `SPUE` 與伺服器運算利用率。
2. **全系統能效（TPUE）涵蓋電源轉換損耗**：僅看 PUE 會忽略伺服器內部 PSU 與 VRM 的轉換損耗；Google 的 $\text{TPUE}$ 已從 2005 年的 `3.2` 改善至約 `1.35`。
3. **水資源與碳排納入核心設計約束**：用水效率 $\text{WUE}$ 與小時級無碳能源（Hourly CFE，Google 2023 年達 64%）及 Scope 3 隱含碳（LC3 混凝土、Mass Timber）共同構成新一代資料中心永續標準。

## 核心數學定義

依據 [[Barroso2026-WSC-4thEd]]（Chapter 9），[[warehouse-scale-computers|WSC]] 整體運算能源效率拆解為：

$$\text{Efficiency} = \frac{1}{\text{PUE}} \cdot \frac{1}{\text{SPUE}} \cdot \frac{\text{Computation}}{\text{Energy To Components}}$$

各項關鍵指標定義如下：

$$\text{PUE} = \frac{\text{Facility Power}}{\text{IT Equipment Power}}, \quad \text{TPUE} = \text{PUE} \times \text{SPUE}$$

$$\text{WUE} = \frac{\text{Water Usage (L)}}{\text{IT Energy Usage (kWh)}}$$

其中 $\text{SPUE}$（Server PUE）衡量伺服器機箱內部電源供應器（PSU）、電壓調節模組（VRM）與風扇的額外損耗。

## Power Oversubscription 容量增益

由於大規模叢集極少同時達到 100% 額定功耗（例如某 5,000 台伺服器叢集尖峰僅達 72% 額定功率，餘裕 $u = 0.28$），透過軟體電力封頂可安全超額配置伺服器數量：

$$\text{Capacity Gain} = \frac{1}{1 - 0.28} = 1.39\times$$

Google 在 MVPP 供電架構上實務採用約 25% 的 Power Oversubscription。

## 相關頁面

- 來源：[[Barroso2026-WSC-4thEd]]
- 相關概念：[[warehouse-scale-computers]]、[[software-defined-infrastructure]]
