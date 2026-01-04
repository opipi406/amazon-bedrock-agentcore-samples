## AgentCore RuntimeでのA2Aの概要

### 概要

Amazon Bedrock AgentCore Runtimeは、AIエージェントとツールをデプロイおよびスケーリングするために設計された、セキュアなサーバーレスランタイムです。
あらゆるフレームワーク、モデル、プロトコルをサポートし、開発者が最小限のコード変更でローカルプロトタイプを本番環境対応のソリューションに変換できるようにします。

[Strands Agents](https://strandsagents.com/latest/)は、エージェントを構築するためのシンプルでコードファーストなフレームワークです。

最近、AWSはAgentCore Runtimeの[A2Aサポート](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-a2a.html)を発表しました。

この例では、Amazon Bedrock AgentCoreとStrands Agentsを使用してマルチエージェントシステムを構築します。

このチュートリアルでは、3つのエージェントの作成について説明します。1つ目はAWSドキュメントの専門家で、MCPを使用してAWS Docsを利用します。2つ目は、最新のブログやAWSニュースをWebで検索します。3つ目はオーケストレーターで、MCPを使用して前の2つを呼び出します。

<img src="images/architecture.png" style="width: 80%;">

### チュートリアルの概要

これらのチュートリアルでは、以下の機能について説明します：

- [1 - StrandsとBedrock AgentCoreでA2Aを始める](01-a2a-getting-started-agentcore-strands.ipynb)
- [2 - A2Aを使用してサブエージェントを呼び出すオーケストレーターを作成する](02-a2a-deploy-orchestrator.ipynb)
- [3 - クリーンアップ](03-a2a-cleanup.ipynb)
