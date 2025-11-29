# Agent-Based Essay Writer Overview

## 中文版

### 問題描述
國家考試的申論題要求在有限時間內寫出結構嚴謹、論點清晰的文章。考生常見的難題包括：拆解題意、安排「起承轉合」的脈絡、分配段落字數，以及兼顧語氣與論證深度。本系統旨在產生具參考價值的範例文章，協助考生快速理解標準結構並反覆練習。

### 為何採用代理（Agents）
- **步驟分工：** 將題意解析、架構設計、寫作與潤稿拆成不同代理，便於針對每一步微調策略。
- **透明可追蹤：** 各階段輸出中間成果（大綱、草稿、修訂意見），方便檢視與修正。
- **可擴充性：** 需要新增語氣、長度或引用規範時，只需調整或插入對應代理，不必改寫整個流程。
- **品質穩定：** 每個代理都是檢查點，能在早期捕捉邏輯或篇幅問題，降低一次性生成的失誤。

### 架構概覽
- **Root Orchestrator（`root_agent`）：** 串接全流程並傳遞上下文。
- **TopicAnalysisAgent：** 判斷題型、抓取關鍵論點與必答要素。
- **OutlineGenerationAgent：** 生成起承轉合大綱，附段落目標與字數配額。
- **ContentWritingAgent：** 依大綱撰寫段落，控制口吻與長度。
- **ReviewAndPolishAgent：** 檢查連貫性、語法與字數（預設 700 字以內），提出修訂。
- **產出物：** 各步驟的輸出供下一步使用，確保邏輯連續與篇章一致。

### 建置方式
- **語言與執行環境：** Python 3.10+。
- **核心套件：** `google-adk` 提供模型介面；`python-dotenv` 從 `.env` 讀取設定。
- **主要設定：** 內建模型為 `gemini-2.5-flash`，憑證以環境變數 `GOOGLE_API_KEY` 提供。
- **目錄配置：** `agent.py` 為總控代理；`sub_agents/` 放置各子代理定義與提示詞。
- **使用方式：** 匯入 `root_agent`，輸入考題敘述，即可取得具標準結構的範例文章供複習或微調。

### 若有更多時間，將會改善
- 建立自動評測迴路，依歷屆評分規準量化連貫度與論證完整性。
- 加入檢索增強，以最新法規或數據支撐論點。
- 製作簡易網頁介面，允許生成前先調整大綱。
- 提供雙語與多語提示包，涵蓋不同考試情境。
- 強化事實查核與偏誤防護，降低生成不準確內容的風險。

## English Version (under 1,500 words)

### Problem Statement
National civil-service essay questions require candidates to produce tightly structured, clear arguments under strict time limits. Common hurdles include parsing the prompt, planning a coherent flow, allocating word counts, and balancing tone with depth. This system generates exemplar essays so learners can study standard structures and rehearse effectively.

### Why Agents?
- **Specialized stages:** Separate agents handle prompt analysis, outline design, drafting, and polishing, allowing targeted tuning at each step.
- **Transparent checkpoints:** Every stage emits intermediate outputs (outline, draft, revision notes) so users can inspect and adjust.
- **Flexible extension:** New tone, length, or citation rules can be added by inserting or tweaking agents without rewriting the whole pipeline.
- **Quality control:** Each agent acts as a guardrail to catch logic or length issues early, avoiding one-shot generation errors.

### Architecture Overview
- **Root Orchestrator (`root_agent`):** Connects the workflow and carries context across steps.
- **TopicAnalysisAgent:** Identifies question type, key arguments, and required points.
- **OutlineGenerationAgent:** Produces an introduction-body-conclusion outline with goals and word budgets per paragraph.
- **ContentWritingAgent:** Writes paragraphs to match the outline, tone, and length constraints.
- **ReviewAndPolishAgent:** Checks coherence, grammar, and word limits (default 700 words) and suggests revisions.
- **Artifacts:** Each step’s output feeds the next to keep logic and narrative consistent.

### How It Was Built
- **Language & runtime:** Python 3.10+.
- **Core libraries:** `google-adk` for model access; `python-dotenv` to load configuration from `.env`.
- **Key defaults:** Uses the `gemini-2.5-flash` model with credentials provided via the `GOOGLE_API_KEY` environment variable.
- **Layout:** `agent.py` hosts the orchestrator; `sub_agents/` contains agent definitions and prompt templates.
- **Usage:** Import `root_agent`, provide the exam prompt, and receive a reference essay with standard structure for review or refinement.

### If I Had More Time
- Build an automatic evaluation loop that scores coherence and argument completeness using historical rubrics.
- Add retrieval augmentation to ground arguments in up-to-date laws and data.
- Create a lightweight web UI that lets users adjust the outline before generation.
- Offer bilingual and multilingual prompt packs for diverse exam contexts.
- Strengthen fact-checking and bias safeguards to reduce inaccurate outputs.
