
from google.adk.agents import Agent
import os
from dotenv import load_dotenv

load_dotenv()
model = os.getenv("MODEL", "gemini-2.5-flash")

'''
TopicAnalysisAgent Translation
Description (English): Analyze the user's topic to determine the essay type and identify key points and requirements.
Instruction (English):
1. Read and understand the user's topic and constraints.
2. Classify the topic as lyrical or persuasive.
3. Extract keywords, key points, and grading criteria.
4. Add the 700-character limit requirement.
5. Output a structured topic analysis report covering type, key points, and writing essentials.
'''
TopicAnalysisAgent = Agent(
        model='gemini-2.5-flash',
        name="TopicAnalysisAgent",
        description="分析使用者提供的題目，判斷題型、確定關鍵點與要求",
        instruction="""
        處理流程：
        1. 閱讀並理解使用者提供的題目與限制條件
        2. 判斷題型，只要分成兩類：抒情文或論說文
        3. 擷取關鍵詞、重點與評分項目
        4. 加入字數要求：700中文字以內
        5. 輸出：結構化的題目分析報告，包含題型、關鍵點與寫作要點
        """,
    tools=[],
	output_key="TopicAnalysis",
)
