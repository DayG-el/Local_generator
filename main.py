import subprocess
import os
import csv
from hytra import HyperGraph as hypergraph
h = hypergraph()
def executeCpp():

	# create a pipe to a child process
	data, temp = os.pipe()

	# write to STDIN as a byte object(convert string
	# to bytes with encoding utf8)
	os.write(temp, bytes("5 10\n", "utf-8"));
	os.close(temp)

	# store output of the program as a byte string in s
	s = subprocess.check_output("g++ -O3 -o DL DL.cpp", stdin = data, shell = True)
	s = subprocess.check_output("DL in2.dat out.dat", stdin = data, shell = True)


	# decode s to a normal string
	print(s.decode("utf-8"))


def read_data(file_loc='out.dat'):
	trans = dict()
	with open(file_loc) as f:
		filedata = csv.reader(f, delimiter=',')
		count = 0
		for line in filedata:
			count += 1
			trans[count] = set(line)
			h.added(trans[count])
			print("Hyperedge number ", count, "est :", trans[count])
	return trans


# Driver function
if __name__=="__main__":

	executeCpp()


