
from webbrowser import get
from mpi4py import MPI
comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
p = comm.Get_size()

def get_data(my_rank, p, comm):
    
    a = None
    b = None
    n = None
    if my_rank == 0 :
        
        print("Rank", my_rank, ": Enter a, b and n\n")
        a = float(input("enter a \n"))
        b = float(input("enter b \n"))
        n = int(input("enter n \n"))
        print("ready for broadcast \n")
        
    a = comm.bcast(a)
    b = comm.bcast(b)
    n = comm.bcast(n)

    return a, b, n


a, b, n  = get_data(my_rank, p, comm)

dest = 0
total = 

if __name__ == "__main__":
    get_data()