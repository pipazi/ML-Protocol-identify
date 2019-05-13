#!/usr/bin/env python
import sys
import glob
import os
import linecache
import re
from collections import defaultdict
import random
import subprocess
import numpy

dotfile = sys.argv[1]
func_list = sys.argv[2]
timeout = int(sys.argv[3])
pointer = sys.argv[4]

# file_name = ''
# name_string = file_name.split('.')
# output = open(name_string[0]+'.out','w')

tree = defaultdict(list)
code_lib = defaultdict(list)
nodes = set()
edges = set()
EE = []
mergepath = []
slicing_lib = []
path_lib = []
funcs_lib=[]
file_lib = []
before = []
path_num = 0
count = 0

def buildTree(file_name):
	del EE[:]
	def find_edge():
		with open(file_name) as f:
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
		with open(file_name) as f:
			lnum = 0
			for line in f:
				lnum+=1
				if 'ENTRY' in line:
					l = linecache.getline(file_name, lnum-2).strip()
					l = l.split('[')
					EE.append(l[0].strip())
	
	
	
		with open(file_name) as f:
			lnum = 0
			for line in f:
				lnum+=1
				if 'EXIT' in line:
					l = linecache.getline(file_name, lnum-2).strip()
					l = l.split('[')
					EE.append(l[0].strip())
	
	

	find_edge()
	entry_exit()
	for a,b in edges:
			if b not in tree[a]:
				tree[a].append(b)

def randwalk(timeout):
	global count
	count = 0
	slicing_count = 0
	ans = set()
	del path_lib[:]
	def singlePath():
		def helper(pre_path,cur_node):
			if cur_node == EE[1]:
				ans.add(pre_path[2:]+'->'+cur_node)
				#print ans
			else:
				numKids = len(tree[cur_node])
				nextNode = tree[cur_node][random.randint(0,numKids-1)]
				if nextNode in pre_path or nextNode == cur_node:
					helper('',EE[0])
				else:
					helper(pre_path+'->'+cur_node,nextNode)

		helper('',EE[0])

	last_len = 0
	repeat = 0
	while len(ans) < 300000 and repeat < timeout:
		singlePath()
		if len(ans) == last_len:
			repeat += 1
		else:
			last_len = len(ans)

	for item in ans:
		path = item.split('->')
		path = filter(None,path)
		for node in path:
			if int(node) in slicing_lib:
				slicing_count += 1
		if slicing_count > 1:
			path_lib.append(item)
			count += 1

def slicing_related(file_name):
	with open(file_name) as f:
		for line in f:
			if 'blue4' in line:
				_id = line.strip()
				_id = int(_id.split(' ')[0])
				slicing_lib.append(_id)



def codelib(file_name):
	lnum = 0
	with open(file_name) as f:
		for line in f:
			lnum+=1
			if 'code:' in line:
				_id = linecache.getline(file_name,lnum-2).strip()
				_id = int(_id.split(' ')[0])
				code = line.strip()
				code = code.split('code:')[1].split('\\n')[0]
				code_lib[_id].append(code)


def printallpath():
	for path in path_lib:
		output.write(path+'\n')


def func_lib():
        with open(func_list) as f:
                for line in f:
                        function = line.split('\t')[0]
                        if function not in funcs_lib:
                                funcs_lib.append(function)
	funcs_lib.remove('main')


def set_output(file_name):
	global output
	name_string = file_name.split('.')
	output = open(name_string[0]+'.out','w')


code_lib_sub = defaultdict(list)
sub_path = []
word = ''

def combine():
	global output
        global before
        global mergepath
	global word
	global count
	count = 0
	one_mul_path = [[]]
	name_string = dotfile.split('.')
	path_file = name_string[0]+'.out'
	output = open(name_string[0]+'.dot.out','w')


# analysis the input function
	with open(path_file) as f:
		for line in f:
			line = line.split('->')
			for node in line:
				string = code_lib[int(node)][0]
				for one in one_mul_path:
					one.append(str(string))
				string = re.split('#|;|,|-|\\|->|\n|\t|=|:|\)|\(|\{|\}|!|\[|\]|&|<|>|\*|\+|~| |\.|\?|/|&|$|^|\"|\||',string)
				string = filter(None,string)
				for token in string:
					if token in funcs_lib:
						pre_word = str(token)
						for token in string: 
							if token == pointer:
								for one in one_mul_path:
									one.pop()
								word = str(pre_word)
								multipath(one_mul_path)


# output the result
			for one in one_mul_path:
				for node in one:
					output.write(node+'\n')
				output.write('\n')
				count+=1
				if count == 1500:
					break
			one_mul_path = [[]]



def multipath(one_mul_path):
	subfunc_name = word + '.dot'
	print(subfunc_name)

        lnum = 0
        num = 0
	total_path = 0
	cur_path_len = 0
	temp_len = 0
	sub_path = []
	temp_list = []


# load reference function code and id
        with open(subfunc_name) as f:
                for line in f:
                        lnum+=1
                        if 'code:' in line:
                                _id = linecache.getline(subfunc_name,lnum-2).strip()
                                _id = int(_id.split(' ')[0])
                                code = line.strip()
                                code = code.split('code:')[1].split('\\n')[0]
                                code_lib_sub[_id].append(code)


# load refernce function path
        subfunc_name = subfunc_name.split('.')[0]+'.out'
        with open(subfunc_name) as f:
                for line in f:
                        line = line.rstrip("\n")
                        line = line.split('->')
			sub_path.append(line)
	total_path = int(len(sub_path))


# initalize for insert
	for path in one_mul_path:
		temp_list.append(list(path))
		cur_path_len += 1

	temp_len = int(cur_path_len)

	for x in range(1, total_path):
		for path in temp_list:
			one_mul_path.append(list(path))


# insert
	while(temp_len):
		i = int(temp_len - 1)
		for path in sub_path:
			for node in path:
				if code_lib_sub[int(node)][0] == 'ENTRY' or code_lib_sub[int(node)][0] == 'EXIT':
					pass
				else:
					one_mul_path[i].append(str(code_lib_sub[int(node)][0]))
			i+=cur_path_len
		temp_len-=1



def ture_path():
	print('...')
	codelib(dotfile)
	print('code lib generated')
	slicing_related(dotfile)
	print('slicing finished')
	func_lib()
	print('function libs found')
	combine()
	print('the total path is %s' % count)

def init(file_name):
	set_output(file_name)
	print(output)
	buildTree(file_name)
	print('Builded tree')
	slicing_related(file_name)
	print('slicing finished')
	randwalk(timeout)
	print('extracted path: %s' %count)
	printallpath()
	print('wrote all path')
	output.close()

if __name__ == "__main__":
	file_lib = glob.glob("./*.dot")
	for files in file_lib:
		input_file = str(files[2:])
		init(input_file)
	raw_input()
	ture_path()
