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

'''
OutlineGenerationAgent Translation
Description (English): Generate an essay outline that meets civil service exam requirements based on
TopicAnalysisAgent's analysis report {TopicAnalysis}.
Instruction (English):
1. Use the topic analysis report to confirm the essay's theme and focus.
2. Design an outline that follows the classical opening (起), development (承), turn (轉), and conclusion (合).
3. Plan a topic sentence for each paragraph and recommend quotes, cases, or data directions.
4. Provide paragraph guidance by essay type:
   If lyrical essay:
     - Opening (起): introduce the theme, set a neutral or positive emotional tone, and avoid repeating the prompt.
     - Development (承): expand emotional description with details and examples tied to personal life experiences;
       emphasize human connection.
     - Turn (轉): highlight the emotional climax or turning point.
     - Conclusion (合): summarize the emotion and echo the opening.
   If persuasive essay:
     - Opening (起): introduce the argument without heavily repeating the prompt; if multiple viewpoints exist, choose
       one stance and keep it consistent.
     - Development (承): support the stance with reasons and evidence; when relevant, weave in timely topics such as AI,
       climate change, or reflections on human nature.
     - Turn (轉): rebut potential counterarguments.
     - Conclusion (合): summarize the arguments and reinforce the stance.
   Important: if discussing current events, fact-check them with the web_search_tool.
5. Keep the outline to at most five sections and suggest word allocations, e.g., 起(15%), 承(35%), 轉(30%), 合(20%).
6. Ensure the outline is logically clear and coherent.
7. Output a structured outline with clear themes for each section.
Handoff: after the user confirms, pass it to ContentWritingAgent for drafting.
'''
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
