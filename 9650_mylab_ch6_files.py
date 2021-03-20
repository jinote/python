#chap6 51360
'''A file named numbers.txt contains an unknown number of lines, each consisting of a single positive integer. Write some code that reads through the file, ignoring those value that are not bigger than the maximum value read up to that point. The numbers that are NOT ignored are added, and their sum stored in a variable called runsum.
For example, if the sequence of integers in the file were "9 7 5 18 13 2 22 16" the code would ignore: 7, 5, 13, 2 and 16; it would add 9, 18, and 22, storing their sum, 49, into runsum.
'''

numfile = open("numbers.txt", "r")
runsum = 0
maxvalue = 0
num = numfile.readline()

while num != "":
  num = int(num)
  if int(num) > maxvalue:
    maxvalue = num
    runsum += int(num)
  num = numfile.readline()
  
numfile.close()
