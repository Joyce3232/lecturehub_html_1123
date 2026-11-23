---
title: "Tensor Processing Unit (TPU)"
type: entity
source_type: mixed
raw_file:
  - "raw/docs/Barroso2026-WSC-4thEd.pdf"
source_url: "https://doi.org/10.1007/978-3-031-99489-0"
source_date: "2026-01-01"
ingested_at: "2026-11-22"
status: active
tags:
  - ai-accelerator
  - tpu
  - hardware-architecture
  - google
---

# Tensor Processing Unit (TPU)

## 核心結論（Key Takeaways）

1. **為深度學習矩陣運算而生的 ASIC**：[[tensor-processing-unit|TPU]] 以脈動陣列（Systolic Array）MXU 取代傳統 CPU 快取階層，將每瓦效能（Perf/W）提升至通用 CPU 的數十倍（TPUv1 達系統級 $34\times$、晶片級 $83\times$）。
2. **晶片間直連與光學電路交換（OCS）**：透過 3D Torus ICI（$4 \times 4 \times 4$ Cubes）與 MEMS 反射鏡 OCS，在 TPUv7 單一 Pod 可擴展至 9,216 顆晶片，無需傳統乙太網路交換器瓶頸。
3. **推動資料中心機櫃與液冷革命**：高密度 AI Pod 使單機櫃功耗從傳統 10–30 kW 推升至 50–200 kW，自 TPUv3 起全面導入銅製冷板液冷（Copper Cold Plates + CDU）。

## 微架構與系統演進（依據 [[Barroso2026-WSC-4thEd]]）

- **核心運算單元**：
  - **MXU（Matrix Multiply Unit）**：$256 \times 256$ Systolic Array，達成高達 $256\times$ 的運算元重用（Operand Reuse），原生支援 `bf16` 及新一代 `fp8`、`fp4`、`ocp-mx` 數值格式。
  - **VPU（Vector Processing Unit）**：$128 \times 8$ 向量處理器搭配晶片上 `vmem`。
  - **SparseCore**：針對推薦系統等高維稀疏 Embedding 工作負載最佳化。
  - **HBM 與 ICI Router**：高頻寬記憶體與晶片間互連路由器。
- **能效與電源挑戰**：大型 ML 訓練會產生 15–50 MW 等級的劇烈功率擺盪，可透過編譯器層級排程平滑約 50% 的功率波動。

## 相關頁面

- 來源：[[Barroso2026-WSC-4thEd]]
- 相關概念：[[warehouse-scale-computers]]、[[power-usage-effectiveness]]
- 相關實體：[[borg]]
