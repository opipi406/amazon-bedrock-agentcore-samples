# Amazon Bedrock AgentCore Runtime

## 概要
Amazon Bedrock AgentCore Runtime は、AI エージェントやツールのデプロイとスケールのために設計されたセキュアなサーバーレスランタイムです。
あらゆるフレームワーク、モデル、プロトコルをサポートし、ローカルプロトタイプから本番レディなソリューションへの移行を最小限のコード変更で実現します。

Amazon BedrockAgentCore Python SDK は軽量なラッパーを提供し、あなたのエージェント関数を Amazon Bedrock と互換性のある HTTP サービスとして簡単にデプロイできます。HTTP サーバの詳細は SDK が自動的に処理するため、エージェント本来のロジック構築に集中できます。

`@app.entrypoint` デコレーターを関数に付与し、SDK の `configure` および `launch` 機能を使うだけで、あなたのエージェントを AgentCore Runtime にデプロイできます。デプロイ後は SDK や boto3、AWS SDK for JavaScript、AWS SDK for Java など様々な AWS 開発ツールからエージェントへリクエストを送ることができます。

![Runtime Overview](images/runtime_overview.png)

## 主な特長

### フレームワーク・モデルの柔軟性

- どんなエージェントフレームワーク（Strands Agents, LangChain, LangGraph, CrewAI など）からでもデプロイ可能
- あらゆるモデル（Amazon Bedrock 以外も可）を利用可能

### 統合性

Amazon Bedrock AgentCore Runtime は、以下を含む他の Amazon Bedrock AgentCore 機能と統合された SDK を通じて連携できます：

- Amazon Bedrock AgentCore Memory
- Amazon Bedrock AgentCore Gateway
- Amazon Bedrock AgentCore Observability
- Amazon Bedrock AgentCore Tools

この統合により、AI エージェントの開発・デプロイ・運用を一元的に管理でき、開発プロセスを大幅に簡素化します。

### 利用ユースケース

Runtime はさまざまな用途に最適です：

- リアルタイムかつインタラクティブな AI エージェント
- 長時間実行・複雑な AI ワークフロー
- マルチモーダル処理（テキスト、画像、音声、動画）

## チュートリアルの概要

本チュートリアルでは下記の機能を順に解説します：

- [エージェントのホスティング](01-hosting-agent)
- [MCP サーバーのホスティング](02-hosting-MCP-server)
- [高度なコンセプト](03-advanced-concepts)
