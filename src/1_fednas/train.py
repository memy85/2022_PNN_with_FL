import torch
import torch.nn as nn
from mpi4py import MPI

from src.MyModule.models import Model, Server

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0 :
    server = Server(10)
    comm.Recv(data, )
    

else :
    model = Model(10)

if __name__ == "__main__":
    pass