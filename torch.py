import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

class InteractionDataset(Dataset):
    def __init__(self, user_ids, item_ids, labels):
        self.user_ids = user_ids
        self.item_ids = item_ids
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.user_ids[idx], self.item_ids[idx], self.labels[idx]

user_ids = [0, 1, 2, 0, 1]
item_ids = [3, 4, 5, 5, 3]
labels = [1, 0, 1, 0, 1]

dataset = InteractionDataset(user_ids, item_ids, labels)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)
