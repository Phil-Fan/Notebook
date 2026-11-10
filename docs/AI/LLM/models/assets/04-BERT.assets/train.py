import os

import numpy as np
import torch
import torch.nn as nn
from data import Dataset, load_data
from torch.optim import Adam
from tqdm import tqdm
from transformers import BertModel


class BertClassifier(nn.Module):
    """BERT-based classifier model.这里直接使用 bert-base-cased，加上一个线性层"""

    def __init__(self, dropout: float = 0.5, num_classes: int = 5):
        super(BertClassifier, self).__init__()

        self.bert = BertModel.from_pretrained("bert-base-cased")
        self.dropout = nn.Dropout(dropout)
        self.linear = nn.Linear(self.bert.config.hidden_size, num_classes)

    def forward(self, input_id: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
        outputs = self.bert(input_ids=input_id, attention_mask=mask)
        pooled_output = outputs.pooler_output
        dropout_output = self.dropout(pooled_output)
        return self.linear(dropout_output)


def train(
    model: nn.Module,
    train_data: Dataset,
    val_data: Dataset,
    learning_rate: float,
    epochs: int,
    batch_size: int = 2,
) -> None:
    # Initialize datasets
    train_dataset, val_dataset = Dataset(train_data), Dataset(val_data)

    # Create data loaders
    train_dataloader = torch.utils.data.DataLoader(
        train_dataset, batch_size=batch_size, shuffle=True
    )
    val_dataloader = torch.utils.data.DataLoader(val_dataset, batch_size=batch_size)

    # Set device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    # Initialize loss and optimizer
    criterion = nn.CrossEntropyLoss().to(device)
    optimizer = Adam(model.parameters(), lr=learning_rate)

    # Training loop
    for epoch_num in range(epochs):
        total_acc_train = 0
        total_loss_train = 0

        model.train()
        # Training phase
        for train_input, train_label in tqdm(train_dataloader):
            # 这里 train_input 是 BertTokenizer 的输出，是一个字典，包含 input_ids, attention_mask, token_type_ids
            train_label = train_label.to(device)
            mask = train_input["attention_mask"].to(device)
            input_id = train_input["input_ids"].squeeze(1).to(device)

            optimizer.zero_grad()
            output = model(input_id, mask)

            batch_loss = criterion(output, train_label)
            total_loss_train += batch_loss.item()

            acc = (output.argmax(dim=1) == train_label).sum().item()
            total_acc_train += acc

            batch_loss.backward()
            optimizer.step()

        # Validation phase
        model.eval()
        total_acc_val = 0
        total_loss_val = 0

        with torch.no_grad():
            for val_input, val_label in val_dataloader:
                val_label = val_label.to(device)
                mask = val_input["attention_mask"].to(device)
                input_id = val_input["input_ids"].squeeze(1).to(device)

                output = model(input_id, mask)
                batch_loss = criterion(output, val_label)
                total_loss_val += batch_loss.item()

                acc = (output.argmax(dim=1) == val_label).sum().item()
                total_acc_val += acc

        print(
            f"""Epochs: {epoch_num + 1} 
            | Train Loss: {total_loss_train / len(train_data): .3f} 
            | Train Accuracy: {total_acc_train / len(train_data): .3f} 
            | Val Loss: {total_loss_val / len(val_data): .3f} 
            | Val Accuracy: {total_acc_val / len(val_data): .3f}"""
        )


def evaluate(model: nn.Module, test_data: Dataset, batch_size: int = 2) -> float:
    test_dataset = Dataset(test_data)
    test_dataloader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    model.eval()
    total_acc_test = 0
    with torch.no_grad():
        for test_input, test_label in test_dataloader:
            test_label = test_label.to(device)
            mask = test_input["attention_mask"].to(device)
            input_id = test_input["input_ids"].squeeze(1).to(device)
            output = model(input_id, mask)
            acc = (output.argmax(dim=1) == test_label).sum().item()
            total_acc_test += acc

    test_accuracy = total_acc_test / len(test_data)
    print(f"Test Accuracy: {test_accuracy:.3f}")
    return test_accuracy


def main():
    np.random.seed(112)
    torch.manual_seed(112)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(112)

    # Load and split data
    train_path = os.path.join("data", "BBC News Train.csv")
    df = load_data(train_path, with_label=True)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    # Split into train/val/test (80%/10%/10%)
    n = len(df)
    n_train = int(0.8 * n)
    n_val = int(0.9 * n)
    df_train = df.iloc[:n_train]
    df_val = df.iloc[n_train:n_val]
    df_test = df.iloc[n_val:]

    print(f"Dataset sizes - Train: {len(df_train)}, Val: {len(df_val)}, Test: {len(df_test)}")

    # Train model
    model = BertClassifier()
    train(model=model, train_data=df_train, val_data=df_val, learning_rate=1e-6, epochs=5)

    evaluate(model, df_test)

    # Save model
    save_path = os.path.join("models", "bert_classifier.pth")
    os.makedirs("models", exist_ok=True)
    torch.save(model.state_dict(), save_path)
    print(f"Model saved to {save_path}")


if __name__ == "__main__":
    main()
