# AgentCore Runtime上でのMCPサーバーのホスティング

## 概要

このセッションでは、Amazon Bedrock AgentCore Runtime上でMCPツールをホスティングする方法について説明します。

Amazon Bedrock AgentCore Python SDKを使用して、エージェントの機能をAmazon Bedrock AgentCoreと互換性のあるMCPサーバーとしてラップします。
MCPサーバーの詳細を処理するため、エージェントのコア機能に集中できます。

Amazon Bedrock AgentCore Python SDKは、エージェントまたはツールコードをAgentCore Runtime上で実行できるように準備します。

コードをAgentCore標準化されたHTTPプロトコルまたはMCPプロトコルコントラクトに変換し、従来のリクエスト/レスポンスパターン（HTTPプロトコル）の直接REST APIエンドポイント通信、またはツールおよびエージェントサーバー用のModel Context Protocol（MCPプロトコル）を可能にします。

ツールをホスティングする際、Amazon Bedrock AgentCore Python SDKは[セッション分離](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#session-management)のための`MCP-Session-Id`ヘッダーを使用して[Stateless Streamable HTTP](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#stateless-streamable-http)トランスポートプロトコルを実装します。サーバーは、プラットフォームが生成したMcp-Session-Idヘッダーを拒否しないように、ステートレス操作をサポートする必要があります。
MCPサーバーはポート`8000`でホスティングされ、1つの呼び出しパス`mcp-POST`を提供します。この対話エンドポイントはMCP RPCメッセージを受信し、ツールの機能を通じて処理します。レスポンスのコンテンツタイプとして`application/json`と`text/event-stream`の両方をサポートします。

AgentCoreプロトコルをMCPに設定すると、AgentCore RuntimeはMCPサーバーコンテナがパス`0.0.0.0:8000/mcp`上にあることを期待します。これは、公式のMCPサーバーSDKのほとんどがサポートするデフォルトパスです。

AgentCore Runtimeは、デフォルトでセッション分離を提供し、それがないリクエストに対して自動的にMcp-Session-Idヘッダーを追加するため、ステートレスストリーミング可能なHTTPサーバーをホスティングする必要があります。これにより、MCPクライアントは同じBedrock AgentCore RuntimeセッションIDへの接続の継続性を持つことができます。

`InvokeAgentRuntime` APIのペイロードは完全にパススルーされるため、MCPのようなプロトコルのRPCメッセージを簡単にプロキシできます。

このチュートリアルでは、以下を学習します：

* ツール付きのMCPサーバーの作成方法
* サーバーのローカルテスト方法
* AWSへのサーバーのデプロイ方法
* デプロイされたサーバーの呼び出し方法

### チュートリアルの詳細

| 情報               | 詳細                                                       |
|:-------------------|:-----------------------------------------------------------|
| チュートリアルタイプ | ツールのホスティング                                       |
| ツールタイプ       | MCPサーバー                                                |
| チュートリアル構成要素 | AgentCore Runtime上でのツールのホスティング。MCPサーバーの作成 |
| チュートリアル垂直領域 | クロス垂直領域                                             |
| 例の複雑さ         | 簡単                                                       |
| 使用SDK            | Amazon BedrockAgentCore Python SDKおよびMCP Client         |

### チュートリアルアーキテクチャ
このチュートリアルでは、既存のMCPサーバーをAgentCore runtimeにデプロイする方法について説明します。

デモンストレーションの目的で、3つのツールを持つ非常にシンプルなMCPサーバーを使用します：`add_numbers`、`multiply_numbers`、`greet_users`

![MCPアーキテクチャ](images/hosting_mcp_server.png)

### チュートリアルの主な機能

* MCPサーバーのホスティング
