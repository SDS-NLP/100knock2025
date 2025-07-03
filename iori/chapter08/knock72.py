from knock71 import train_data,dev_data
from knock70 import token_to_id, id_to_token, embedding_matrix
import torch

import torch.nn as nn
import torch.nn.functional as F

class LogisticRegressionModel(nn.Module):
    def __init__(self, embedding_dim):
        super(LogisticRegressionModel, self).__init__()
        self.linear = nn.Linear(embedding_dim, 1)  

    def forward(self, x):
        x = torch.mean(x, dim=1)  
        x = self.linear(x)       
        x = torch.sigmoid(x)     
        return x

model = LogisticRegressionModel(embedding_matrix.shape[1])