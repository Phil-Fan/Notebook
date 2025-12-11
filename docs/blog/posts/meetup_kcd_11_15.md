---
comments: true
authors:
  - Phil-Fan
categories:
  - Meeting
tags:
  - meeting
date:
  created: 2025-11-15
nostatistics: true
---


# AI/ML 分会场

## dynamic.ai

DRA dynamic resource allocation

- 粒度精确到卡，如果放小模型，显存利用率低（～5%）
- 小模型在垂直领域更稳定幻觉更少
- AWS：提供粒度为半卡的调度。痛点：还是太大了

dynamia.ai：异构 GPU 资源调度 (主要负责南北向流量的资源申请)

- 调度器层：调度器扩展
- 容器层：hami core 符号劫持

volcano

- 也使用 hami core
- 任务级调度能力较优

## multi-agent

Why agent: LLM is certainly the main application is the trend of AI

- Function call is a turning point where we can use some existing tools
- Modern agents:
  - Task decomposition
  - Tools selection
  - Memory
  - Multi-agent

[strands-agents](https://github.com/strands-agents): an OSS given by AWS

- built-in tools: python tools; MCP tools; pre-built tools;
- a large set of tools with better support and intergration for cloud services
- support multiple types of model

Orchestrator: agents as tools, with every

- agent graph: concat some tools into a bigger part
- graph vs workflow

swarm mode: decentralized; share context

## Structured out

put & func call in vLLM

- choice：`choice = ["red","green"]`
- regex: json schema
- son
- grammar
- sql
- EBNF / Lark grammars

中间输出 json

- structural tag

guided output 的 CPU bubble 问题

### 原理

- 在 sampler 中把不符合要求的去除
- 状态机跟踪某个时间点哪些 token 是合规的

### tool parser

template 渲染

## RoleBasedGroup

1. 迭代性：PD 分离一定是未来的架构吗？extensive
2. 有状态性：
3. 运行可靠

RBG 是面向多角色协同场景设计的工作负载

- 多角色的创建、调度、升级、故障自愈、服务发现

## 蚂蚁：Gateway API inference extension GIE

什么是云原生

什么是
`

genai-bench

llm-optimizer
SLO

goodput 的理念：满足 SLO 约束的

GuideLLM from vllm

stepfun 的论文

计数器

sglang roter

AIGW

业务架构还没有收敛，基础架构
