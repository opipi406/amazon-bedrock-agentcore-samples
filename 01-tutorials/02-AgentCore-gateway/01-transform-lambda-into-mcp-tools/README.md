# GatewayのためのLambda関数ツールの実装

## 概要
Bedrock AgentCore Gatewayは、お客様が既存のLambda関数をフルマネージドなMCPサーバーとして運用できるようにするサービスです。インフラやホスティングの管理が不要で、既存のAWS Lambda関数をそのまま利用したり、新たにツール用のLambda関数を追加することもできます。Gatewayは、これらすべてのツールに対して統一されたModel Context Protocol (MCP) インターフェースを提供します。  
Gatewayは、インバウンド認証とアウトバウンド認証の二重認証モデルを採用しており、リクエストの受け入れとバックエンドリソースへの安全な接続の両方でアクセス制御を実現します。インバウンド認証はGatewayターゲットへのアクセスを試みるユーザーの検証・認可を担い、アウトバウンド認証は認証済みユーザーの代理としてバックエンドリソースへの安全な接続を実施します。この二つの認証メカニズムにより、IAM認証情報とOAuthベースの認証フローの両方をサポートしたユーザーとターゲットリソース間の安全な橋渡しが実現します。

![仕組みの図](images/lambda-iam-gateway.png)

![仕組みの図](images/lambda-gw-iam-inbound.png)


### Lambda contextオブジェクトの理解
GatewayがLambda関数を呼び出す際、特別なコンテキスト情報を`context.client_context`オブジェクト経由で渡します。このコンテキストには呼び出しに関する重要なメタデータが含まれており、関数内でリクエスト処理の判定に利用できます。  
`context.client_context.custom`オブジェクトで利用可能なプロパティは以下の通りです：
* bedrockagentcoreEndpointId: リクエストを受け取ったGatewayエンドポイントのID
* bedrockagentcoreTargetId: Lambda関数へルーティングしたGatewayターゲットのID
* bedrockagentcoreMessageVersion: このリクエストで使用されているメッセージフォーマットのバージョン
* bedrockagentcoreToolName: 呼び出されたツール名。Lambda関数が複数のツールとして実装されている場合に特に重要です
* bedrockagentcoreSessionId: 現在の呼び出しのセッションID。セッション内の複数のツール呼び出しを関連付ける際に利用できます

これらのプロパティはLambda関数のコード内でアクセスでき、呼び出されたツールの判別や、関数の動作のカスタマイズに活用できます。

![lambda-context-objectのイメージ](images/lambda-context-object.png)

### レスポンス形式とエラーハンドリング

Lambda関数は、Gatewayがクライアントへ戻せるように、決まったフォーマットのレスポンスを返す必要があります。レスポンスは以下の構造のJSONオブジェクトとしてください。  
`statusCode` フィールドには、処理結果を示すHTTPステータスコードを設定してください：
* 200: 成功
* 400: 不正リクエスト（クライアントエラー）
* 500: サーバー内部エラー

`body` フィールドは文字列でもJSON文字列（より複雑なレスポンスを渡す場合）でも構いません。構造化したレスポンスを返したい場合は、JSON文字列にシリアライズしてください。

### エラーハンドリング
適切なエラーハンドリングは、クライアントへ有益なフィードバックを返すために重要です。Lambda関数では例外をキャッチし、適切なエラーレスポンスを返すようにしてください。

### テストについて

```__context__```フィールドは、本番環境でGatewayから渡されるイベントには含まれません。これはテスト時にコンテキストオブジェクトをシミュレーションするためのものです。  
Lambdaコンソールでテストする際は、テスト用コンテキストの扱いに対応したコード修正が必要です。これにより、Gatewayターゲットとしてデプロイする前に様々なツール名や入力パラメータでLambda関数の動作テストが可能になります。

### クロスアカウントLambdaアクセス

Lambda関数がGatewayとは別のAWSアカウントに存在する場合、GatewayがLambda関数を呼び出せるようリソースベースポリシーの設定が必要です。以下はその例です：

```
{
  "Version": "2012-10-17",
  "Id": "default",
  "Statement": [
    {
      "Sid": "cross-account-access",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/GatewayExecutionRole"
      },
      "Action": "lambda:InvokeFunction",
      "Resource": "arn:aws:lambda:us-west-2:987654321098:function:MyLambdaFunction"
    }
  ]
}
```
ポリシー内の各項目の意味は以下の通りです：
- 123456789012：GatewayがデプロイされているアカウントのID
- GatewayExecutionRole：Gatewayで利用されるIAMロール名
- 987654321098：Lambda関数がデプロイされているアカウントのID
- MyLambdaFunction：Lambda関数の名前

このポリシーを追加後、異なるアカウント間でもGatewayターゲット設定時にLambda関数のARNを指定できます。

### チュートリアル詳細

| 情報                 | 詳細                                                         |
|:---------------------|:-----------------------------------------------------------|
| チュートリアルタイプ   | インタラクティブ                                            |
| AgentCoreコンポーネント| AgentCore Gateway, AgentCore Identity, AWS IAM             |
| エージェントフレームワーク | Strands Agents                                         |
| LLMモデル             | Anthropic Claude Haiku 4.5, Amazon Nova Pro              |
| チュートリアル構成要素 | AgentCore Gatewayの作成と呼び出し                        |
| チュートリアル業種     | クロスバーティカル                                         |
| サンプルの複雑さ      | イージー（簡単）                                           |
| 使用SDK               | boto3                                                      |

## チュートリアルアーキテクチャ

### チュートリアルの主な特徴

* Lambda関数をMCPツールとして公開
* OAuthおよびIAMによるツール呼び出しのセキュア化

## チュートリアルの概要

本チュートリアルでは次の機能について説明します。

- [OAuthインバウンド認証でAWS Lambda関数をMCPツールに変換する方法](01-gateway-target-lambda-oauth.ipynb)

- [AWS IAMインバウンド認証でAWS Lambda関数をMCPツールに変換する方法](02-gateway-target-lambda-iam.ipynb)
