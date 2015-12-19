# Removing Duplicates from Music library(File)
# Attempt No. 1
# all-alphabet string matching test
# Compiled in Python 3.x


# Usage : program creates a new tempXXXXXX directory and copies 
#         all the distinct music files to that folder
  
from os import listdir
from os.path import isfile, join
import re
import subprocess
import time
import os.path

# mypath is path of music library
def compress_lib(mypath):
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	onlyfiles.sort()
	print(len(onlyfiles))
	list2 = []
	for s in onlyfiles:
		# extracting text from file names
		list2.append("".join(re.findall("[a-zA-z]+",s.replace("_","").lower())))
	i = 0
	my_hash = {}
	i = 0 
	for i in range(len(onlyfiles)):
		my_hash[list2[i]] = onlyfiles[i]
	print(len(my_hash))
	# create a new folder with timestamp 
	new_file_path = os.path.join(mypath,"temp"+time.strftime("%H%M%S"))
	str = "mkdir "+new_file_path
	print(new_file_path)
	print(str)
	subprocess.Popen(str,shell = True)
	for (k,v) in my_hash.items():
		v = v.replace(' ','\ ')
		v = v.replace('[','\[')
		v = v.replace(']','\]')
		v = v.replace('(','\(')
		v = v.replace(')','\)')
		v = v.replace("'","\\'")
		v = v.replace("$","\$")
		v = v.replace("&","\&")
		str2 = "cp "+os.path.join(mypath,v)+" "+new_file_path+"/"
		print(str2)
		subprocess.Popen(str2,shell=True)

if __name__=="__main__":
	mypath = str(input("Enter the path : "))
	compress_lib(mypath)