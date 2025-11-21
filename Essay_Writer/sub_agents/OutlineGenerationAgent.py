from google.adk.agents import Agent

OutlineGenerationAgent = Agent(
    model='gemini-2.5-flash',
    name="OutlineGenerationAgent",
    description="輸入TopicAnalysisAgent產出的題目分析報告",
    instruction="""
    處理過程
    1. 根據題目分析報告，確定文章的主題和重點
    2. 設計符合國考作文「起、承、轉、合」的大鋼
    3. 規劃每個段落的主題句(topic sentence)
    4. 建議可以在每個段落引用的名言、案例或數據方向。
    5. 確保大綱邏輯清晰且連貫
    5. 輸出：一個結構化大綱，每個部分都有明確的主題。
    """,

    output_key="EssayOutline",
)
