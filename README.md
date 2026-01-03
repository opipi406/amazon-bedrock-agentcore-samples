<div align="center">
  <div>
    <a href="https://aws.amazon.com/bedrock/agentcore/">
      <img width="150" height="150" alt="image" src="https://github.com/user-attachments/assets/b8b9456d-c9e2-45e1-ac5b-760f21f1ac18" />
   </a>
  </div>

  <h1>
      Amazon Bedrock AgentCore サンプル集
  </h1>

  <h2>
    どんなフレームワークやモデルでも、大規模かつ安全にAIエージェントをデプロイ＆運用
  </h2>

  <div align="center">
    <a href="https://github.com/awslabs/amazon-bedrock-agentcore-samples/graphs/commit-activity"><img alt="GitHub コミットアクティビティ" src="https://img.shields.io/github/commit-activity/m/awslabs/amazon-bedrock-agentcore-samples"/></a>
    <a href="https://github.com/awslabs/amazon-bedrock-agentcore-samples/issues"><img alt="GitHub オープンイシュー" src="https://img.shields.io/github/issues/awslabs/amazon-bedrock-agentcore-samples"/></a>
    <a href="https://github.com/awslabs/amazon-bedrock-agentcore-samples/pulls"><img alt="GitHub オープンプルリクエスト" src="https://img.shields.io/github/issues-pr/awslabs/amazon-bedrock-agentcore-samples"/></a>
    <a href="https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/LICENSE"><img alt="ライセンス" src="https://img.shields.io/github/license/awslabs/amazon-bedrock-agentcore-samples"/></a>
  </div>
  
  <p>
    <a href="https://docs.aws.amazon.com/bedrock-agentcore/">ドキュメント</a>
    ◆ <a href="https://github.com/aws/bedrock-agentcore-sdk-python">Python SDK</a>
    ◆ <a href="https://github.com/aws/bedrock-agentcore-starter-toolkit">スターターツールキット</a>
    ◆ <a href="https://discord.gg/bedrockagentcore-preview">Discord</a>
  </p>
</div>

Amazon Bedrock AgentCore サンプルのリポジトリへようこそ！

Amazon Bedrock AgentCoreは、"フレームワーク非依存"および"モデル非依存"です。これにより、どんなフレームワークでも、どんな大規模言語モデル（LLM）でも、高度なAIエージェントを安全かつスケーラブルにデプロイ・運用できます。[Strands Agents](https://strandsagents.com/latest/)、[CrewAI](https://www.crewai.com/)、[LangGraph](https://www.langchain.com/langgraph)、[LlamaIndex](https://www.llamaindex.ai/)他、どんなフレームワーク／モデルでも動作対応可能。専用インフラの開発・運用という煩雑な作業を排し、お好みのフレームワーク／モデルをそのまま持ち込んで展開できます。

本リポジトリは、Amazon Bedrock AgentCoreの導入・実装・活用のための例やチュートリアルを提供します。

## 🎥 動画

Amazon Bedrock AgentCoreで最初の本番用AIエージェントを構築しよう。プロトタイピングから一歩進み、AgentCoreを使ったエージェントAIアプリケーションの本番運用化までデモ動画でご紹介します。

<p align="center">
  <a href="https://www.youtube.com/watch?v=wzIQDPFQx30"><img src="https://markdown-videos-api.jorgenkh.no/youtube/wzIQDPFQx30?width=640&height=360&filetype=jpeg" /></a>
</p>

## 📁 リポジトリ構成

### 📚 [`01-tutorials/`](./01-tutorials/)
**インタラクティブ学習 & 基礎**

このフォルダには、ノートブック形式でAgentCore機能の基礎から学べるチュートリアルが含まれています。

AgentCoreの各コンポーネントごとに構成されています：

* **[Runtime](./01-tutorials/01-AgentCore-runtime)**: Amazon Bedrock AgentCore Runtimeは、どんなフレームワーク・プロトコル・モデルでも利用可能なセキュアなサーバーレス実行基盤です。AIエージェントやツールを迅速にプロトタイピングし、シームレスにスケール＆市場投入を加速します。
* **[Gateway](./01-tutorials/02-AgentCore-gateway)**: エージェントは、データベース検索やメッセージ送信など現実世界のタスクを実行するためのツールが必要です。Bedrock AgentCore Gatewayは、API、Lambda、既存サービスをMCP対応ツールへ自動変換し、開発者は面倒な統合管理なしにエージェントが利用できる機能を瞬時に提供できます。
* **[Memory](./01-tutorials/04-AgentCore-memory)**: Bedrock AgentCore Memoryにより、開発者はフルマネージドなメモリ基盤を活用して、豊かなパーソナライズドエージェント体験の構築と用途に応じたメモリカスタムが容易になります。
* **[Identity](./01-tutorials/03-AgentCore-identity)**: Bedrock AgentCore Identityは、AWSサービスやSlack・Zoomなどサードパーティとのシームレスなエージェント識別・アクセス管理を実現。Okta、Entra、Amazon Cognitoなど標準IDプロバイダーもサポートしています。
* **[Tools](./01-tutorials/05-AgentCore-tools)**: Bedrock AgentCoreには2つの組み込みツールがあります。**コードインタープリター**はAIエージェントが安全にコードを書いて実行できる機能で、精度と問題解決力を向上。**ブラウザツール**はAIエージェントがWebサイトをナビゲートし、多段階フォームや複雑作業を低遅延・完全分離のセキュアサンドボックス内で実行させます。
* **[Observability](./01-tutorials/06-AgentCore-observability)**: AgentCore Observabilityにより、開発者は統一ダッシュボードからエージェントの性能をトレース・デバッグ・監視可能。OpenTelemetry互換のテレメトリやワークフローの詳細可視化で、品質基準の維持や動作分析も容易です。

* **[AgentCore end-to-end](./01-tutorials/07-AgentCore-E2E)**: このチュートリアルでは、カスタマーサポートエージェントをプロトタイプから本番までBedrock AgentCoreサービスで段階的に構築します。


これらのサンプルは、初心者や基礎概念を学びたい方向けの内容です。

### 💡 [`02-use-cases/`](./02-use-cases/)
**エンド・ツー・エンドアプリケーション**

Bedrock AgentCoreを活用した現実的なビジネス課題解決のユースケースを体系的に解説しています。

各ユースケースはAgentCoreコンポーネントに集中した実装例と詳細解説付きです。

### 🔌 [`03-integrations/`](./03-integrations/)
**フレームワーク & プロトコル連携**

Strands Agents、LangChain、CrewAIなど人気のエージェントフレームワークとの連携方法を解説。

A2Aによるエージェント間通信や各種マルチエージェント協調パターンの実現。入口を変えたエージェント連携手法も学べます。

### 🏗️ [`04-infrastructure-as-code/`](./04-infrastructure-as-code/)
**デプロイ自動化・インフラコード化**

Bedrock AgentCoreリソースをインフラ構成管理ツール（CloudFormation、AWS CDK、Terraform）で自動デプロイする例を掲載。

基本ランタイム、MCPサーバー、マルチエージェントシステム、ツール・メモリ統合型など各種プロダクション用テンプレートあり。

### 🚀 [`05-blueprints/`](./05-blueprints/)
**フルスタック・リファレンスアプリケーション**

Bedrock AgentCore上に構築された、すぐにデプロイできる実践的なエージェントAIアプリ例集。

各ブループリントは、サービス統合／認証／ビジネスロジックまで組み込み済みの基盤として活用できます。

## ノートブックの実行手順

1. 仮想環境の作成・有効化
```bash
python -m venv .venv
source .venv/bin/activate
```

2. 依存パッケージのインストール
```bash
pip install -r requirements.txt
```

3. ノートブック実行に必要なAWS認証情報をエクスポートまたは有効化

4. Jupyterノートブック用に仮想環境をカーネルとして登録
```bash
python -m ipykernel install --user --name=notebook-venv --display-name="Python (notebook-venv)"
```

カーネルの一覧は以下で確認できます：
```bash
jupyter kernelspec list
```

5. ノートブックを実行し、正しいカーネルを選択
```bash
jupyter notebook path/to/your/notebook.ipynb
```

**重要:** Jupyterでノートブックを開いた後、「カーネル」→「カーネルの変更」→「Python (notebook-venv)」を選択し、仮想環境のパッケージを利用できるようにしてください。

## クイックスタート - [Amazon Bedrock AgentCore Runtime](https://github.com/aws/bedrock-agentcore-starter-toolkit/blob/main/documentation/docs/user-guide/runtime/quickstart.md)

### ステップ1: 前提条件

- [AWSアカウント](https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fportal.aws.amazon.com%2Fbilling%2Fsignup%2Fresume&client_id=signup) の作成＆`aws configure`による認証情報設定
- [Python 3.10](https://www.python.org/downloads/) 以上
- [Docker](https://www.docker.com/) または [Finch](https://runfinch.com/) のインストール（ローカル開発時のみ）
- モデルアクセス：Amazon BedrockコンソールでAnthropic Claude 4.0が有効になっていること（[設定方法](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access-modify.html)）
- AWS権限：
    - `BedrockAgentCoreFullAccess` マネージドポリシー
    - `AmazonBedrockFullAccess` マネージドポリシー
    - `Caller 権限`: 詳細は[こちら](https://github.com/aws/bedrock-agentcore-starter-toolkit/blob/main/documentation/docs/user-guide/runtime/permissions.md#developercaller-permissions)

### ステップ2: エージェントの作成・インストール

```bash
# 必要なパッケージ両方をインストール
pip install bedrock-agentcore strands-agents bedrock-agentcore-starter-toolkit
```

`my_agent.py` を作成：

```python
from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent

app = BedrockAgentCoreApp()
agent = Agent()

@app.entrypoint
def invoke(payload):
    """AIエージェントのメイン関数"""
    user_message = payload.get("prompt", "こんにちは！どのようなご用件でしょうか？")
    result = agent(user_message)
    return {"result": result.message}

if __name__ == "__main__":
    app.run()
```
`requirements.txt` を作成：

```bash
cat > requirements.txt << EOF
bedrock-agentcore
strands-agents
EOF
```
### ステップ3: ローカルでテスト

```bash
# エージェントを起動
python my_agent.py

# （別ターミナルで）テスト送信
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "こんにちは!"}'
```
成功すると次のような応答が返ります：{"result": "こんにちは！お手伝いします..."}

### ステップ4: AWSへデプロイ

```bash
# 設定とデプロイ（必要なリソースを自動作成）
agentcore configure -e my_agent.py
agentcore launch

# デプロイ済みエージェントのテスト
agentcore invoke '{"prompt": "ジョークを言って"}'
```

おめでとうございます！エージェントがAmazon Bedrock AgentCore Runtime上で稼働しています。

[Gateway](https://github.com/aws/bedrock-agentcore-starter-toolkit/blob/main/documentation/docs/user-guide/gateway/quickstart.md)・[Identity](https://github.com/aws/bedrock-agentcore-starter-toolkit/blob/main/documentation/docs/user-guide/identity/quickstart.md)・[Memory](https://github.com/aws/bedrock-agentcore-starter-toolkit/blob/main/documentation/docs/user-guide/memory/quickstart.md)・[Observability](https://github.com/aws/bedrock-agentcore-starter-toolkit/blob/main/documentation/docs/user-guide/observability/quickstart.md)・[組み込みツール](https://github.com/aws/bedrock-agentcore-starter-toolkit/tree/main/documentation/docs/user-guide/builtin-tools)のガイドもどうぞ。

## 🔗 関連リンク

- [Amazon Bedrock AgentCore はじめてのワークショップ (英語)](https://catalog.us-east-1.prod.workshops.aws/workshops/850fcd5c-fd1f-48d7-932c-ad9babede979/en-US)
- [AgentCore Deep Dive ワークショップ](https://catalog.workshops.aws/agentcore-deep-dive/en-US)
- [Amazon Bedrock AgentCore 料金](https://aws.amazon.com/bedrock/agentcore/pricing/)
- [Amazon Bedrock AgentCore よくある質問](https://aws.amazon.com/bedrock/agentcore/faqs/)

## 🤝 コントリビューション（貢献）

皆様のご貢献をお待ちしています！[コントリビューションガイドライン](CONTRIBUTING.md)で以下を説明しています。

- 新しいサンプルの追加
- 既存例の改善
- 問題報告
- 改善提案


## 📄 ライセンス

このプロジェクトはApache License 2.0で提供されています。[LICENSE](LICENSE)ファイルをご確認ください。

## コントリビューター

<a href="https://github.com/awslabs/amazon-bedrock-agentcore-samples/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=awslabs/amazon-bedrock-agentcore-samples" />
</a>
