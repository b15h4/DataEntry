import csv

NumbersLINC = []

with open('numbers.csv', mode='r') as csv_file:
	csv_reader = csv.reader(csv_file)
	for row in csv_reader:
		NumbersLINC.append(row)



for x in list(NumbersLINC):
	input1 = x[0]
	input2 = x[1]
	input3 = x[2]

	print(input1,input2,input3)