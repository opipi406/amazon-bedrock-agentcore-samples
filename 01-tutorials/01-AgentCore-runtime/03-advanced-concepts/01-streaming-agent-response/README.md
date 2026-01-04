# Amazon Bedrock AgentCore Runtime での Strands Agents と Amazon Bedrock モデルを使用したストリーミング応答

## 概要

このチュートリアルでは、既存のエージェントを使用して Amazon Bedrock AgentCore Runtime でストリーミング応答を実装する方法を学習します。

リアルタイムストリーミング機能を示す、Amazon Bedrock モデルを使用した Strands Agents の例に焦点を当てます。

### チュートリアルの詳細

| 情報         | 詳細                                                                          |
|:--------------------|:---------------------------------------------------------------------------------|
| チュートリアルタイプ       | ストリーミング付き会話型                                                    |
| エージェントタイプ          | 単一                                                                           |
| エージェントフレームワーク   | Strands Agents                                                                   |
| LLM モデル           | Anthropic Claude Haiku 4.5                                                      |
| チュートリアルコンポーネント | AgentCore Runtime を使用したストリーミング応答。Strands Agent と Amazon Bedrock Model の使用 |
| チュートリアル垂直領域   | クロス垂直                                                                   |
| 例の複雑さ  | 簡単                                                                             |
| 使用するSDK            | Amazon BedrockAgentCore Python SDK と boto3                                     |

### チュートリアルアーキテクチャ

このチュートリアルでは、ストリーミングエージェントを AgentCore runtime にデプロイする方法について説明します。

デモンストレーションの目的で、ストリーミング機能を備えた Amazon Bedrock モデルを使用する Strands Agent を使用します。

この例では、`get_weather`、`get_time`、`calculator` の3つのツールを持つシンプルなエージェントを使用しますが、リアルタイムストリーミング応答機能が強化されています。

<div style="text-align:left">
    <img src="images/architecture_runtime.png" width="100%"/>
</div>

### チュートリアルの主な機能

* Amazon Bedrock AgentCore Runtime でのストリーミング応答の実装
* Server-Sent Events (SSE) を使用したリアルタイム部分結果配信
* ストリーミング機能を備えた Amazon Bedrock モデルの使用
* 非同期ストリーミングサポートを備えた Strands Agents の使用
* 段階的な応答表示によるユーザー体験の向上
