---
title: "Warehouse-Scale Computers (WSC)"
type: concept
source_type: mixed
raw_file:
  - "raw/docs/Barroso2026-WSC-4thEd.pdf"
source_url: "https://doi.org/10.1007/978-3-031-99489-0"
source_date: "2026-01-01"
ingested_at: "2026-11-22"
status: active
tags:
  - warehouse-scale-computing
  - architecture
  - reliability
---

# Warehouse-Scale Computers (WSC)

## 核心結論（Key Takeaways）

1. **單一計算實體思維**：WSC 將整座資料中心內的數萬至數十萬台伺服器、網路交換器、儲存與電力冷卻設施視為同一台「電腦」，進行全棧軟硬體協同設計。
2. **規模引發的質變**：當節點規模達到 $10^5$ 等級時，硬體故障從「偶發例外」轉變為「每兩小時發生一次的常態」，必須由軟體層（如 [[borg|Borg]] 與 [[colossus|Colossus]]）自動吸收故障。
3. **跨層次權衡**：WSC 的設計核心在於效能、[[tail-latency|Tail Latency]]、[[power-usage-effectiveness|能源效率]]與總擁有成本（TCO）之間的系統級最佳化。

## 與傳統資料中心及 Hyperscalers 的差異

依據 [[Barroso2026-WSC-4thEd]]（Chapter 1 & 2），WSC 的定位如下：
- **傳統資料中心（Traditional Data Centers）**：主要為企業內部 IT 或客戶代管（Colocation）服務，執行異質且彼此獨立的軟體堆疊，硬體與軟體高度解耦。
- **Warehouse-Scale Computers (WSC)**：由單一組織擁有並全棧控制（從電力、冷卻、伺服器主機板到作業系統與分散式應用框架），能針對特定工作負載進行跨層最佳化。
- **Hyperscalers**：具備多個跨地理區域（Regions 與 Availability Zones）WSC 的超大規模雲端與網路服務供應商（如 Google、AWS、Azure）。

## 故障頻率與自動化需求

假設單台伺服器的年化故障率（Annualized Failure Rate, AFR）為 $5\%$：
- **100 台伺服器規模**：平均每 2 個月出現 1 次硬體故障，仍可仰賴人工維運處理。
- **100,000 台伺服器規模**：平均**每 2 小時出現 1 次硬體故障**，人工介入完全不可行，必須全面依賴自動化叢集排程與分散式容錯儲存。

## 相關頁面

- 來源：[[Barroso2026-WSC-4thEd]]
- 相關概念：[[scale-up-vs-scale-out]]、[[software-defined-infrastructure]]、[[tail-latency]]、[[power-usage-effectiveness]]
- 核心組件：[[borg]]、[[colossus]]、[[spanner]]、[[tensor-processing-unit]]
