import os
import logging
from mcp import stdio_client, StdioServerParameters
from strands import Agent
from strands.multiagent.a2a import A2AServer
from strands.tools.mcp import MCPClient
from fastapi import FastAPI
import uvicorn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
runtime_url = os.environ.get('AGENTCORE_RUNTIME_URL', 'http://127.0.0.1:9000/')
host, port = "0.0.0.0", 9000

# MCPクライアントを作成（Managed approachで使用）
mcp_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx",
            args=["awslabs.aws-documentation-mcp-server@latest"]
        )
    )
)

system_prompt = """あなたはAWS Documentation MCPサーバーを搭載したAWSドキュメントアシスタントです。あなたの役割は、ユーザーがAWSドキュメントから正確で最新の情報を見つけるのを支援することです。

重要: 応答は短く、焦点を絞ったものにしてください。

ガイドライン:
- 簡潔で実用的な回答を提供する（最大3文）
- リストには箇条書きを使用する
- 冗長な説明は省略する
- MCPが利用できない場合、基本的なAWS知識を提供する
- 操作は8秒後にタイムアウト
- 完全性よりも速度を優先する

利用可能な場合は、AWSドキュメント検索ツールにアクセスできます。"""

# Managed approachでMCPClientをエージェントに渡す
# エージェントがMCPクライアントのライフサイクルを自動管理
agent = Agent(
    system_prompt=system_prompt,
    tools=[mcp_client],
    name="AWS Docsエージェント",
    description="AWS MCPを使用してAWS Docsにクエリを送信するエージェント。",
)

a2a_server = A2AServer(
    agent=agent,
    http_url=runtime_url,
    serve_at_root=True
)

@app.get("/ping")
def ping():
    return {"status": "healthy"}

app.mount("/", a2a_server.to_fastapi_app())

if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)
