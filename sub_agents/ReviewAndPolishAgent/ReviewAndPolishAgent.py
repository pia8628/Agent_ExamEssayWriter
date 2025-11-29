from google.adk.agents import Agent
import os
from dotenv import load_dotenv

load_dotenv()
model = os.getenv("MODEL", "gemini-2.5-flash")

'''
ReviewAndPolishAgent Translation
Description (English): Review and polish essay content {EssayContent} from ContentWritingAgent to ensure it meets civil
service exam standards.
Instruction (English):
1. Carefully review the essay for grammar, spelling, and punctuation errors.
2. Assess structure and logical flow between paragraphs to ensure natural transitions.
3. Polish the expression according to civil service exam standards to improve clarity and impact.
4. Provide revision suggestions and generate a refined final version.
5. Output the fully reviewed and polished essay content.
'''
ReviewAndPolishAgent = Agent(
    model=model,
    name="ReviewAndPolishAgent",
    description="輸入ContentWritingAgent產出的文章內容{EssayContent}，對文章進行審核和潤色，確保符合國考作文標準",
    instruction="""
    處理過程
    1. 仔細審核文章內容，檢查語法、拼寫和標點符號錯誤
    2. 評估文章的結構和邏輯連貫性，確保段落之間過渡自然
    3. 根據國考作文標準，進行必要的潤色，提高文章的表達效果
    4. 提出修改建議，並生成潤色後的最終版本
    5. 輸出：經過審核和潤色的完整文章內容
    """,
    tools=[],
    output_key="ReviewedEssayContent",
)
