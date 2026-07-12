---
status: new
--- 

# 04 | SFT

## 原理

1. 基础模型 (Pre-trained Model): 首先，我们有一个经过“预训练”的大语言模型（如 LLaMA, Mistral, Qwen 等）。这个模型通过在海量无标签的文本数据上学习，已经掌握了语言的语法、事实知识、基本推理能力，但它还不知道如何与人“对话”或精确地遵循指令。它像一个知识渊博但未经社会化的学者。
2. 高质量的“指令 - 回答”数据：SFT 的关键在于数据。我们需要一个高质量、人工标注的“指令 - 回答”（Instruction-Response）或“提问 - 回答”（Prompt-Completion）数据集。每一条数据都包含一个我们希望模型响应的输入，以及一个理想的、高质量的输出范例。

    ```json
    {
      "instruction": "请用三句话解释什么是人工智能。",
      "output": "人工智能是计算机科学的一个分支，它研究如何让机器像人一样思考和学习。它涵盖了机器学习、自然语言处理等多个领域。最终目标是创造出能够执行复杂任务的智能体。"
    }
    ```

3. 训练过程：模型接收数据集中的 "instruction" 部分作为输入，模型会生成一个自己的回答，训练算法（如反向传播）会比较模型的回答和数据集中预设的标准答案 "output" 之间的差异（计算损失 Loss，如最小化交叉熵损失），算法会微调模型的内部参数（权重），使得模型下一次再遇到类似的指令时，其生成的回答能更接近标准答案。

## 选择

- 只能解决正确性的问题
- 无法解决安全性：比如训练数据说“糖尿病人不能吃糖”，但是询问模型是否可以吃巧克力，模型回答“糖尿病人可以少量摄入”

## 相关工作

- InstructGPT (OpenAI, 2022) - Training language models to follow instructions with human feedback
  - 贡献：这篇论文正式提出了“对齐”的概念，并开创性地提出了 SFT -> RM -> RLHF 的三阶段训练流程，这成为了后续所有类 ChatGPT 模型的基础范式。SFT 作为第一步，其重要性被充分证明。
- FLAN (Google, 2021) - Finetuned Language Models are Zero-Shot Learners
  - 贡献：证明了通过在大量不同类型的指令任务上对模型进行微调，可以极大地提升模型在从未见过的任务上的“零样本”泛化能力。它验证了“指令微调”这条路的巨大潜力。
- LoRA (Microsoft, 2021) - LoRA: Low-Rank Adaptation of Large Language Models
  - 贡献：提出了 LoRA 方法，完美解决了全量微调的资源困境，使得在单张消费级显卡上微调大模型成为可能，极大地推动了开源社区的发展。
- Alpaca (Stanford, 2023) - Alpaca: A Strong, Replicable Instruction-Following Model
  - 贡献：这虽然不是一篇正式论文，但其影响力巨大。它证明了只需使用少量高质量的指令数据（约 5.2 万条，由 GPT-3.5 生成），并采用 LoRA 方法对 LLaMA 这样优秀的开源底座模型进行 SFT，就能达到惊人好的指令遵循效果。它引爆了开源模型的“指令微调”浪潮。

## llama-factory 使用记录

!!! note "Llama-factory"
    Llama-factory 是一个用于大规模语言模型（LLM）训练和推理的框架。它提供了一套工具和接口，简化了从数据准备到模型部署的整个流程。Llama-factory 支持多种模型架构和数据集，允许用户根据自己的需求进行定制和扩展。通过集成的 WebUI，用户可以方便地管理模型训练过程，调整参数，并实时监控训练进度和性能指标。此外，Llama-factory 还支持分布式训练和推理，能够有效利用多台机器的计算资源，提高模型的训练效率和推理速度。

### 安装与使用

- 中文教程[安装 - LLaMA Factory](https://llamafactory.readthedocs.io/zh-cn/latest/getting_started/installation.html)
- [LLaMA-Factory 微调教程】LoRA 微调 改变大模型的自我认知 - 知乎](https://zhuanlan.zhihu.com/p/24909312513)

[Llamafactory](https://llamafactory.readthedocs.io/zh-cn/latest/index.html)

[llama-factory SFT 系列教程 (二)，大模型在自定义数据集 lora 训练与部署_llama-factory 自定义数据集-CSDN 博客](https://blog.csdn.net/sjxgghg/article/details/137656248?spm=1001.2014.3001.5502)

这里使用 AutoDL 上的社区镜像

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112920092478120&bvid=BV1a3aQeuEou&cid=500001641377964&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

### 实战记录 —— 微调 qwen 实现 Multi30K 下英译德翻译模型

使用的是 Multi30K 数据集，下载地址：<https://github.com/neychev/small_DL_repo/tree/master/datasets/Multi30k>

#### 下载模型

下载`Qwen2.5-7B-Instruct`模型，放在`/root/Qwen2.5-7B-Instruct`下

#### 准备数据

根据 sft 的格式，整理数据，按照 instruction, input, output 格式

```json title="整理数据，按照instruction, input, output格式"
{
    "instruction": "Translate the following English text to German.", 
    "input": "Two young, White males are outside near many bushes.", 
    "output": "Zwei junge weiße Männer sind im Freien in der Nähe vieler Büsche."
}
```

### 开启 webui

开启 webui 之后，操作比较简单，只需要选择对应的模型，修改参数，填写对应路径，即可进行训练
![image](https://img.philfan.cn/AI__LLM__Sci__assets__04-SFT.assets__webui.webp)

#### 进行训练

- PEFT 0.12.0
- Transformers 4.45.2
- Pytorch 2.4.1+cu121
- Datasets 2.21.0
- Tokenizers 0.20.1

可以中途切断，loss 不需要太低

![image](https://img.philfan.cn/AI__LLM__Sci__assets__04-SFT.assets__loss.webp)

```shell title="训练命令 基本是默认的参数"
llamafactory-cli train \
    --stage sft \
    --do_train True \
    --model_name_or_path /root/LLaMA-Factory/src/output/en2de \
    --preprocessing_num_workers 16 \
    --finetuning_type lora \
    --template qwen \
    --flash_attn auto \
    --dataset_dir /root/LLaMA-Factory/data \
    --dataset 你的数据集 \
    --cutoff_len 1024 \
    --learning_rate 5e-05 \
    --num_train_epochs 6.0 \
    --max_samples 100000 \
    --per_device_train_batch_size 2 \
    --gradient_accumulation_steps 8 \
    --lr_scheduler_type cosine \
    --max_grad_norm 1.0 \
    --logging_steps 5 \
    --save_steps 100 \
    --warmup_steps 0 \
    --optim adamw_torch \
    --packing False \
    --report_to none \
    --output_dir saves/Qwen2.5-7B-Instruct/lora/train_2025-07-14-22-51-16 \
    --bf16 True \
    --plot_loss True \
    --ddp_timeout 180000000 \
    --include_num_input_tokens_seen True \
    --lora_rank 8 \
    --lora_alpha 32 \
    --lora_dropout 0 \
    --loraplus_lr_ratio 16 \
    --lora_target all 
```

#### API 推理

在服务器上执行

```shell title="api.sh"
source activate llama
cd /root/LLaMA-Factory

CUDA_VISIBLE_DEVICES=0 API_PORT=6006 python src/api.py \
    --model_name_or_path /root/LLaMA-Factory/src/output/en2de \
    --template qwen \
```

相当于把这项服务部署到了服务器的端口上，然后通过 openai 的 api 进行调用，就可以实现推理

```python title="api.py"
import openai
import sys

api_key = "EMPTY"
openai.api_base = "http://localhost:6006/v1"


def chat_with_gpt3_5(messages):
    response = openai.ChatCompletion.create(
        model="xxx",
        messages=messages,
        api_key=api_key,
        stream=True  # 启用流式输出
    )

    full_response = ""
    for chunk in response:
        if 'choices' in chunk and len(chunk['choices']) > 0:
            content = chunk['choices'][0].get('delta', {}).get('content', '')
            if content:
                print(content, end='', flush=True)
                full_response += content
    print() 
    return full_response

conversation = [
    {"role": "system", "content": "你是一个聪明的 AI"}
]

while True:

    user_input = input("You: ")

    if user_input.lower() == '退出':
        print("Assistant: 再见！")
        break

    conversation.append({"role": "user", "content": user_input})

    print("Assistant: ", end='', flush=True)
    assistant_message = chat_with_gpt3_5(conversation)

    conversation.append({"role": "assistant", "content": assistant_message})
```

则可以在本地浏览器访问`http://localhost:6006`，进行推理，也可以通过 api 进行调用

下面的代码中我测试了英译德的测试集 1000 个样本，达到了 44.45 的 bleu 分数

[:fontawesome-solid-code:   inference.py](./assets/04-SFT.assets/inference.py){: .md-button .md-button--primary }  

[:fontawesome-solid-code:   bleu.py](./assets/04-SFT.assets/bleu.py){: .md-button .md-button--primary }

```text title="部分翻译结果"
Original English: 2 blond girls are sitting on a ledge in a crowded plaza.
Translation: 2 blonde Mädchen sitzen auf einer Fassade in einem überfüllten Platz.
Reference German: 2 blonde Mädchen sitzen auf einem Absatz auf einem belebten Platz.
BLEU score: 66.23282548391518

Original English: A child is splashing in the water
Translation: Ein Kind macht im Wasser Platsch.
Reference German: Ein Kind planscht im Wasser.
BLEU score: 66.64762996818769

Original English: Three people sit at a picnic table outside of a building painted like a union jack.
Translation: Drei Personen sitzen an einem Picknicktisch vor einem Gebäude, das wie ein Union Jack gemalt ist.
Reference German: Drei Leute sitzen an einem Picknicktisch vor einem Gebäude, das wie der Union Jack bemalt ist.
BLEU score: 85.15116314550686
```

```shell title="翻译结果"
Translation English to German and calculating BLEU scores...
100%|█████████████████████████████████████████████████████████████████████████████████████| 1000/1000 [09:52<00:00,  1.69it/s]
Average BLEU score for DE to EN: 44.44732087434253
```

### 问题解决

1. 模型问题，下载模型
   - 如果下载出现问题，会报错

    ```text
    safetensors_rust.SafetensorError: Error while deserializing header: MetadataIncompleteBuffer
    ```

2. 模版问题：使用`llama3`模版：可以在   `template.py` 中添加自己的对话模板。
3. lora 问题

    ```text
    ValueError: Target modules {'c_attn'} not found in the base model. Please check the target modules and try again.
    ```

    改成`q_proj,v_proj`

    ```text
    --lora_target q_proj,v_proj
    ```
