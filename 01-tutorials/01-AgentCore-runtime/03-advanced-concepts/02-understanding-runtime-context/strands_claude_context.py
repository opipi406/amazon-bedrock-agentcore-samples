from strands import Agent, tool
from strands_tools import calculator # Import the calculator tool
import argparse
import json
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands.models import BedrockModel
import asyncio
from datetime import datetime

app = BedrockAgentCoreApp()

# Create a custom tool 
@tool
def weather():
    """ Get weather """ # Dummy implementation
    return "sunny"

@tool
def get_time():
    """ Get current time """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

model_id = "global.anthropic.claude-haiku-4-5-20251001-v1:0"
model = BedrockModel(
    model_id=model_id,
)
agent = Agent(
    model=model,
    tools=[
        calculator, weather, get_time
    ],
    system_prompt="""あなたは便利なアシスタントです。簡単な計算ができ、
天気予報を伝え、現在の時刻を提供できます。
常にユーザーの名前を呼んで会話を始めましょう
    """
)

def get_user_name(user_id):
    users = {
        "1": "Maira",
        "2": "Mani",
        "3": "Mark",
        "4": "Ishan",
        "5": "Dhawal"
    }
    return users[user_id]

@app.entrypoint
def strands_agent_bedrock_handling_context(payload, context):
    """
    AgentCoreランタイムのエントリポイント。コンテキスト処理とセッション管理を実演します。

    Args:
        payload: ユーザーデータとリクエスト情報を含む入力ペイロード
        context: セッションおよび実行情報を含むランタイムコンテキストオブジェクト

    Returns:
        str: コンテキスト情報を組み込んだエージェントの応答
    """
    user_input = payload.get("prompt")
    user_id = payload.get("user_id")
    user_name = get_user_name(user_id)

    # Access runtime context information
    print("=== Runtime Context Information ===")
    print("User id:", user_id)
    print("User Name:", user_name)
    print("User input:", user_input)
    print("Runtime Session ID:", context.session_id)
    print("Context Object Type:", type(context))
    print("=== End Context Information ===")

    # Create a personalized prompt that includes context information
    prompt = f"""私の名前は{user_name}です。以下が私のリクエストです：{user_input}

    Additional context：これは session {context.session_id} です。
    私の名前を確認の上、ご対応をお願いいたします。"""

    response = agent(prompt)
    return response.message['content'][0]['text']

if __name__ == "__main__":
    app.run()
