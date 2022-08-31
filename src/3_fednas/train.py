import torch
import torch.nn as nn
from mpi4py import MPI
import random 
import numpy as np

# from src.MyModule.models import Model, Server

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

class Model:
    
    def __init__(self, client):
        self.client = client
        self.number = self.make_random_numbers()
     
    def make_random_numbers(self):
        return np.random.rand(1, seed=self.client)
    
    def train(self, server_weights):
        print('training ...')
        new_weights = server_weights + self.number
        print('train finished')
        return new_weights

class Server:
    
    def __init__(self):
        self.cur_round = 1
        self.total_round = 10
    
    def initialize(self):
        return np.random.rand(1, seed=0)
    
    def aggregate(self, *args):
        num_of_clients = len(args)
        averaged = sum(args) / num_of_clients
        return averaged
    
    def finalize(self):
        print('ended')


if rank == 0 :
    server = Server()
    w = server.initialize()
    comm.Bcast(w, root=0)
    
    comm.Irecv()
    
else :
    model = Model(rank)

if __name__ == "__main__":
    pass