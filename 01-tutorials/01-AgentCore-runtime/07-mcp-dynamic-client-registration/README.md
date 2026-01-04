# AgentCore RuntimeとAuth0を使用した動的クライアント登録

## 概要

このセッションでは、Amazon Bedrock AgentCore RuntimeでMCPツールをホストする方法について説明します。このMCPは、Auth0の動的クライアント登録（Dynamic Client Registration）機能と統合されます。

Amazon Bedrock AgentCore Python SDKを使用して、エージェントの関数をAmazon Bedrock AgentCoreと互換性のあるMCPサーバーとしてラップします。MCPサーバーの詳細を処理するため、エージェントのコア機能に集中できます。

Amazon Bedrock AgentCore Python SDKは、エージェントまたはツールコードをAgentCore Runtimeで実行できるように準備します。

## はじめに

このチュートリアルを開始するには、Jupyterノートブックのステップバイステップガイドを開いて従ってください：

**[📓 deploy_dcr_mcp_agentcore.ipynb](deploy_dcr_mcp_agentcore.ipynb)**

ノートブックには、このチュートリアルを完了するために必要なすべてのコード例、設定、詳細な手順が含まれています。

## 学習内容

このチュートリアルでは、以下を学習します：

* ツール付きMCPサーバーの作成方法
* サーバーをローカルでテストする方法
* Auth0テナントをDCRをサポートするように設定し、APIとアプリを追加する方法
* サーバーをAWSにデプロイし、Auth0のDCRと統合する方法
* デプロイされたサーバーを呼び出す方法

### チュートリアルの詳細

| 情報               | 詳細                                                       |
|:------------------|:-----------------------------------------------------------|
| チュートリアルタイプ | Auth0でのツールホスティング + DCR                          |
| ツールタイプ       | MCPサーバー                                                 |
| チュートリアル構成要素 | AgentCore Runtimeでのツールホスティング、MCPサーバーの作成 |
| チュートリアル垂直領域 | クロス垂直領域                                              |
| 例の複雑さ         | 中程度                                                      |
| 使用SDK            | Amazon BedrockAgentCore Python SDKとMCP Client            |

### チュートリアルアーキテクチャ

このチュートリアルでは、この例をAgentCore Runtimeにデプロイする方法について説明します。

デモンストレーションの目的で、3つのツール（`add_numbers`、`multiply_numbers`、`greet_users`）を持つ非常にシンプルなMCPサーバーを使用します。

<img src="images/architecture.png" width="80%">

### チュートリアルの主な機能

* MCPサーバーのホスティング
* 動的クライアント登録（DCR）
* Auth0
