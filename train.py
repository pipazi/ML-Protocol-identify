import csv
import re

test_lib = []
train_lib = []

header =  ['0', '1', '2','3', '4', '5','6', '7', '8', '9',
'10', '11', '12', '13', '14', '15','16', '17', '18', '19',
'20', '21', '22', '23', '24', '25','26', '27', '28', '29',
'30', '31', '32', '33', '34', '35','36', '37', '38', '39',
'40', '41', '42', '43', '44', '45','46', '47', '48', '49',
'50', '51', '52', '53', '54', '55','56', '57', '58', '59',
'60', '61', '62', '63', '64', '65','66', '67', '68', '69',
'70', '71', '72', '73', '74', '75','76', '77', '78', '79',
'80', '81', '82', '83', '84', '85','86', '87', '88', '89',
'90', '91', '92', '93', '94', '95','96', '97', '98', '99', 'class']
test_lib.append(header)
train_lib.append(header)


with open('any.vec.txt', 'r') as anyFile:
	for line in anyFile:
		line = re.split(' |\n',line)
		line = filter(None,line)
		line.append('any')
		train_lib.append(line)
with open('any_test.vec.txt', 'r') as anytestFile:
        for line in anytestFile:
                line = re.split(' |\n',line)
                line = filter(None,line)
                line.append('any')
                test_lib.append(line)
with open('other_big.vec.txt', 'r') as otherFile:
        for line in otherFile:
		line = re.split(' |\n',line)
		line = filter(None,line)
		line.append('other')
                train_lib.append(line)
with open('other2.vec.txt','r') as other2File:
	for line in other2File:
		line = re.split(' |\n',line)
		line = filter(None,line)
		line.append('other')
		test_lib.append(line)
with open('gen.vec.txt', 'r') as genFile:
	for line in genFile:
		line = re.split(' |\n',line)
		line = filter(None,line)
		line.append('gen')
		train_lib.append(line)
with open('gen_test.vec.txt', 'r') as gentestFile:
        for line in gentestFile:
                line = re.split(' |\n',line)
                line = filter(None,line)
                line.append('gen')
                test_lib.append(line)
with open('train.csv', 'w') as trainFile:
	writer = csv.writer(trainFile)
	writer.writerows(train_lib)

with open('test.csv', 'w') as testFile:
	writer = csv.writer(testFile)
	writer.writerows(test_lib)
anyFile.close()
otherFile.close()
genFile.close()
gentestFile.close()
anytestFile.close()
trainFile.close()
testFile.close()
