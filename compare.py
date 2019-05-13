#!/usr/bin/env python
import sys
import linecache
import re
from collections import defaultdict
import random

dotfile = sys.argv[1]
timeout = int(sys.argv[2])
name_string = dotfile.split('.')[0]
output = open(name_string+'.dot.out','w')
tree = defaultdict(list)  # keynode: [child1, child2]
code_lib = defaultdict(list)
nodes = set()
edges = set()
EE = []
path_lib = []


def buildTree():
	def find_edge():
		with open(dotfile) as f:
			for line in f:
				if '->' in line:
					l = line.split('[')[0]
					l = l.strip()
					l = l.split(' -> ')
					if l[0].isdigit():
						edges.add(tuple(l))
						nodes.add(l[0])
						nodes.add(l[1])
	def entry_exit():
		with open(dotfile) as f:
			lnum = 0
			for line in f:
				lnum+=1
				if 'ENTRY' in line:
					l = linecache.getline(dotfile, lnum-2).strip()
					l = l.split('[')
					EE.append(l[0].strip())
	
	
	
		with open(dotfile) as f:
			lnum = 0
			for line in f:
				lnum+=1
				if 'EXIT' in line:
					l = linecache.getline(dotfile, lnum-2).strip()
					l = l.split('[')
					EE.append(l[0].strip())
	
	

	find_edge()
	entry_exit()
	for a,b in edges:
			if b not in tree[a]:
				tree[a].append(b)



def codelib():
        lnum = 0
        with open(dotfile) as f:
                for line in f:
                        lnum+=1
                        if 'code:' in line:
                                _id = linecache.getline(dotfile,lnum-2).strip()
                                _id = int(_id.split(' ')[0])
                                code = line.strip()
                                code = code.split('code:')[1].split('\\n')[0]
                                code_lib[_id].append(code)

def randwalk(timeout):
	ans = set()
	def singlePath():
		def helper(pre_path,cur_node):
			if cur_node == EE[1]:
				ans.add(pre_path[2:]+'->'+cur_node)
				#print ans
			else:
				numKids = len(tree[cur_node])
				nextNode = tree[cur_node][random.randint(0,numKids-1)]
				if nextNode in pre_path or nextNode==cur_node:
					helper('',EE[0])
				else:
					helper(pre_path+'->'+cur_node,nextNode)

		helper('',EE[0])

	last_len = 0
	repeat = 0
	while len(ans) < 300000 and repeat<timeout:
		singlePath()
		if len(ans) == last_len:
			repeat += 1
		else:
			last_len = len(ans)

	for i,item in enumerate(ans):
		path_lib.append(item)


def printpath():
	count = 0
	for path in path_lib:
		path = path.split('->')
		for node in path:
			output.write(str(code_lib[int(node)][0])+'\n')
		output.write('\n')
		count += 1
	print('Total path is:',count)

def main():
	buildTree()
	codelib()
	randwalk(timeout)
	printpath()

if __name__ == "__main__":
	main()
