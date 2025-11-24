from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools import AgentTool

import os
from dotenv import load_dotenv

load_dotenv()
model = os.getenv("MODEL", "gemini-2.5-flash")

search_agent = Agent(
    model="gemini-2.5-flash",
    name="search_agent",
    instruction="Use Google Search to find up-to-date, reliable sources and return grounded findings.",
    tools=[google_search], 
    output_key="SearchResults",
)

web_search_tool = AgentTool(agent=search_agent)

OutlineGenerationAgent = Agent(
    model=model,
    name="OutlineGenerationAgent",
    description="輸入TopicAnalysisAgent產出的題目分析報告{TopicAnalysis}，生成符合國考作文要求的文章大綱",
    instruction="""
    輸入TopicAnalysisAgent產出的題目分析報告{TopicAnalysis}
    處理過程
    1. 根據題目分析報告，確定文章的主題和重點
    2. 設計符合國考作文「起、承、轉、合」的大綱
    3. 規劃每個段落的主題句(topic sentence)
    4. 建議可以在每個段落引用的名言、案例或數據方向。
        如果是抒情文：
            - 起：引入主題，設置情感基調(中立或正向，不可負面情感)。不要過多重複題目內容。
            - 承：展開情感描寫，加入細節和例子，必須與個人生命經驗相關，強調人與人的連結
            - 轉：情感高潮或轉折點
            - 合：總結情感，呼應開頭
        如果是論說文：
            - 起：引入論點(不要過多重複題目內容)，提出觀點
                  如果題目有不同觀點，擇一立場進行論述，前後文立場需一致。                  
            - 承：支持論點的理由和證據，如果相關，可加入熱門議題如：AI、氣候變遷、人性反思等
            - 轉：反駁可能的反對意見
            - 合：總結論點，強調立場
        重要！！如果內容有關於時事，請使用web_search_tool工具查核事實
    5. 至多不要超過5段，並為每個部分分配適當的字數比例，例如：起(15%)、承(35%)、轉(30%)、合(20%)。
    6. 確保大綱邏輯清晰且連貫
    7. 輸出：一個結構化大綱，每個部分都有明確的主題。
    如果使用者確認大綱沒有問題，請交給ContentWritingAgent進行下一步的內容撰寫。
    """,

    tools=[web_search_tool],
    output_key="EssayOutline",
)
