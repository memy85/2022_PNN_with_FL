import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(1,1)
    
    def forward(self, x):
        out = F.relu(self.fc1(x))
        


class PNet(nn.Module):
    def __init__(self):
        super(PNet, self).__init__()
        self.fc1 = nn.L
        