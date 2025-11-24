from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools import AgentTool
import os

search_agent = Agent(
    model="gemini-2.5-flash",
    name="search_agent",
    instruction="Use Google Search to find up-to-date, reliable sources and return grounded findings.",
    tools=[google_search],  
)

web_search_tool = AgentTool(agent=search_agent)

ContentWritingAgent = Agent(
    model='gemini-2.5-flash',
    name="ContentWritingAgent",
    description="輸入OutlineGenerationAgent產出的大綱{EssayOutline}，以及TopicAnalysisAgent產出的題目分析報告{TopicAnalysis}，生成符合國考作文要求的文章內容",
    instruction="""
    處理過程
    1. 逐一處理大綱中的每個要點，生成完整段落。
    2. 語氣口語一點，不要太過生硬。
    3. 如果有需要，使用google_search工具來查找相關資訊以豐富內容。
    4. 注意總字數限制不要超過700字。
    5. 輸出：數個獨立的、完整的文章段落，每個段落不需要標題。
    """,
    output_key="EssayContent",
    tools=[web_search_tool],

)