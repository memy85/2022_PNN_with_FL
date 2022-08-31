from mpi4py import MPI
import torch


class Server:
    
    def __init__(self, total_rounds,
                       epoch_per_round, 
                       randomseed, 
                       communicator : MPI.COMM_WORLD, size):
        self.comm = communicator
        self.total_rounds = total_rounds
        self.epoch_per_round = epoch_per_round
        self.randomseed = randomseed
        self.size = size
        self.param = torch.rand(100)
    
    
    def send(self, data):
        '''
        broadcast to all clients
        tag = 0 : start training
        tag = 1 : end total round
        '''
        # for procid in range(1, self.size):
        #     self.comm.send(data, dest=procid)
        data = self.comm.bcast(data, root=0)
    
    def receive(self):
        '''
        receive all data sent from clients
        '''
        data = list()
        for procid in range(1,self.size):
            data.append(self.comm.recv(source=procid))
        return data
    
    def aggregate(self, data : list):
        new_data = sum(data) / len(data)
        return new_data
    
    def round(self, start_conf, round_num):
        print('starting round ... ')
        self.send(start_conf)
        print('sent messages to clients')
        recv = self.receive()
        print('received messages from clients')
        new = self.aggregate(recv)
        print(f'{round_num} round finished')
        return new
    
    def train(self, round_num):
        self.param = self.round(self.param, round_num)