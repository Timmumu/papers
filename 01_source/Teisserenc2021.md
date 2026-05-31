---
ref: ""
citekey: "Teisserenc2021"
title: "Adoption of blockchain technology through digital twins in the construction industry 4.0: A PESTELS approach"
authors: "Benjamin Teisserenc, Samad Sepasgozar"
year: 2021
journal: "Buildings"
doi: "10.3390/buildings11120670"
zotero_key: "EN7S2R5T"
zotero_status: verified
last_verified: "2026-06-01"
tags:
  - Verified
  - Digital-Twin
  - Blockchain
  - Construction-4.0
---
CiteKey: "Teisserenc2021"
tags: [literature_review, "blockchain", "digital_twins", "construction_industry"]
Critique_Labels: 
   - "(+)Full-Life-Cycle"
   - "(!)Implementation-Gap"
1. **tags**: #literature_review #blockchain #digital_twins #construction_industry
2. **Critique_Summary**: Proposes a novel framework (DDTC) for blockchain-DT integration but lacks empirical validation.
3. **Research Method**: 
   - "Qualitative"
   - "PESTELS analysis, literature review, technical content analysis"
4. **Core Argument**: "BCT-DT integration can solve trust, efficiency, and lifecycle management challenges in construction."
5. **Main Contribution**: 
   - **Theoretical**: DDTC framework for BCT-DT integration.
   - **Methodological/Technical**: Identifies blockchain protocols (e.g., Ethereum, IPFS) for DT.
   - **Practical**: Solutions for Industry 4.0 trust and sustainability.
6. **Research Gap Filled**: "Addresses technical and integration gaps in BCT for construction (Technical/Integration Gaps)."
7. **Limitation of this study**: "No empirical validation; scalability/privacy issues unresolved."
8. **Cross-Lifecycle Critique Matrix**:
   - **Depth**: Concept-only (!)
   - **Lifecycle**: Full-Life-Cycle (+)
   - **DfX Focus**: Integrated (+)
   - **Rigor**: Data-void (!)
   - **Status**: Seminal-Framework (+)

---

### **詳細結構化評審 (繁體中文)**
**1. 核心要素提取 (CiteKey, Method, Argument, etc.)**
- 方法論：採用 PESTELS 分析框架，定性文獻綜述，區塊鏈技術現狀內容分析。
- 核心論點：區塊鏈與數字孿生整合可解決建築行業的信任、效率與數據完整性問題。
- 貢獻：提出 DDTC 理論框架，識別關鍵技術組件（如以太坊、IPFS），提供產業應用路徑。
**2. 五大跨生命週期評價矩陣 (Critique Matrix)**
- **實踐深度**：純理論推導（!），缺乏實證驗證。
- **生命週期集成**：完整覆蓋設計-建造-運維全周期（+），但未驗證跨階段數據流可行性。
- **質量與安全設計**：整合 DfQ（數據完整性）與 DfS（網絡安全）（+）。
- **方法論嚴謹性**：基於文獻分析，無實測數據支持（!）。
- **學術地位與邏輯**：開創性框架研究（+），但技術可行性未驗證。
**3. 研究空白與局限區分 (Gap vs Limitation)**
- **填補空白**：明確指出區塊鏈在建築行業的技術性缺口（如存儲限制、物聯網認證）。
- **存在局限**：未解決實際部署中的擴展性問題和 GDPR 合規挑戰。
**4. 總結與展望**
- 該研究為區塊鏈在建築工業的應用提供理論基礎，但需後續實證研究驗證 DDTC 框架的可行性。未來可結合實測數據優化區塊鏈共識機制與隱私保護設計。

---
### 它回避/未解决的问题 (Gaps & Limitations)

你可以利用这些“被回避的问题”来作为你论文的 **Research Gap（研究空白）**，从而凸显你研究的价值：

1. **缺乏技术实现路径（How-to Implementation）**：
    - **问题**：文章停留在“分析层面”，并没有给出一个具体的**系统架构图**。
    - **你的机会**：你的研究可以填补这个空白，提出一个基于语义（Boje）和去中心化逻辑的具体 FLC 框架。
    
2. **回避了“数据爆炸”与区块链性能的冲突**：
    - **问题**：文章讨论了区块链的好处，但**回避了**如何在区块链上处理数字孪生产生的海量实时数据（存储成本和延迟问题）。
    - **你的机会**：你可以提出你刚才想到的“链上验证+链下存储”的**混合架构（Hybrid Architecture）**。
        
3. **对“人的因素”挖掘不足**：
    - **问题**：虽然提到了社会因素，但它没有深入探讨 **Flyvbjerg 提到的“战略性误报（Strategic Misrepresentation）”** 这种深层心理博弈。它更多是在谈宏观的“行业采纳度”。
    - **你的机会**：你可以将该文的 PESTELS 框架与 Flyvbjerg 的项目失败理论结合，探讨技术如何真正约束人的不诚信行为。
        
4. **缺乏实证案例验证（Validation）**：
    - **问题**：该研究主要是文献综述和定性分析，缺乏真实工程项目的测试。
    - **你的机会**：如果你能结合香港的 **Smart Contract/DWSS** 实践，你的论文就会比它更有说服力。

### 建议在你的 Obsidian 中这样标注：

- **引用位置**：在谈论“为什么要用区块链解决 DT 的信息管理”时引用此文。
    
- **批判性笔记**：_"Teisserenc & Sepasgozar (2021) identified the macro-level barriers via PESTELS, but failed to address the micro-level data friction and the technical trade-offs between blockchain latency and DT real-time requirements."_