from mpi4py import MPI
import torch

from server import Server
from client import Client

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
total_round  = 10


def main():
    
    if rank == 0 : 
        server = Server(total_round, 10, 1, comm, size)
    else :
        client = Client(rank, comm)
        
    for r in range(total_round) :     
        # server
        if rank == 0 :
            print(f'the total clients are {size - 1}')
            server.train(r)
        # client
        else :
            print(f'this is the rank : {rank}')
            client.train()

    print('ended process')

if __name__ == '__main__':
    main()
