---
title: "The Data Center as a Computer: Designing Warehouse-Scale Machines (4th Edition)"
type: source
source_type: docs
raw_file: "raw/docs/The Data Center as a Computer Designing Warehouse-Scale Machines Book Open Access © 2026.pdf"
source_url: "https://doi.org/10.1007/978-3-031-99489-0"
source_date: "2026-01-01"
ingested_at: "2026-11-22"
status: active
tags:
  - warehouse-scale-computing
  - data-center
  - distributed-systems
  - hardware-architecture
  - sustainability
  - tco
  - ai-infrastructure
---

# The Data Center as a Computer: Designing Warehouse-Scale Machines (4th Edition)

- **作者**：Luiz André Barroso (1964–2023)、Urs Hölzle、Parthasarathy Ranganathan（Google LLC）
- **出版資訊**：Springer Nature Switzerland AG, 2026（Open Access, CC BY 4.0），*Synthesis Lectures on Computer Architecture*
- **書目識別碼**：ISSN `1935-3235` / `1935-3243`；ISBN `978-3-031-99488-3` / `978-3-031-99489-0`；[DOI: 10.1007/978-3-031-99489-0](https://doi.org/10.1007/978-3-031-99489-0)

## 核心結論（Key Takeaways）

1. **資料中心即電腦（Data Center as a Computer）**：[[warehouse-scale-computers|Warehouse-Scale Computers (WSC)]] 並非單純的伺服器集合，而是透過軟硬體協同設計（Hardware-Software Co-Design），將數萬至數十萬台伺服器、網路與儲存整合為單一計算實體的系統。
2. **規模驅動自動化與軟體定義基礎設施**：在 5% 年化故障率（Annualized Failure Rate, AFR）下，100,000 台伺服器的叢集平均每 2 小時就會發生一次硬體故障，使得人工維運不再可行，必須依賴 [[borg|Borg]] 等自動化調度與 [[software-defined-infrastructure|Software-Defined Infrastructure (SDI)]] 實現高可用性。
3. **AI/ML 重塑基礎設施與機櫃密度**：AI 訓練與推論工作負載使單機櫃功耗從傳統 10–30 kW 躍升至 50–200 kW，推動液冷（Cold Plates / CDU）、光學電路交換（Optical Circuit Switching, OCS）與 [[tensor-processing-unit|TPU]] 等專用加速器成為主流。
4. **Tail Latency 與 TCO 主導系統設計權衡**：大規模分散式查詢受制於 [[tail-latency|Tail Latency]] 放大效應，需以 Hedged Requests 與容錯編碼（Reed-Solomon）平衡效能與成本；整體經濟效益則由 TCO 模型與「Data Center Tax（約佔 30% 叢集週期）」決定。
5. **能源效率與永續發展進入精細化時代**：Google 追蹤 12 個月平均 [[power-usage-effectiveness|PUE]] 已降至 1.09，進一步節能轉向提升伺服器利用率（Fleet CPU Utilization 約 50%）、Power Oversubscription（約 25%–39% 容量增益）、小時級無碳能源（Hourly CFE）調度與 Scope 3 隱含碳（Embodied Carbon）減量。

---

## 各章節技術摘要與核心公式

### Chapter 1：Introduction
- 區分傳統資料中心（企業代管、異質負載）、[[warehouse-scale-computers|Warehouse-Scale Computers (WSC)]]（單一組織全棧控制、大規模同質/半同質計算）與 Hyperscalers（超大規模雲端服務商）。
- **規模帶來的質變**：以 5% AFR 估算，100 台伺服器約每 2 個月故障 1 次（可人工處理），但 100,000 台伺服器約**每 2 小時故障 1 次**，迫使系統必須假設故障為常態並內建自動復原機制。
- 第四版由原先 8 章擴充至 12 章，新增 AI/ML 基礎設施、機密運算（Confidential Computing）、永續水電指標與過去 25 年 WSC 演進回顧。

### Chapter 2：Overview of WSC Architecture
- **地理階層**：Region（直徑約 50 km）包含 2–3 個 Campus / Availability Zones。GCP 與 AWS 採 3 Zones 設計（單一 Zone 故障容錯需 $1.5\times$ 容量冗餘）；Azure 採 2 Zones 設計（需 $2N$ 容量冗餘）。
- **機櫃與伺服器規格**：標準機櫃單位 $1\text{U} = 1.75\text{ in} = 44.45\text{ mm}$，常見為 42U 機櫃。
- **儲存系統譜系**：DAS vs. NAS；[[colossus|GFS / Colossus / GCS]] 採用 Reed-Solomon 糾刪碼；BigTable / Dynamo 採最終一致性（Eventual Consistency）；[[spanner|Spanner]] 提供 SQL 介面與外部強一致性（External Consistency）。
- **網路拓撲（2025 基準）**：25–50 Tbps 交換器；機櫃內（64 台伺服器）400 Gbps；相鄰機櫃約 100 Gbps；跨 WSC 約 50 Gbps。
- **2024 Google 2-socket x86 伺服器峰值功耗拆解**（768 GB DRAM，80% 利用率）：
  - CPUs：786 W（56.7%）
  - Memory：258 W（18.6%）
  - Power Loss（VRM 與 PDN 的 $I^2R$ 損耗）：223 W（16.1%）
  - Cooling：44.6 W（3.2%）
  - Storage：44 W（3.2%）
  - Networking：30 W（2.2%）

### Chapter 3：Overview of WSC Workloads
- **技術堆疊分層**：Applications（Online vs. Offline）$\to$ Application Frameworks $\to$ Cluster Infrastructure（MapReduce、[[spanner|Spanner]]、[[colossus|Colossus]]、RPC）$\to$ Resource Management（[[borg|Borg]]）$\to$ Platform Software $\to$ Hardware + Monitoring/Tools。
- **雲端服務模型與 SLO 等級**：IaaS（GCE）、PaaS（GKE、Cloud Run、Cloud SQL）、SaaS（Google Workspace）。Google 內部 SLO 分級涵蓋 HALO、HALS、HALT、MALS/MALT、WALS/WALT 與 BE（Spot / Preemptible）。
- **超大規模應用案例**：
  - **Web Search**：索引超過 100,000 TB，日夜尖峰離峰比達 $5\times$。
  - **YouTube**：熱門影片採 2-pass 轉碼，搭配 Edge CDN 分發。
  - **Gmail**：由 100+ 座 [[spanner|Spanner]] 資料庫與 Blobstore 組成，使用 Paxos Leader Placement 與 Consistent Hashing。
  - **AI/ML Workloads**：涵蓋 Pre-training、SFT、RLHF、Distillation 與 Inference-time Compute；數值格式演進至 `bf16`、`fp8`、`fp4` 與 `ocp-mx`；並行策略包含 Data / Model / Pipeline Parallelism。
  - **GCE / BigQuery / Dataflow**：GCE 採用 Titan RoT 驗證啟動、Titanium IPU 分層卸載（Host 端 Titanium Adapter + 遠端 Hyperdisk 代理）與即時遷移（Live Migration：Pre-copy $\to$ 亞秒級 Blackout $\to$ Post-copy）；BigQuery 結合 Dremel、[[colossus|Colossus]] 與 Capacitor 欄式儲存。
- **關鍵系統設計權衡**：
  - 副本數 $N$ vs. $RS(k, m)$ 糾刪碼（Erasure Coding）。
  - Brownouts（降級服務）vs. Blackouts（完全中斷）；Query of Death (QoD) 與 Canary 部署；Chubby / ZooKeeper / etcd 共識服務；先壓縮再加密（Compression before Encryption）。
  - **[[tail-latency|Tail Latency]] 放大**：若單台伺服器有 1% 機率延遲超過 1 秒，對 100 台伺服器平行發起扇出請求（Fan-out）時，整體請求延遲超過 1 秒的機率為：
    $$P(\text{latency} > 1\text{ s}) = 1 - (1 - 0.01)^{100} \approx 63\%$$

### Chapter 4：WSC Software
- **叢集與區域邊界**：Cluster / Cell（10–30 MW，數萬台伺服器）$<$ Zone $<$ Region。
- **[[borg|Borg]]**：負責 Bin Packing 與 Affinity / Anti-affinity 排程；其設計經驗延伸至 Kubernetes 與 Cloud Run。
- **[[colossus|Colossus]]**：由 MD1/MD0 B-trees Metadata、Paxos Curators 與網路連接磁碟層 `D` 組成，採用 Client-side Reed-Solomon / Replication（相較 GCS 透過 API Server 代理）。
- **[[spanner|Spanner]]**：透過 GPS 與原子鐘構成的 `TrueTime` API（回傳不確定區間 $[earliest, latest]$）實現全域外部一致性與 `99.999%` SLO（CAP 理論上屬 CP，實務上接近 CA）。
- **WAN 與邊緣網路**：Anycast DNS（BGP）、Google Global Cache (GGC)、Edge POPs，以及 Cold-potato vs. Hot-potato 路由（超過 98% 流量達成 Single Hand-off）。
- **供應鏈前置期與維運工程**：如 TSMC 5nm 晶圓生產約需 5 個月、變電站建設超過 1 年；導入 IaC（Terraform、Ansible）、SLIs/SLOs/SLAs、Dapper / OpenTelemetry 分散式追蹤、Google-Wide Profiling (GWP)、SRE 無指責事後檢討（Blameless Postmortems）與硬體信任根（Titan、Nitro、OpenTitan、Caliptra）、Intel CAT / RDT 快取隔離。

### Chapter 5：Data Center Infrastructure
- **建置成本與機櫃功率**：資料中心建置成本約 $\$5\text{–}20/\text{W}$，大型園區超過 100 MW；Uptime Institute 分為 Tiers I–IV，且超過 70% 的停機事故源自人為錯誤。ML 機櫃功耗達 50–200 kW（傳統為 10–30 kW），且 ML 訓練因具備 Checkpointing 機制，可容忍接近 Tier-1 等級的電力基礎設施。
- **供電拓撲與效率**：
  - Radial（$N+1$ ATS）vs. Google MVPP（11–15 kV，$N+M$ 發電機組）vs. Distributed Redundant（如 4/3 DR）。
  - AC 供電鏈整體效率約 85%（$97\%\text{ UPS} \times 97\%\text{ PDU} \times 94\%\text{ PSU} \times 96\%\text{ VR}$），DC 供電鏈可達 89%（$99\% \times 98\% \times 96\% \times 96\%$）。
  - 分散式 12V/48V 機櫃內 UPS 損耗僅約 0.1%（傳統集中式為 1%–3%）；Google 已部署超過 1 億顆 Li-ion / LFP 電池芯；ML 訓練會引發 25–50 MW 等級的劇烈功率擺盪。
- **散熱與機械設計**：
  - 25 MW 機房（體積 $25,000\text{ m}^3$）若失去冷卻，室溫將以 $0.8^\circ\text{C/s}$ 攀升，5–15 分鐘內必須觸發緊急斷電（EPO）。
  - 冷卻架構涵蓋 2-loop 與 3-loop（空氣 $\to$ 製程水 $\to$ 冷凝水）、CRACs、冰水主機（Chillers）、自然冷卻（Free Air / Water Economizers，依濕球溫度與乾球溫度設計）、冷卻水塔（1–2°C Approach）、CFD 模擬、熱通道封閉（Hot Aisle Containment）。
  - 晶片功耗超過 200–250 W 時轉向液冷：[[tensor-processing-unit|TPUv3]] 採用銅製冷板（Copper Cold Plates）搭配 CDU，並探索單相/雙相浸沒式冷卻（1P/2P Immersion Cooling）。
  - 模組化建造（Kit-of-Parts、5 Envelopes）與 Rack Mover 機器人（部署速度提升 $5\times$）。

### Chapter 6：Computing Building Blocks
- **[[scale-up-vs-scale-out|Scale-Up vs. Scale-Out]] 效能模型**：
  $$\text{time} = 1\text{ ms} + f \cdot \left(\frac{1}{N} \cdot 100\text{ ns} + \frac{N-1}{N} \cdot 100\ \mu\text{s}\right)$$
  當總核心數超過 2,000 cores 時，512 台低階伺服器與 16 台 128-core SMP 的效能差距縮小至約 5% 以內。
- **Brawny vs. Wimpy Cores**：ARM Neoverse V2（Google Axion）與 AWS Graviton 採用 1 vCPU = 1 Physical Core 設計，將每核心 DRAM 減半可節省 20%–25% 伺服器成本。
- **加速器互連與架構**：
  - [[tensor-processing-unit|TPU]] ICI（$4 \times 4 \times 4$ Cubes 搭配 OCS，TPUv7 單 Pod 可達 9,216 顆晶片）、NVIDIA NVLink（高達 256 GPUs）與 UALink。
  - **Multi-Arena 伺服器安全邊界**：CPU、GPU、BMC 與 SmartNIC 各自作為獨立信任域，由 [[borg|Borg]] 排程器執行遠端認證（Attestation）。
  - **TPU 內部微架構**：MXU（$256 \times 256$ Systolic Array，提供 $256\times$ 運算元重用）、VPU（$128 \times 8$ 搭配 `vmem`）、SparseCore、HBM、ICI Router 與 `bf16`。
  - **專用加速卡**：VCU（Video Coding Unit）在 VP9 轉碼上吞吐量達 CPU 的 $8\times\text{–}20\times$，20 顆 VCU 的 Perf/TCO 達 $33.3\times$；Titanium IPU 基於 Intel E2100（200 Gbps，16 顆 ARM Neoverse N1 核心）。
- **Clos 網路與儲存元件**：
  - $k$-port 交換器構成的三層 Fat-tree Clos 網路可連接 $\frac{k^3}{4}$ 台伺服器，共需 $\frac{5k^2}{4}$ 台交換器；Jupiter 頻寬從 1.3 Pbps 演進至 6.5 Pbps，並採用無 Spine 的 MEMS 反射鏡 OCS 架構。
  - 25 TB HDD 以 200 MB/s 完整讀取需 35 小時（「Disk is the new tape」）；推廣 Diskless 伺服器與獨立 Disk/Flash Appliances（400 Gbps NIC 超額訂閱 16 顆 SSD）。

### Chapter 7：Software-Defined Infrastructure
- **[[software-defined-infrastructure|Software-Defined Infrastructure (SDI)]]**：
  - **Software-Defined Servers (SDS)**：Limoncello MSR 動態調校、Heracles QoS 隔離、AutoFDO（效能 $+10\%\text{–}15\%$）、Hugepage-aware TCMalloc（效能 $+7.7\%$、RAM $-2.4\%$、記憶體碎片 $-26\%$）、Platform-aware 排程（效能 $+7\%\text{–}10\%$、加速器利用率 $2\times$）、Tiered Memory（MRC/MPKI 曲線）與 H2O-NAS。
  - **Software-Defined Networking (SDN)**：OpenFlow、P4、OpenConfig、SAI、SONiC；Jupiter 流量工程（WCMP）、Network-aware 排程、BwE、B4、Protective ReRoute、Espresso、Cloud Armor 與 dSDN。
  - **Software-Defined Storage**：[[colossus|Colossus]] 統一儲存層、容量（Bytes）與 IOPS 分離計費、透明 SSD 快取與位置無關的冷儲存。
  - **電力與晶片設計自動化**：Thunderbolt 雙閾值軟硬節流封頂（Power Capping，帶來 9%–25% 超額訂閱增益）、Autocap、Autopilot 與 AlphaChip 晶片佈局最佳化。

### Chapter 8：Performance & Costs
- **2025 儲存與網路延遲階層**：L1 Cache `1 ns`、L3 Cache `25 ns`、DRAM `80–250 ns`、CXL Far Memory `1 μs`、400 Gbps 傳送 1 MB `20 μs`、SSD 隨機讀取 `80 μs`、HDD 尋道 `10 ms`、美西至荷蘭往返（CA–NL–CA）`150 ms`。
- **Data Center Tax**：RPC、壓縮、序列化與記憶體拷貝等底層開銷約佔全機隊 CPU 週期的 30%。
- **評估與模擬工具**：分層模擬（Core $\to$ SoC $\to$ Node $\to$ Cluster）、Fleetbench、WSMeter（以 GCU 為基準單位）與 Sage。
- **TCO 總擁有成本公式**：
  $$\text{TCO} = \text{DC depreciation} + \text{DC opex} + \text{server depreciation} + \text{server opex}$$
  DC Capex 約 $\$6\text{–}13/\text{W}$（另加場址開發 $\$1\text{–}2/\text{W}$），伺服器採 6 年折舊並計入 NRE。在計入真實 [[power-usage-effectiveness|PUE]]、利用率與軟體授權後，3 年期 On-prem（$\$47,000$）與 GCP（$\$50,500$）TCO 極為接近。

### Chapter 9：Energy & Sustainability
- **系統總能效與 [[power-usage-effectiveness|PUE]] / WUE 公式**：
  $$\text{Efficiency} = \frac{1}{\text{PUE}} \cdot \frac{1}{\text{SPUE}} \cdot \frac{\text{Computation}}{\text{Energy To Components}}$$
  $$\text{PUE} = \frac{\text{Facility Power}}{\text{Equipment Power}}, \quad \text{TPUE} = \text{PUE} \times \text{SPUE}$$
  $$\text{WUE} = \frac{\text{Water Usage (L)}}{\text{Energy Usage (kWh)}}$$
  Google 追蹤 12 個月平均 PUE 達 `1.09`（新加坡為 `1.13`），DeepMind AI 散熱調控降低夏季冷卻額外耗電 40%；TPUE 已從 2005 年的 `3.2` 降至約 `1.35`。WUE 產業平均為 `1.8`，Meta 為 `0.26`、AWS 為 `0.25`（目標 2030 年達成 120% Water Positive）。
- **基準測試與利用率**：SPECpower、MLPerf Power（指標為 `Samples/J` 與 `1/J`）；Google 機隊平均 CPU 利用率約 50%（實務上限約 65%–70%），GCE 約 33.5%。
- **Energy Proportionality 與 Power Oversubscription**：Turbo on Demand 提升 30% 能效；編譯器排程可將 15 MW 的 ML 功率擺盪平滑約 50%；TPUv1 相較 Haswell CPU 達成系統級 $34\times$、晶片級 $83\times$ Perf/W。5,000 台伺服器叢集尖峰僅達額定功率 72%，可提供：
  $$\frac{1}{1 - 0.28} = 1.39\times \text{ 容量增益}$$
  Google 在 MVPP 上實作 25% Power Oversubscription。
- **碳排範疇與 AI 能源經濟學**：Scope 1 僅佔 Google 總排放 1%；Scope 2 於 2023 年達 64% 小時級無碳能源（Hourly CFE）並推動 Carbon-aware 排程；Scope 3 聚焦 LC3 低碳混凝土與 Mass Timber 減碳。2019–2021 年間 AI 佔 Google 總用電 $<15\%$（其中推論約佔 60%）。建置 1 GW AI 資料中心的 6 年 TCO 高達 $\$40\text{–}50\text{B}$，需對應約 $\$100\text{B}$ 的 6 年營收。根據 IEA 統計，全球 ICT 用電佔比為：WSCs 8.5%、其他資料中心 15.8%、使用者終端設備 46.0%、網路基礎設施 27.0%。

### Chapter 10：Trusted Computing
- **可用性與失效分級**：區分 Availability 與 Reliability（MTBF、MTTR、RTO、RPO）；失效嚴重度排序為 `Corrupted > Unreachable > Degraded > Masked`。
- **事故根因與硬體失效率**：68% 的大規模停機源自設定變更（Config）與程式二進位檔推送（Binary Pushes）。Google 2018 年平均每台機器年重啟 12.4 次、平均停機約 10 分鐘（可用度 99.93%）；2024 年年化當機率已降至 $<5\%$。DRAM FIT 約 70–100（採 Chipkill ECC 防護）；SSD P/E 壽命為 SLC 10k+、TLC 3k、QLC 1.5k 次，並受 Write Amplification 與阿瑞尼士定律（Arrhenius Law）斷電資料保存期限制；持續防範靜默資料損毀（Silent Data Corruption, SDC）。
- **安全縱深防禦**：5 項維運實務與 CAPA 流程；6 層實體安全防護（點出 BMS 氣隙隔離在 Stuxnet 等攻擊下的限制）；Titan / OpenTitan / Caliptra 晶片信任根（RoT）；靜態加密（每個資料塊採獨立 DEK AES-256）與傳輸加密（ALTS、TLS）；機密運算（TEE：AMD SEV-SNP、Intel TDX、ARM CCA）；防範 Spectre/Meltdown 側通道攻擊、零信任架構（Zero-Trust）與雙人覆核原則（Two-Person Rule）。

### Chapter 11 & Chapter 12：Retrospective, Future & Top 25 Papers
- 回顧 Google WSC 發展的 **5 個時代（1999–2023）**與 **9 項關鍵教訓**（區分 Roofshots 漸進最佳化與 Moonshots 典範轉移）。
- 展望「Mud to Cloud（從土建到雲端）」與「Chip to Ship（從晶片到整機櫃交付）」的垂直整合趨勢。
- 精選 **Top 25 WSC 經典論文**（自 1998 年 PageRank 至 2022 年 Pathways）。
