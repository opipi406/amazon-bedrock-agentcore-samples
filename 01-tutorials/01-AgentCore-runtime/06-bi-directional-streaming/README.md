# Amazon Bedrock AgentCore - 双方向WebSocketサンプル

このリポジトリには、Amazon Bedrock AgentCoreとの双方向WebSocket通信を実証するサンプル実装が含まれています：

- **Sonic** - AgentCoreに直接デプロイされるネイティブAmazon Nova Sonic Python WebSocket実装。直接イベント処理によるNova Sonicプロトコルの完全な制御を提供します。音声選択と割り込みサポートを備えたリアルタイム音声会話をテストするためのWebクライアントが含まれています。

- **Strands** - 簡略化されたリアルタイム音声会話のためにStrands BidiAgentを使用した高レベルフレームワーク実装。自動セッション管理、ツール統合、合理化されたAPIを備えたNova Sonic上に構築されています。フレームワーク抽象化の恩恵を受ける迅速なプロトタイピングと本番アプリケーションに最適です。

- **Echo** - AI機能なしでWebSocket接続と認証をテストするためのシンプルなエコーサーバー。

すべてのサンプルは、ルートの`setup.sh`と`cleanup.sh`スクリプトを通じて統一されたセットアップとクリーンアッププロセスを使用します。

## 前提条件

- 適切な権限で設定されたAWS CLI
- Python 3.12+
- Docker（カスタムエージェントイメージをビルドするため）
- AWSアカウントID

---

## Sonicサンプル - ネイティブNova Sonic 2実装

このサンプルは、**ネイティブAmazon Nova Sonic 2 Python WebSocketサーバー**をAgentCoreに直接デプロイします。直接イベント処理によるNova Sonicプロトコルの完全な制御を提供し、セッション管理、オーディオストリーミング、応答生成の完全な可視性を提供します。

**アーキテクチャ：**

![AgentCore Sonic Architecture](./images/agentcore-sonic-architecture.png)

**最適な用途：** セッション管理とイベント処理のきめ細かい制御を必要とするリアルタイム音声会話の本番アプリケーション。

### セットアップ

```bash
# 必須
export ACCOUNT_ID=your_aws_account_id

# オプション - これらをカスタマイズするか、デフォルトを使用
export AWS_REGION=us-east-1
export IAM_ROLE_NAME=WebSocketSonicAgentRole
export ECR_REPO_NAME=agentcore_sonic_images
export AGENT_NAME=websocket_sonic_agent

# AWS認証（いずれかの方法を選択）：

# 方法1: AWSプロファイルを使用（推奨）
# AWS_PROFILE環境変数を設定するか、デフォルトプロファイルに適切なアクセス権があることを確認
export AWS_PROFILE=your_profile_name

# 方法2: AWS認証情報を直接使用
# export AWS_ACCESS_KEY_ID=your_access_key
# export AWS_SECRET_ACCESS_KEY=your_secret_key
# export AWS_SESSION_TOKEN=your_session_token  # オプション、一時的な認証情報の場合

# セットアップを実行
./setup.sh sonic
```

### クライアントの実行

**オプション1: スタートスクリプトを使用（推奨）**
```bash
./start_client.sh sonic
```

**オプション2: 手動起動**
```bash
# 環境変数をエクスポート（セットアップ出力から）
export AWS_REGION="us-east-1"

# AWS認証（いずれかの方法を選択）：
# AWS_PROFILE環境変数を設定するか、デフォルトプロファイルに適切なアクセス権があることを確認
export AWS_PROFILE=your_profile_name
# または
# export AWS_ACCESS_KEY_ID=your_access_key
# export AWS_SECRET_ACCESS_KEY=your_secret_key
# export AWS_SESSION_TOKEN=your_session_token  # オプション

# Webクライアントを起動
python sonic/client/client.py --runtime-arn "<agent-arn-from-setup>"
```

Webクライアントは以下を実行します：
1. ブラウザで自動的に開く
2. マイクへのアクセスを要求
3. AIとのリアルタイム音声会話を有効化

### 機能

- **リアルタイムオーディオストリーミング** - 自然に話しかけて即座に応答を得る
- **音声選択** - 複数の言語（英語、フランス語、イタリア語、ドイツ語、スペイン語）から複数の音声を選択
- **動的音声切り替え** - アクティブな会話中に音声を変更
- **割り込みサポート** - アシスタントの応答中に割り込むバージイン機能
- **ツール統合** - 「今何時ですか？」や「今日は何日ですか？」などの質問に応答するサンプル`getDateTool`を含む
- **WebベースのUI** - インストール不要、任意のモダンブラウザで動作
- **セッション管理** - 自動セッション処理とオーディオバッファリング
- **イベントログ** - フィルタリング機能付きでリアルタイムにすべてのWebSocketイベントを表示

### サンプルツール: getDateTool

Sonic実装には、ツール統合の動作例が含まれています。`getDateTool`は以下を実証します：
- クライアント設定でツールを定義する（[`sonic/client/sonic-client.html`](sonic/client/sonic-client.html#L617-L628)）
- セッションセットアップ中にツール設定を送信する（[`sonic/client/sonic-client.html`](sonic/client/sonic-client.html#L773-L784)）
- サーバーでツール呼び出しを処理する（[`sonic/websocket/s2s_session_manager.py`](sonic/websocket/s2s_session_manager.py#L339-L342)）
- 結果を会話フローに戻す

**試してみる：** 「今何時ですか？」や「今日の日付は？」などの質問をすると、アシスタントがツールを呼び出して現在のUTC日時を取得します。

### クリーンアップ

```bash
./cleanup.sh sonic
```

---

## Strandsサンプル - フレームワークベースの実装

このサンプルは、Amazon Nova Sonicを使用したリアルタイム音声会話のために**Strands BidiAgentフレームワーク**を使用することを実証します。Strandsは、双方向ストリーミング、自動セッション管理、ツール統合を簡素化する高レベル抽象化を提供します。

**アーキテクチャ：**

Strands実装は、BidiAgentフレームワークを使用して、WebSocket通信、オーディオストリーミング、ツールオーケストレーションの複雑さを自動的に処理します。

**最適な用途：** 完全なNova Sonic機能を維持しながら、フレームワーク抽象化の恩恵を受ける迅速なプロトタイピングと本番アプリケーション。

### セットアップ

```bash
# 必須
export ACCOUNT_ID=your_aws_account_id

# オプション - これらをカスタマイズするか、デフォルトを使用
export AWS_REGION=us-east-1
export IAM_ROLE_NAME=WebSocketStrandsAgentRole
export ECR_REPO_NAME=agentcore_strands_images
export AGENT_NAME=websocket_strands_agent

# AWS認証（いずれかの方法を選択）：

# 方法1: AWSプロファイルを使用（推奨）
# AWS_PROFILE環境変数を設定するか、デフォルトプロファイルに適切なアクセス権があることを確認
export AWS_PROFILE=your_profile_name

# 方法2: AWS認証情報を直接使用
# export AWS_ACCESS_KEY_ID=your_access_key
# export AWS_SECRET_ACCESS_KEY=your_secret_key
# export AWS_SESSION_TOKEN=your_session_token  # オプション、一時的な認証情報の場合

# セットアップを実行
./setup.sh strands
```

### クライアントの実行

**オプション1: スタートスクリプトを使用（推奨）**
```bash
./start_client.sh strands
```

**オプション2: 手動起動**
```bash
# 環境変数をエクスポート（セットアップ出力から）
export AWS_REGION="us-east-1"

# AWS認証（いずれかの方法を選択）：
# AWS_PROFILE環境変数を設定するか、デフォルトプロファイルに適切なアクセス権があることを確認
export AWS_PROFILE=your_profile_name
# または
# export AWS_ACCESS_KEY_ID=your_access_key
# export AWS_SECRET_ACCESS_KEY=your_secret_key
# export AWS_SESSION_TOKEN=your_session_token  # オプション

# Webクライアントを起動
python strands/client/client.py --runtime-arn "<agent-arn-from-setup>"
```

Webクライアントは以下を実行します：
1. ブラウザで自動的に開く
2. マイクへのアクセスを要求
3. AIとのリアルタイム音声会話を有効化

### サンプルツール: 電卓

Strands実装には、フレームワークベースのツール統合を実証する電卓ツールが含まれています。このツールは基本的な算術演算を実行できます。

**試してみる：** 「25かける4は？」や「100を5で割った値を計算して」などの質問をすると、アシスタントが電卓ツールを使用します。

### Sonicサンプルとの主な違い

- **抽象化レベル：** Strandsは高レベルAPIを提供し、Sonicは直接プロトコル制御を提供
- **コードの複雑さ：** Strandsはセッション管理のボイラープレートが少ない
- **ツール統合：** フレームワークがツールオーケストレーションを自動的に処理
- **柔軟性：** Sonicはイベントと応答のよりきめ細かい制御を提供

### クリーンアップ

```bash
./cleanup.sh strands
```

---

## Echoサンプル - WebSocketテスト

WebSocket接続と認証をテストするためのシンプルなエコーサーバー。

### セットアップ

```bash
# 必須
export ACCOUNT_ID=your_aws_account_id

# オプション - これらをカスタマイズするか、デフォルトを使用
export AWS_REGION=us-east-1
export IAM_ROLE_NAME=WebSocketEchoAgentRole
export DOCKER_REPO_NAME=agentcore_echo_images
export AGENT_NAME=websocket_echo_agent

# AWS認証（いずれかの方法を選択）：

# 方法1: AWSプロファイルを使用（推奨）
# AWS_PROFILE環境変数を設定するか、デフォルトプロファイルに適切なアクセス権があることを確認
export AWS_PROFILE=your_profile_name

# 方法2: AWS認証情報を直接使用
# export AWS_ACCESS_KEY_ID=your_access_key
# export AWS_SECRET_ACCESS_KEY=your_secret_key
# export AWS_SESSION_TOKEN=your_session_token  # オプション、一時的な認証情報の場合

# セットアップを実行
./setup.sh echo
```

### クライアントの実行

**オプション1: スタートスクリプトを使用（推奨）**
```bash
./start_client.sh echo
```

**オプション2: 手動起動**
```bash
# 環境変数をエクスポート（セットアップ出力から）
export AWS_REGION="us-east-1"

# AWS認証（いずれかの方法を選択）：
# AWS_PROFILE環境変数を設定するか、デフォルトプロファイルに適切なアクセス権があることを確認
export AWS_PROFILE=your_profile_name
# または
# export AWS_ACCESS_KEY_ID=your_access_key
# export AWS_SECRET_ACCESS_KEY=your_secret_key
# export AWS_SESSION_TOKEN=your_session_token  # オプション

# SigV4ヘッダー認証でテスト
python echo/client/client.py --runtime-arn "<agent-arn-from-setup>" --auth-type headers

# SigV4クエリパラメータでテスト
python echo/client/client.py --runtime-arn "<agent-arn-from-setup>" --auth-type query
```

### 機能

- **シンプルなエコー** - メッセージを送信してエコー応答を検証
- **複数の認証方法** - SigV4ヘッダーまたはクエリパラメータをテスト
- **接続テスト** - WebSocket接続を検証
- **最小限の依存関係** - デバッグに最適

### 期待される出力

```
WebSocket connected
Sent: {"msg": "Hello, World! Echo Test"}
Received: {"msg": "Hello, World! Echo Test"}
Echo test PASSED
```

### クリーンアップ

```bash
./cleanup.sh echo
```

---

## デプロイメントの仕組み

`setup.sh`スクリプトは完全なデプロイメントを自動化します：

1. **前提条件のチェック** - jq、Python 3、Docker、AWS CLIがインストールされていることを検証
2. **Python環境** - 仮想環境を作成して依存関係をインストール
3. **Dockerビルドとプッシュ** - ARM64コンテナイメージをビルドしてAmazon ECRにプッシュ
4. **IAMロール** - ECR、CloudWatch、Bedrock、X-Rayの権限を持つロールを作成
5. **エージェントランタイム** - WebSocketサーバーをBedrock AgentCoreにデプロイ
6. **設定** - クリーンアップのためにデプロイメント詳細を`setup_config.json`に保存

デプロイメント後、ECRリポジトリ、IAMロール、実行中のエージェントランタイム、および簡単なクリーンアップのための設定ファイルが作成されます。

---

## ファイル構造

```
.
├── setup.sh                       # 統一セットアップスクリプト（フォルダパラメータを受け取る）
├── start_client.sh                # 統一クライアント起動スクリプト（フォルダパラメータを受け取る）
├── cleanup.sh                     # 統一クリーンアップスクリプト（フォルダパラメータを受け取る）
├── requirements.txt               # Python依存関係
├── websocket_helpers.py           # 共有WebSocketユーティリティ（SigV4認証、事前署名付きURL）
├── agent_role.json               # IAMロールポリシーテンプレート
├── trust_policy.json             # IAM信頼ポリシー
│
├── sonic/                        # Sonicサンプル（ネイティブ実装）
│   ├── client/                   # Webベースのクライアント
│   │   ├── sonic-client.html     # 音声選択付きHTML UI
│   │   ├── client.py             # Webサーバー
│   │   └── requirements.txt      # クライアント依存関係
│   ├── websocket/                # サーバー実装
│   │   ├── server.py             # Sonic WebSocketサーバー
│   │   ├── s2s_session_manager.py # セッション管理
│   │   ├── s2s_events.py         # イベント処理
│   │   ├── Dockerfile            # コンテナ定義
│   │   └── requirements.txt      # サーバー依存関係
│   └── setup_config.json         # setup.shによって生成
│
├── strands/                      # Strandsサンプル（フレームワークベース）
│   ├── client/                   # Webベースのクライアント
│   │   ├── strands-client.html   # HTML UI
│   │   ├── client.py             # Webサーバー
│   │   └── requirements.txt      # クライアント依存関係
│   ├── websocket/                # サーバー実装
│   │   ├── server.py             # Strands BidiAgentサーバー
│   │   ├── Dockerfile            # コンテナ定義
│   │   └── requirements.txt      # サーバー依存関係
│   └── setup_config.json         # setup.shによって生成
│
└── echo/                         # Echoサンプル（テスト）
    ├── client/                   # CLIクライアント
    │   └── client.py             # Echoテストクライアント
    ├── websocket/                # サーバー実装
    │   ├── server.py             # Echo WebSocketサーバー
    │   ├── Dockerfile            # コンテナ定義
    │   └── requirements.txt      # サーバー依存関係
    └── setup_config.json         # setup.shによって生成
```

---
