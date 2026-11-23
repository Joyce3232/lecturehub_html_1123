---
title: "Scale-Up vs. Scale-Out"
type: concept
source_type: mixed
raw_file:
  - "raw/docs/Barroso2026-WSC-4thEd.pdf"
source_url: "https://doi.org/10.1007/978-3-031-99489-0"
source_date: "2026-01-01"
ingested_at: "2026-11-22"
status: active
tags:
  - architecture
  - scalability
  - modeling
---

# Scale-Up vs. Scale-Out

## 核心結論（Key Takeaways）

1. **大規模叢集下 Scale-Out 逼近 Scale-Up 效能**：當總核心數超過 2,000 cores 時，大量低階伺服器（Scale-Out）與少數高階 SMP 伺服器（Scale-Up）的整體執行時間差距縮小至約 5% 以內，但成本優勢明顯偏向 Scale-Out。
2. **通訊延遲與本地計算比例決定收斂點**：跨節點網路延遲（微秒級）與節點內記憶體存取延遲（奈秒級）的落差，是決定系統擴展效率的關鍵參數。
3. **Brawny vs. Wimpy Cores 需視工作負載而定**：ARM Neoverse V2（Google Axion）與 AWS Graviton 透過 `1 vCPU = 1 Physical Core` 搭配減半每核心 DRAM 容量，可節省 20%–25% 伺服器硬體成本。

## 效能分析模型

依據 [[Barroso2026-WSC-4thEd]]（Chapter 6），若單次請求基礎執行時間為 $1\text{ ms}$，且有比例 $f$ 的時間需在總數為 $N$ 的伺服器之間進行遠端存取（本地存取延遲 $100\text{ ns}$、跨伺服器網路存取延遲 $100\ \mu\text{s}$），則執行時間模型為：

$$\text{time} = 1\text{ ms} + f \cdot \left(\frac{1}{N} \cdot 100\text{ ns} + \frac{N-1}{N} \cdot 100\ \mu\text{s}\right)$$

此模型顯示：當規模突破數千核心（例如比較 512 台低階伺服器 vs. 16 台 128-core SMP）時，$\frac{N-1}{N}$ 在兩者之間皆趨近於 1，使多台通用型伺服器的系統性價比（Perf/TCO）大幅勝出。

## 相關頁面

- 來源：[[Barroso2026-WSC-4thEd]]
- 相關概念：[[warehouse-scale-computers]]、[[tail-latency]]
