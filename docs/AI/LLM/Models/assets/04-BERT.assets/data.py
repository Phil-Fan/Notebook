import numpy as np
import pandas as pd
import torch
from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-cased")
labels = {"business": 0, "entertainment": 1, "sport": 2, "tech": 3, "politics": 4}


def load_data(path, with_label=True):
    """
    加载数据集，返回 DataFrame。
    with_label: 是否包含标签列（train/solution 为 True，test 为 False）
    """
    df = pd.read_csv(path)
    if with_label:
        # 兼容 train/solution 格式
        if "Category" in df.columns:
            df = df.rename(columns={"Category": "category", "Text": "text"})
        else:
            df = df.rename(columns={"category": "category", "text": "text"})
    else:
        # test 集没有标签
        if "Text" in df.columns:
            df = df.rename(columns={"Text": "text"})
        else:
            df = df.rename(columns={"text": "text"})
    return df


## 这里做了特殊处理以兼容 test 和 train 数据集，因为 test 集没有标签，
class Dataset(torch.utils.data.Dataset):
    def __init__(self, df):
        if "category" in df.columns:
            self.labels = [labels[label] for label in df["category"]]
        else:
            self.labels = None
        self.texts = [
            tokenizer(
                text, padding="max_length", max_length=512, truncation=True, return_tensors="pt"
            )
            for text in df["text"]
        ]

    def classes(self):
        return self.labels

    def __len__(self):
        return len(self.texts)

    def get_batch_labels(self, idx):
        # Fetch a batch of labels
        if self.labels is None:
            return None
        return np.array(self.labels[idx])

    def get_batch_texts(self, idx):
        # Fetch a batch of inputs
        return self.texts[idx]

    def __getitem__(self, idx):
        batch_texts = self.get_batch_texts(idx)
        if self.labels is None:
            return batch_texts  # 只返回文本
        batch_y = self.get_batch_labels(idx)
        return batch_texts, batch_y
