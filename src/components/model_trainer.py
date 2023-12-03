import os
from ...logger import logging
import pandas as pd
from src.config.configuration import ModelTrainerConfig,ModelTrainerParmas
import torch
from torch.utils.data import Dataset,DataLoader
import torch.nn as nn
import torch.optim as optim
from src.utils.common import one_hot_ce_loss

class Net(nn.Module):
    def __init__(self,vocab_size):
        super(Net,self).__init__()
        self.embed = nn.Embedding(vocab_size,100)
        # Define GRU layer
        self.gru = nn.GRU(
            input_size=100,
            hidden_size=64,
            num_layers=2,
            batch_first=True,
            dropout = 0.3,
        )
        self.batchnorm = nn.BatchNorm1d(64)
        self.fc = nn.Linear(64, 128)
        self.dropout = nn.Dropout(0.5)
        self.fc2 = nn.Linear(128,3)

    def forward(self, x):
        out = self.embed(x)
        h0 = torch.zeros(2, x.size(0), 64)
        out, _ = self.gru(out, h0)
        out = self.fc(self.batchnorm(out[:, -1, :]))
        out = self.dropout(out)
        out = self.fc2(out)
        return out
class tokenizedDataset(Dataset):
    def __init__(self,X,y):
        super().__init__()
        self.X = torch.tensor(X)
        self.y = torch.tensor(y)
    def __len__(self):
        return self.X.shape[0]
    def __getitem__(self,idx):
        X = self.X[idx]
        y = self.y[idx]
        return X,y


class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig,params:ModelTrainerParmas):
        self.config = config
        self.params =params
    def run(self):
        try:
            train_df = pd.read_csv(self.config.train_data_path,header = False,index = False)
            logging(f"Loaded training data Successfully with shape {train_df.shape}")
            numberOfRecords = int(train_df.shape[0]//16*16)
            tokenizedTrainData = tokenizedDataset(train_df[:-3][:numberOfRecords],train_df[:-3]y_train[:numberOfRecords])
            dataloader_train = DataLoader(tokenizedTrainData,
                                        batch_size = 16,
                                        shuffle = True)
            model = Net(self.params.vocab_size)
            criterion = nn.CrossEntropyLoss()
            optimizer = optim.Adam(
            model.parameters(), lr=0.0001
            )
            model.train()
            for epoch in range(10):
                for seqs, labels in dataloader_train:
                    outputs = model(seqs)
                    # Compute loss
                    loss = one_hot_ce_loss(outputs,labels.to(torch.float32))
                    optimizer.zero_grad()
                    loss.backward()
                    optimizer.step()
                print(f"Epoch {epoch+1}, Loss: {loss.item()}")

            with open(self.config.model_path,"wb") as f:
                torch.save(model.state_dict(),f)
            logging(f"model saved to path {self.config.model_path}")
        except Exception as e:
            raise e