from google.adk.agents import Agent
from google.adk.tools import google_search
import os


ContentWritingAgent = Agent(
    model='gemini-2.5-flash',
    name="ContentWritingAgent",
    description="輸入OutlineGenerationAgent產出的大綱{EssayOutline}，以及TopicAnalysisAgent產出的題目分析報告{TopicAnalysis}，生成符合國考作文要求的文章內容",
    instruction="""
    處理過程
    1. 逐一處理大綱中的每個要點，生成完整段落。
    2. 語氣口語一點，不要太過生硬。
    3. 注意總字數限制不要超過700字。
    4. 輸出：數個獨立的、完整的文章段落，每個段落不需要標題。
    """,
    output_key="EssayContent",
    tools=[],

)