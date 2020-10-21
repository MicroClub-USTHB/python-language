
import os, sys

def f(directory):
	for i in os.listdir(directory):
		i=directory+"/"+i
		if os.path.isdir(i):
			f(i)
		print(i)
f(sys.argv[1])

