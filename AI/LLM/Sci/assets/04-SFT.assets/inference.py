import openai
import tqdm
from bleu import bleu, get_bleu

api_key = "EMPTY"
openai.api_base = "http://localhost:6006/v1"


def chat_with_qwen(messages):
    """使用服务器部署的训练好的模型进行预测"""
    response = openai.ChatCompletion.create(
        model="xxx",
        messages=messages,
        api_key=api_key,
        stream=True,  # 启用流式输出
    )

    full_response = ""
    for chunk in response:
        if "choices" in chunk and len(chunk["choices"]) > 0:
            content = chunk["choices"][0].get("delta", {}).get("content", "")
            if content:
                full_response += content
    return full_response


# Load test data
test_data_path = "./test/"
test_data_en = []
with open(test_data_path + "test.en", "r", encoding="utf-8") as f:
    for line in f:
        test_data_en.append(line.strip())

test_data_de = []
with open(test_data_path + "test.de", "r", encoding="utf-8") as f:
    for line in f:
        test_data_de.append(line.strip())

print("Translation English to German and calculating BLEU scores...")
bleu_scores_ende = []

with open("output.log", "w", encoding="utf-8") as log_file:
    for i, (sentence_en, sentence_de) in tqdm.tqdm(
        enumerate(zip(test_data_en, test_data_de)), total=len(test_data_en)
    ):  # zip + enumerate 可以实现同步遍历
        conversation = [
            {"role": "system", "content": "Translate the following English text to German."},
            {"role": "user", "content": sentence_en},
        ]
        generated_text = chat_with_qwen(conversation)

        bleu = get_bleu(hypotheses=generated_text.split(), reference=sentence_de.split())
        bleu_scores_ende.append(bleu)

        log_file.write(f"Original English: {sentence_en}\n")
        log_file.write(f"Translation: {generated_text}\n")
        log_file.write(f"Reference German: {sentence_de}\n")
        log_file.write(f"BLEU score: {bleu}\n\n")

# Calculate average BLEU score for DE to EN
avg_bleu_ende = sum(bleu_scores_ende) / len(bleu_scores_ende)
print(f"Average BLEU score for DE to EN: {avg_bleu_ende}")
