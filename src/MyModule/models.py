import torch
import torch.nn as nn
import torch.nn.functional as F



class Model(nn.Module):
    '''
    simple mlp model
    '''
    def __init__(self, input_shape, output_shape, hidden_shape, model_number):
        self.model_number = model_number
        self.layer1 = nn.Linear(input_shape, hidden_shape)
        self.layer2 = nn.Linear(hidden_shape, hidden_shape)
        self.layer3 = nn.Linear(hidden_shape, output_shape)
        
    
    def forward(self, x):
        layers = nn.Sequential(
            self.layer1,
            nn.ReLU,
            self.layer2,
            nn.ReLU,
            self.layer3,
            nn.Softmax
        )
        
        y = layers(x)
        return y
    


class Server:
    
    def __init__(self, total_round):
        self.round = 0
        self.total_round = total_round
    
    def aggregate_weights(self, weights):
        