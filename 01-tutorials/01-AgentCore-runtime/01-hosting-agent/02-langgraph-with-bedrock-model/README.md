# Amazon Bedrock AgentCore Runtime で Amazon Bedrock モデルを使用した LangGraph エージェントのホスティング

## 概要

このチュートリアルでは、Amazon Bedrock AgentCore Runtime を使用して既存のエージェントをホスティングする方法を学習します。

Amazon Bedrock モデルを使用した LangGraph の例に焦点を当てます。Amazon Bedrock モデルを使用した Strands Agents については[こちら](../01-strands-with-bedrock-model)を確認してください。
OpenAI モデルを使用した Strands Agents については[こちら](../03-strands-with-openai-model)を確認してください。

### チュートリアルの詳細

| 情報                     | 詳細                                                                      |
|:-------------------------|:-------------------------------------------------------------------------|
| チュートリアルタイプ       | 会話型                                                                    |
| エージェントタイプ         | 単一                                                                      |
| エージェントフレームワーク | LangGraph                                                                |
| LLM モデル               | Anthropic Claude Haiku 4.5                                                |
| チュートリアルコンポーネント | AgentCore Runtime でのエージェントのホスティング。LangGraph と Amazon Bedrock モデルの使用 |
| チュートリアル垂直領域     | クロス垂直                                                                 |
| 例の複雑さ               | 簡単                                                                      |
| 使用 SDK                 | Amazon BedrockAgentCore Python SDK と boto3                              |

### チュートリアルアーキテクチャ

このチュートリアルでは、既存のエージェントを AgentCore runtime にデプロイする方法について説明します。

デモンストレーションの目的で、Amazon Bedrock モデルを使用する LangGraph エージェントを使用します。

この例では、`get_weather` と `get_time` の2つのツールを持つ非常にシンプルなエージェントを使用します。

<div style="text-align:left">
    <img src="images/architecture_runtime.png" width="100%"/>
</div>

### チュートリアルの主な機能

* Amazon Bedrock AgentCore Runtime でのエージェントのホスティング
* Amazon Bedrock モデルの使用
* LangGraph の使用
