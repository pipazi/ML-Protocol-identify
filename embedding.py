import sys
import re
import random
import linecache
import os
import glob


def embedding(item):
	output = open(item+'.txt','w')
	with open(item) as f:
		for line in f:
			if line ==  '\n':
				output.write('\n')
			line = line.strip()
			line = re.split(',|;|\n|\)|\(|\{|\}|\[|\]| |',line)
			line = filter(None,line)
			for token in line:
				output.write(token+' ')
	print(item+' file finished')

def other2(item):
	print(item)
	count = 0
	loop = 200
	output = open('other2_train.txt','a')
	with open(item,'r') as f:
		count = 0
		for line in f:
			count += 1
		if count < 200:
			for line in f:
				print(output)
				output.write(line)
		if count > 200:
			visited = set()
			while(loop):
				lnum = random.randint(1,count)
				if lnum in visited:
					pass
				else:
					visited.add(lnum)
					line = linecache.getline(item, lnum)
					print(output)
					output.write(line)
					loop-=1
		
def valid():
	output = open('other2_valid.txt','w')
	loop = 0
        lnum = 0
	count = 0
	with open('other2_train.txt') as f:
		for line in f:	
			count +=1
		loop = count / 5
		print(count,loop)
                while(loop):
                        lnum = random.randint(1,count)
                        line = linecache.getline('other2_train.txt', lnum)
                        output.write(line)
                        loop -= 1
			

if __name__ == "__main__":
	directory = glob.glob("*")
	directory.remove('embedding.py')
	for item in directory:
		embedding(item)
	directory = glob.glob("*.txt")
	for item in directory:
		other2(item)
	valid()
	os.system('mv other2_train.txt ../')
	os.system('mv other2_valid.txt ../')
	os.system('rm *.txt')
