import logging
import os
import asyncio
from strands import Agent, tool
from strands.multiagent.a2a import A2AServer
import uvicorn
from fastapi import FastAPI

from ddgs import DDGS
from ddgs.exceptions import RatelimitException, DDGSException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

runtime_url = os.environ.get('AGENTCORE_RUNTIME_URL', 'http://127.0.0.1:9000/')

@tool
async def fast_internet_search(keywords: str, max_results: int = 3) -> str:
    """タイムアウト付きの高速Web検索。
    引数:
        keywords (str): 検索クエリのキーワード
        max_results (int): 最大結果数（速度のためデフォルト3）
    戻り値:
        検索結果
    """
    try:
        # より良い結果のためにAWS固有の用語を追加
        aws_keywords = f"site:aws.amazon.com {keywords} AWS"

        # 検索にasyncioタイムアウトを使用
        async def search_with_timeout():
            return DDGS().text(
                aws_keywords, 
                region="us-en", 
                max_results=max_results
            )

        results = await asyncio.wait_for(search_with_timeout(), timeout=8.0)

        if results:
            # 結果を簡潔にフォーマット
            formatted = []
            for i, result in enumerate(results[:max_results], 1):
                formatted.append(f"{i}. {result.get('title', 'No title')}\n   {result.get('href', '')}")

            return "\n".join(formatted)
        else:
            return "AWSの結果が見つかりませんでした。"

    except asyncio.TimeoutError:
        logger.warning(f"検索タイムアウト: {keywords}")
        return "検索がタイムアウトしました。より具体的なクエリを試してください。"
    except RatelimitException:
        logger.warning("レート制限に達しました")
        return "レート制限に達しました。しばらくしてから再試行してください。"
    except (DDGSException, Exception) as e:
        logger.error(f"検索エラー: {e}")
        return f"検索が利用できません: {str(e)[:50]}"

system_prompt = """あなたはAWS Blogエキスパートです。

重要: 応答は短く、最新のものにしてください。

ガイドライン:
- 最大3つの最新の結果を提供する
- 公式のAWSブログ投稿のみに焦点を当てる
- 簡潔な要約を使用する（結果ごとに1-2文）
- 利用可能な場合は直接リンクを含める
- 検索は8秒後にタイムアウト
- 検索が失敗した場合、制限を認める

検索戦略:
- 検索には常に「AWS」を含める
- aws.amazon.com/blogs/のコンテンツに焦点を当てる
- 最近のアナウンスを優先する"""

agent = Agent(
    system_prompt=system_prompt, 
    tools=[fast_internet_search],
    name="AWS Blog/Newsエージェント",
    description="Web上で最新のAWSブログとニュースを検索するエージェント。",
)

host, port = "0.0.0.0", 9000

a2a_server = A2AServer(
    agent=agent,
    http_url=runtime_url,
    serve_at_root=True
)

app = FastAPI()

@app.get("/ping")
def ping():
    return {"status": "healthy"}

app.mount("/", a2a_server.to_fastapi_app())

if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)
