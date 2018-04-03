import os
import glob
import shutil
import random

def dircount(dir_name):
	if not os.path.exists('./data/'):
		os.makedirs('./data/')
	directories = next(os.walk(dir_name))[1]
	for d in directories:
	    if d != "data":
	    	files = next(os.walk(dir_name + "\\" + d))[2]
	    	os.chdir(dir_name + "\\" + d)
	    	selected = random.sample(files, 4)
	    	for file in selected:
	    		shutil.copy(file, dir_name + "\\data")
	    	os.chdir(dir_name)

def filecount(dir_name):
	return len(next(os.walk(dir_name))[2])


dircount(os.getcwd())