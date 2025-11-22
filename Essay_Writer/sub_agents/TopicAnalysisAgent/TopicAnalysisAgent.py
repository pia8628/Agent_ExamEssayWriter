
from google.adk.agents import Agent
import os
from dotenv import load_dotenv

load_dotenv()
model = os.getenv("MODEL", "gemini-2.5-flash")

TopicAnalysisAgent = Agent(
	model=model,
	name="TopicAnalysisAgent",
	description="分析使用者提供的題目，判斷題型、確定關鍵點與要求",
	instruction="""
	處理流程：
	1. 閱讀並理解使用者提供的題目與限制條件
	2. 判斷題型（例如：議論、說明、申論等）
	3. 擷取關鍵詞、重點與評分項目
	4. 輸出：結構化的題目分析報告，包含題型、關鍵點與寫作要點
	""",
	output_key="TopicAnalysis",
)
