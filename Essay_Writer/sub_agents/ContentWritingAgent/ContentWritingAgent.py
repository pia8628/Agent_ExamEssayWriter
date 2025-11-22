from google.adk.agents import Agent
from google.adk.tools import google_search
import os
from dotenv import load_dotenv

load_dotenv()
model = os.getenv("MODEL", "gemini-2.5-flash")

ContentWritingAgent = Agent(
    model=model,
    name="ContentWritingAgent",
    description="輸入OutlineGenerationAgent產出的大綱，以及TopicAnalysisAgent產出的題目分析報告",
    instruction="""
    處理過程
    1. 逐一處理大綱中的每個要點，生成完整段落
    2. 
    3. 輸出：數個獨立的、完整的文章段落
    """,
    output_key="EssayContent",
    tools=[],

)