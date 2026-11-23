---
title: "Tail Latency 與 Hedged Requests"
type: concept
source_type: mixed
raw_file:
  - "raw/docs/Barroso2026-WSC-4thEd.pdf"
source_url: "https://doi.org/10.1007/978-3-031-99489-0"
source_date: "2026-01-01"
ingested_at: "2026-11-22"
status: active
tags:
  - latency
  - distributed-systems
  - reliability
---

# Tail Latency 與 Hedged Requests

## 核心結論（Key Takeaways）

1. **大規模扇出放大長尾效應**：在 [[warehouse-scale-computers|WSC]] 的分散式架構中，單一外部請求往往需平行查詢數十至數百台伺服器（Fan-out），使極少數節點的慢回應主導整體使用者體驗。
2. **機率放大效應不可忽視**：即使單台伺服器僅有 1% 機率出現慢回應，在 100 台並發查詢下，整體請求落入長尾延遲的機率將暴增至 63%。
3. **以 Hedged Requests 換取確定性**：透過對超過預期延遲門檻的請求發出備援複本（Hedged Requests），可在極低額外算力開銷下大幅壓低 p99 延遲。

## 數學推導

依據 [[Barroso2026-WSC-4thEd]]（Chapter 3），假設單一葉節點伺服器出現延遲超過 $1\text{ s}$ 的離群機率為 $p = 0.01$（1-in-100 outlier），當一個請求必須等待 $n = 100$ 台伺服器全部回傳時，至少有一台伺服器延遲超過 $1\text{ s}$ 的機率為：

$$P(\text{latency} > 1\text{ s}) = 1 - (1 - p)^n = 1 - (1 - 0.01)^{100} \approx 0.634 \ (63\%)$$

## 緩解策略

- **Hedged Requests**：在初始請求發出後若超過短期延遲門檻（例如 p95 延遲）仍未回傳，立即向另一副本節點發送相同請求，並取最快回傳者。
- **Canary 與 Query of Death (QoD) 防護**：避免單一異常查詢同時擊垮多個副本節點。
- **微架構與排程隔離**：結合 [[software-defined-infrastructure|SDI]] 中的 Heracles 與 Intel CAT/RDT，降低共置工作負載（Co-located Workloads）造成的快取與頻寬干擾。

## 相關頁面

- 來源：[[Barroso2026-WSC-4thEd]]
- 相關概念：[[warehouse-scale-computers]]、[[software-defined-infrastructure]]
