import sys
lnum =0
with open('train.arff') as f:
	for line in f:
		lnum += 1
		line = line.split(',')
		print(line)
		if len(line) != 101:
			print(lnum)
