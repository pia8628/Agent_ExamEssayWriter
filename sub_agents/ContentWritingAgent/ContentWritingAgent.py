from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools import AgentTool
import os

search_agent = Agent(
    model="gemini-2.5-flash",
    name="search_agent",
    instruction="Use Google Search to find up-to-date, reliable sources and return grounded findings.",
    tools=[google_search],
    output_key="SearchResults",  
)

web_search_tool = AgentTool(agent=search_agent)

'''
ContentWritingAgent Translation
Description (English): Create exam-ready essay content using OutlineGenerationAgent's outline {EssayOutline} and
TopicAnalysisAgent's report {TopicAnalysis}.
Instruction (English):
1. Use the outline and topic analysis as inputs.
2. Expand each outline point into a full paragraph with a conversational tone.
3. Use web_search_tool when needed to find information that enriches the content.
4. Keep the total length within 700 characters.
5. Output several complete paragraphs without headings.
After the user confirms, hand off the content to ReviewAndPolishAgent for review and polishing.
'''
ContentWritingAgent = Agent(
    model='gemini-2.5-flash',
    name="ContentWritingAgent",
    description="輸入OutlineGenerationAgent產出的大綱{EssayOutline}，以及TopicAnalysisAgent產出的題目分析報告{TopicAnalysis}，生成符合國考作文要求的文章內容",
    instruction="""
    輸入OutlineGenerationAgent產出的大綱{EssayOutline}，以及TopicAnalysisAgent產出的題目分析報告{TopicAnalysis}
    處理過程
    1. 逐一處理大綱中的每個要點，生成完整段落。
    2. 語氣口語一點，不要太過生硬。
    3. 如果有需要，使用web_search_tool工具來查找相關資訊以豐富內容。
    4. 注意總字數限制不要超過700字。
    5. 輸出：數個獨立的、完整的文章段落，每個段落不需要標題。
    如果使用者確認沒問題，請把交給ReviewAndPolishAgent進行下一步的審核和潤色。
    """,
    output_key="EssayContent",
    tools=[web_search_tool],

)
