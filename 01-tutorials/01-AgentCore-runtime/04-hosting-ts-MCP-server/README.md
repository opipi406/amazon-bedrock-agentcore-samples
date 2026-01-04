# Amazon Bedrock AgentCore 上の TypeScript MCP サーバー

## 概要

このチュートリアルでは、Amazon Bedrock AgentCore ランタイム環境を使用して TypeScript ベースの MCP（Model Context Protocol）サーバーをホストする方法を説明します。


### チュートリアルの詳細

| 情報               | 詳細                                                       |
|:-------------------|:-----------------------------------------------------------|
| チュートリアルタイプ | TypeScript MCP サーバーのホスティング                      |
| ツールタイプ       | MCP サーバー                                                |
| チュートリアル構成要素 | AgentCore Runtime 上での TypeScript MCP サーバーのホスティング |
| チュートリアル垂直領域 | クロス垂直領域                                              |
| 例の複雑さ         | 簡単                                                        |
| 使用 SDK           | Anthropic の MCP 用 TypeScript SDK                         |

## 前提条件

- Node.js v22 以降  
- Docker（コンテナ化用）  
- Docker イメージを保存するための Amazon ECR（Elastic Container Registry）  
- Bedrock AgentCore へのアクセス権を持つ AWS アカウント  

---

## AgentCore Runtime サービス契約

[公式サービス契約ドキュメント](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-service-contract.html)を参照してください。

**ランタイム設定:**
- **ホスト:** `0.0.0.0`  
- **ポート:** `8000`  
- **トランスポート:** ステートレス `streamable-http`  
- **エンドポイントパス:** `POST /mcp`  

## ローカル開発

1. 依存関係のインストール

```
npm install
```

2. AWS 認証情報の設定
```
aws configure
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_REGION=us-east-1
```

3. サーバーの起動
```
npm run start
```

4. [MCP inspector](https://github.com/modelcontextprotocol/inspector) を使用してローカルでテスト

```
npx @modelcontextprotocol/inspector
```

## Docker デプロイメント

1. ECR リポジトリの作成
```
aws ecr create-repository --repository-name mcp-server --region us-east-1
```
2. ECR へのイメージのビルドとプッシュ
```
# ログイントークンの取得
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin [account-id].dkr.ecr.us-east-1.amazonaws.com

docker buildx --platform linux/arm64 \
  -t [account-id].dkr.ecr.us-east-1.amazonaws.com/mcp-server:latest --push .
```

3. Bedrock AgentCore へのデプロイ

    - AWS コンソール → Bedrock → AgentCore → Create Agent に移動
    - プロトコルとして MCP を選択
    - Agent Runtime の設定:
        - Image URI: [account-id].dkr.ecr.us-east-1.amazonaws.com/mcp-server:latest
        - Bedrock モデルアクセス用の IAM 権限を設定
        - Agent Sandbox でデプロイしてテスト


4. エンコードされた ARN MCP URL の構築

```
echo "agent_arn" | sed 's/:/%3A/g; s/\//%2F/g'
```

```
https://bedrock-agentcore.{region}.amazonaws.com/runtimes/{encoded_arn}/invocations?qualifier=DEFAULT
```

5. [MCP inspector](https://github.com/modelcontextprotocol/inspector) で MCP URL を使用します。

## 参考文献
- https://aws.amazon.com/bedrock/agentcore/
- https://github.com/modelcontextprotocol/typescript-sdk
- https://github.com/modelcontextprotocol/inspector


