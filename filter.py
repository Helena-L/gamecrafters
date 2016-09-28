from mpi4py import MPI

data_set = [1, 2, 3, 4, 5, 6]

def filter_fun(data):
	if data % 2 == 0 :
		return True
	else :
		return False

def my_filter(data_set, filter_fun) :
	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()

	#Scatter
	data = comm.scatter(data_set, root=0)
	size = comm.Get_size()

	if filter_fun(data) == True :
		comm.send(True, dest=0, tag=1)
	else :
		comm.send(False, dest=0, tag=0)

	comm.Barrier()

    # rank == 0
	if rank == 0 :
		count = 0
		data_after_filter = []
		while count < size :
			mark = comm.recv(source = count)
			if mark == True :
				data_after_filter.append(data_set[count])
			count += 1
		print(data_after_filter)

# start data filter
my_filter(data_set, filter_fun)