from mpi4py import MPI
import torch


class Client:
    
    def __init__(self, rank, communicator : MPI.COMM_WORLD):
        self.client_rank = rank
        self.random_number = torch.rand(100)
        self.comm = communicator
        
    def send(self, data):
        self.comm.send(data, dest=0)
        print('sent messages to server')
        
    def receive(self):
        data = None
        req = self.comm.bcast(data, root=0)
        print('received messages from server')
        return req
    
    def train(self):
        req = self.receive()
        print(f'client {self.client_rank} received {req}')
        new_data = self.random_number + req
        self.send(new_data)
        print(f'rank {self.client_rank} sended {new_data}')