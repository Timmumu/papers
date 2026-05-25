# Zotero Fulltext Verification Prompt

Use this prompt to ask Copilot to verify literature review entries against actual PDFs in Zotero:

---

**Copy-paste prompt:**

> Verify the literature review matrix (`MD/LR_Matrix.md`) against the actual fulltext PDFs in my Zotero library. For each paper:
> 1. Search Zotero by title/author to find the item key
> 2. Retrieve the fulltext via `get_item_fulltext`
> 3. Extract: abstract, introduction (first 2 paragraphs), conclusion, limitations section, and future work section
> 4. Cross-check against the matrix columns: Core Argument, Gaps Overcame, Limitation Tags, Future Works
> 5. Report discrepancies and update the matrix accordingly
> 
> Prioritize: Tier 1 papers first, then Tier 2. Flag any paper not found in Zotero for manual import.
> 
> Target files:
> - Matrix to update: `MD/LR_Matrix.md`
> - Literature review: `MD/LR.md`

---

**Notes for the agent:**
- Zotero search tools require activation: `activate_zotero_search_tools`, `activate_zotero_item_details`, `activate_zotero_saved_search_management`
- Library has 1,810 items; `Automation in Construction` is the top journal (175 papers)
- Fulltext retrieval works for PDFs indexed by Zotero; papers without indexed PDFs should be flagged
- The matrix has 91 rows; Tier 1 = 20 papers, Tier 2 = 19 papers, Tier 3 = 11 papers, Tier 4 = 4 papers, Original SLR = ~60 papers
- Key Zotero collections: DT/01_core_frame, DT/02_Semantic, DT/03_cases, DT/04_RefOnly
