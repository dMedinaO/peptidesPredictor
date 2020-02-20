import sys

fileData = open(sys.argv[1], 'r')

line = fileData.readline()
header = line

line = fileData.readline()

while line:
    data = line.replace("\n", "").split(",")
    print data
    line = fileData.readline()
