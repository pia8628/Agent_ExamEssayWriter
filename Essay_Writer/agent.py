from google.adk.agents import Agent

from .sub_agents import (
    TopicAnalysisAgent,
    OutlineGenerationAgent,
    ContentWritingAgent,
    ReviewAndPolishAgent,
)

root_agent = Agent(
    model='gemini-2.5-flash',
    name='Essay_Writer_Agent',
    description='一個專業國家考試作文寫手，能夠根據使用者提供的主題分析、生成大綱、撰寫內容並進行審核和潤色。',
    instruction=f"""

    你是一個專業的國家考試作文寫手。你的任務是根據使用者提供的主題，通過以下四個步驟來完成一篇高質量的作文：
    1. 主題分析：使用TopicAnalysisAgent，理解並分析題目要求，判斷題型，確定關鍵點和要求。
    2. 大綱生成：使用TopicAnalysisAgent根據主題分析的結果，生成一個清晰且有邏輯的大綱，大綱可提供給使用者確認反饋。
    3. 內容撰寫：使用者確認大綱後，利用ContentWritingAgent，根據大綱撰寫完整的作文內容，確保內容連貫且符合主題要求。
    4. 審核和潤色：使用ReviewAndPolishAgent對撰寫的內容進行審核，確保語法正確，並進行必要的潤色以提升文章品質。文章內容須給使用者確認是否修改。
    請根據使用者提供的主題，依次執行上述四個步驟，最終生成一篇符合國家考試標準的高質量作文。
    """,

    sub_agents=[
        TopicAnalysisAgent,
        OutlineGenerationAgent,
        ContentWritingAgent,
        ReviewAndPolishAgent,
    ],
)

