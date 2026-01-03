# Amazon Bedrock AgentCore Runtime で OpenAI モデルを使用した Strands Agents のホスティング

## 概要

このチュートリアルでは、Amazon Bedrock AgentCore Runtime を使用して既存のエージェントをホスティングする方法を学習します。

OpenAI モデルを使用した Strands Agents の例に焦点を当てます。Amazon Bedrock モデルを使用した Strands Agents については[こちら](../01-strands-with-bedrock-model)を確認してください。
Amazon Bedrock モデルを使用した LangGraph については[こちら](../02-langgraph-with-bedrock-model)を確認してください。

### チュートリアルの詳細

| 情報                     | 詳細                                                                  |
|:-------------------------|:----------------------------------------------------------------------|
| チュートリアルタイプ       | 会話型                                                                |
| エージェントタイプ         | 単一                                                                  |
| エージェントフレームワーク | Strands Agents                                                       |
| LLM モデル               | GPT 4.1 mini                                                          |
| チュートリアルコンポーネント | AgentCore Runtime でのエージェントのホスティング。Strands Agent と OpenAI モデルの使用 |
| チュートリアル垂直領域     | クロス垂直                                                            |
| 例の複雑さ               | 簡単                                                                  |
| 使用 SDK                 | Amazon BedrockAgentCore Python SDK と boto3                          |

### チュートリアルアーキテクチャ

このチュートリアルでは、既存のエージェントを AgentCore runtime にデプロイする方法について説明します。

デモンストレーションの目的で、Amazon Bedrock モデルを使用する Strands Agent を使用します。

この例では、`get_weather` と `get_time` の2つのツールを持つ非常にシンプルなエージェントを使用します。

<div style="text-align:left">
    <img src="images/architecture_runtime.png" width="100%"/>
</div>

### チュートリアルの主な機能

* Amazon Bedrock AgentCore Runtime でのエージェントのホスティング
* OpenAI モデルの使用
* Strands Agents の使用
