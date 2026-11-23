---
title: "Operating System Concepts (10th Edition)"
type: source
source_type: docs
raw_file: "raw/docs/Abraham-Silberschatz-Operating-System-Concepts-10th-2018.pdf"
source_url: "https://www.os-book.com/"
source_date: "2018-01-01"
ingested_at: "2026-11-23"
status: active
tags:
  - operating-systems
  - process-management
  - synchronization
  - virtual-memory
  - storage-systems
  - virtualization
---

# Operating System Concepts (10th Edition)

- **作者**：Abraham Silberschatz、Peter Baer Galvin、Greg Gagne
- **出版資訊**：John Wiley & Sons, Inc., 2018（Tenth Edition，全書共 1,278 頁，含 21 章與 4 篇附錄）

## 核心結論（Key Takeaways）

1. **作業系統是硬體資源管理者與抽象層**：OS 透過 Process/Thread、[[virtual-memory-and-paging|Virtual Memory]]、File System 與 I/O Subsystem，將有限的物理資源安全且高效率地分配給多工程式。
2. **多核心與並行同步成為核心挑戰**：面對 Multicore 時代，[[process-synchronization-and-deadlocks|Process Synchronization]]（Peterson's Solution、Atomic Hardware Instructions、Mutex、Semaphore、Monitor）與 Deadlock 防治決定系統正確性與可擴展性。
3. **第十版順應現代硬體與雲端典範轉移**：移除傳統 Segmentation 與過時磁碟排程，改以 Page Swapping、NUMA 記憶體配置、Compressed Memory、NVM/SSD Scheduling、Cloud/Object Storage 與 Containers / Kubernetes（Ch 18）為現代重點。
4. **安全與虛擬化深度整合**：擴充 Mandatory Access Control (MAC)、Linux Capabilities、ARM TrustZone、Type-1/Type-2 Hypervisors 與 Unikernels，與現代 [[warehouse-scale-computers|WSC]] 基礎設施直接銜接。

---

## 全書十大單元架構與關鍵公式

### Part 1：Overview（Ch 1–2）
- 涵蓋 OS 定義、中斷驅動（Interrupt-driven）架構、Dual-Mode Operation（User Mode vs. Kernel Mode）、System Calls、Linkers & Loaders、GRUB 開機與 BCC 除錯工具組。

### Part 2：Process Management（Ch 3–5）
- **Ch 3 Processes**：Process Control Block (PCB)、Context Switch、`fork()` / `exec()`、Shared-Memory 與 Message-Passing IPC（Mach、Android RPC）、`systemd`。
- **Ch 4 Threads & Concurrency**：Multithreading Models（Many-to-One、One-to-One、Many-to-Many）、Pthreads、Windows/Java Threads、Implicit Threading（Thread Pools、Fork-Join、OpenMP、Apple GCD + Swift、Intel TBB）。
- **Ch 5 CPU Scheduling**：排程準則（CPU Utilization、Throughput、Turnaround Time、Waiting Time、Response Time）；演算法涵蓋 FCFS、SJF/SRTF、Round-Robin、Multilevel Feedback Queue、CFS（Linux）、NUMA-aware Load Balancing 與 Real-Time（Rate-Monotonic、EDF）。
  - 指數平均預測下一次 CPU Burst：
    $$\tau_{n+1} = \alpha t_n + (1 - \alpha)\tau_n$$

### Part 3：Process Synchronization（Ch 6–8）
- **Ch 6 Synchronization Tools**：[[process-synchronization-and-deadlocks|Critical-Section Problem]]（Mutual Exclusion、Progress、Bounded Waiting）、Peterson's Solution、硬體原子指令（`test_and_set`、`compare_and_swap`）、Mutex Locks、Semaphores、Monitors 與 Liveness。
- **Ch 7 Synchronization Examples**：Bounded-Buffer、Readers-Writers、Dining-Philosophers、POSIX/Java 同步機制與 Transactional Memory。
- **Ch 8 Deadlocks**：四大必要條件（Mutual Exclusion、Hold and Wait、No Preemption、Circular Wait）、Resource-Allocation Graph、Banker's Algorithm（Safe State 判定）。

### Part 4：Memory Management（Ch 9–10）
- **Ch 9 Main Memory**：[[virtual-memory-and-paging|Contiguous Allocation]]、Paging、TLB 與 Effective Access Time (EAT)、Hierarchical / Hashed / Inverted Page Tables、Page Swapping（第十版移除 Segmentation）、Intel x86-64 與 ARMv8 實例。
- **Ch 10 Virtual Memory**：Demand Paging、Copy-on-Write (COW)、Page Replacement（FIFO、OPT、LRU、Clock）、NUMA Frame Allocation、Thrashing、Working-Set Model、Compressed Memory、Buddy System 與 Slab Allocator。

### Part 5 & 6：Storage Management & File System（Ch 11–15）
- **Ch 11 Mass-Storage Structure**：[[mass-storage-and-raid|HDD 與 NVM (Flash/SSD) 排程]]、Error Detection/Correction、RAID（0/1/4/5/6/0+1/1+0）、Cloud Storage 與 Object Storage。
- **Ch 12 I/O Systems**：Polling / Interrupt / DMA、Blocking vs. Nonblocking / Asynchronous I/O、Vectored I/O。
- **Ch 13–15 File Systems**：Access Methods、Directory Structure、Allocation Methods（Contiguous、Linked、Indexed）、WAFL、VFS 與 NFS。

### Part 7 & 8：Security, Virtualization & Distributed Systems（Ch 16–19）
- **Ch 16–17 Security & Protection**：密碼學基礎、認證、Protection Rings、Access Matrix、RBAC、MAC、ARM TrustZone 與 Sandboxing。
- **Ch 18 Virtual Machines**：Trap-and-Emulate、Binary Translation、Hardware-assisted Virtualization（Intel VT-x / AMD-V）、Containers（Docker、Kubernetes）與 Unikernels。
- **Ch 19 Networks & Distributed Systems**：TCP/IP、Naming、Distributed File Systems 與一致性語意（可與 [[Barroso2026-WSC-4thEd]] 深度對照）。

### Part 9 & 10：Case Studies & Appendices（Ch 20–21, App A–D）
- 深入剖析 Linux（CFS 排程、Slab、ext4）、Windows 10、BSD UNIX 與 Mach。

## 相關頁面

- 課程投影片對照（第九版）：[[Silberschatz2013-OS-Ch06-Memory]]、[[Silberschatz2013-OS-Ch07-VirtualMemory]]、[[Silberschatz2013-OS-Ch08-MassStorage]]
- 跨文比較：[[os-9thed-vs-10thed-evolution]]、[[single-node-os-vs-wsc-storage-and-scheduling]]
- 核心概念：[[virtual-memory-and-paging]]、[[mass-storage-and-raid]]、[[process-synchronization-and-deadlocks]]
