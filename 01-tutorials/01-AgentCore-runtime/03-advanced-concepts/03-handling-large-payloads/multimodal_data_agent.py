from strands import Agent, tool
from strands.models import BedrockModel
import pandas as pd
import base64
import io
import json
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()

# Initialize the model and agent
model_id = "global.anthropic.claude-haiku-4-5-20251001-v1:0"
model = BedrockModel(
    model_id=model_id,
    max_tokens=16000
)

agent = Agent(
    model=model,
    system_prompt="""あなたは大規模なExcelファイルや画像を処理できるデータ分析アシスタントです。
マルチモーダルデータが提供された場合、構造化データと視覚的コンテンツの両方を分析し、
両方のデータソースを組み合わせた包括的な洞察を提供します。
    """
)

@app.entrypoint
def multimodal_data_processor(payload, context):
    """
    Excelデータと画像を含む大規模なマルチモーダルペイロードを処理します。

    Args:
        payload: プロンプト、excel_data (base64)、image_data (base64) を含む
        context: 実行時コンテキスト情報

    Returns:
        str: 両データソースからの分析結果
    """
    prompt = payload.get("prompt", "Analyze the provided data.")
    excel_data = payload.get("excel_data", "")
    image_data = payload.get("image_data", "")

    print(f"=== Large Payload Processing ===")
    print(f"Session ID: {context.session_id}")

    if excel_data:
        print(f"Excel data size: {len(excel_data) / 1024 / 1024:.2f} MB")
    if image_data:
        print(f"Image data size: {len(image_data) / 1024 / 1024:.2f} MB")
    print(f"Excel data {excel_data}")
    print(f"Image data {image_data}")
    print(f"=== Processing Started ===")
    # Decode base64 to bytes
    excel_bytes = base64.b64decode(excel_data)
    # Decode base64 to bytes
    image_bytes = base64.b64decode(image_data)

    # Enhanced prompt with data context
    enhanced_prompt = f"""{prompt}
    両方のデータソースを分析し、洞察を提供してください。
    """

    response = agent(
        [{
            "document": {
                "format": "xlsx",
                "name": "excel_data",
                "source": {
                    "bytes": excel_bytes
                }
            }
        },
        {
            "image": {
                "format": "png",
                "source": {
                    "bytes": image_bytes
                }
            }
        },
        {
            "text": enhanced_prompt
        }]
    )
    return response.message['content'][0]['text']

if __name__ == "__main__":
    app.run()
