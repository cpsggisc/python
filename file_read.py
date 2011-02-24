# file_read.py
# read from text file IN.TXT

infile = open("IN.TXT", "r")

num = int(infile.readline())

result = num * num

print(result)

