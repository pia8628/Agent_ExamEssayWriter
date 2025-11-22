from google.adk.agents import Agent
import os
from dotenv import load_dotenv

load_dotenv()
model = os.getenv("MODEL", "gemini-2.5-flash")

ReviewAndPolishAgent = Agent(
    model=model,
    name="ReviewAndPolishAgent",
    description="輸入ContentWritingAgent產出的文章內容",
    instruction="""
    處理過程
    1. 仔細審核文章內容，檢查語法、拼寫和標點符號錯誤
    2. 評估文章的結構和邏輯連貫性，確保段落之間過渡自然
    3. 根據國考作文標準，進行必要的潤色，提高文章的表達效果
    4. 提出修改建議，並生成潤色後的最終版本
    5. 輸出：經過審核和潤色的完整文章內容
    """,
    output_key="ReviewedEssayContent",
)