# 9650_mylab_ch6_file input and output

# practice
line = "80\n"
line.rstrip()
#'80'

int(line.rstrip())
# 80

# 51360
'''A file named numbers.txt contains an unknown number of lines, each consisting of a single positive integer. Write some code that reads through the file, ignoring those value that are not bigger than the maximum value read up to that point. 
The numbers that are NOT ignored are added, and their sum stored in a variable called runsum.
For example, if the sequence of integers in the file were "9 7 5 18 13 2 22 16" the code would ignore: 7, 5, 13, 2 and 16; it would add 9, 18, and 22, storing their sum, 49, into runsum.'''

# solution1 using FOR
numfile = open("numbers.txt", "r")
runsum = 0
maxvalue = 0

for num in numfile:
  if int(num) > maxvalue: # necessary to write > int
    maxvalue = int(num) # necessary to write > int
    runsum += int(num) # necessary to write > int
    
print(runsum)
numfile.close()

# soulution using WHILE
numfile = open("numbers.txt", "r");
runsum = 0
maxvalue = 0
num = numfile.readline()

while num != "": # no space
  if int(num) > maxvalue:
    maxvalue = int(num)
    runsum += int(num)
   num = numfile.readline() # required

print(runsum)
numfile.close()
             
               
               
#71408
'''Assume that a file containing a series of integers is named numbers.txt. Write
a program that calculates the average of all the numbers stored in the file.'''

#orginal answer
infile = open('numbers.txt', 'r')
total = 0
counter = 0 

for line in infile:
  line = int(line) # required
  total = total + line
  counter = counter + 1


outfile.close()    
print(total/counter)


# In for loop, try and except
try:
  infile = open("number.txt", "r")
except IOError:
  print("Trouble opening file. try again")
  
total = 0
counter = 0

for line in infile:
  try:
    line = int(line)
  except ValueError:
    print("File must have only numbers. Try again.")
  total = total + line
  counter = counter + 1
  
infile.close()
print(total/counter)


# try includes for loop
infile = open("number.txt", "r")

total = 0
counter = 0
try: 
  for line in infile:
    line = int(line)
    total = total + line
    counter = counter + 1
except ValueError:
  print("file must have only numbers. Try again.")

infile.close()
print(total/counter)

# the whole process in the try clause
try: 
  infile = open("numbers.txt", "r")
  total = 0
  counter = 0
  
  for line in infile:
    line = int(line)
    total = total + line
    counter = counter + 1
  
  infile.close()
  print(total/counter)
  
 except ValueError:
  print("File must have only numbers. Try again")
 
 except IOError:
    print("Trouble opening file. Try again.")
   
 except: 
    print("something else wen wrong.")

    
    
#71434
'''The Springfork Amateur Golf Club has a tournament every weekend. The club
president has asked you to write a program that will read each player's name
and score as keyboard input, and then save these as records in a file named
golf.txt.

First, have the program ask the user how many players they want to add to their
record. Then, ask the user for each name and score individually.

golf.txt should be structured so that there is a line with the player's name,
folowed by their score on the next line.

Enter·number·of·players:4↵
Enter·name·of·player·number·1:Jimmy↵
Enter·score·of·player·number·1:30↵

Emily
30
Mike
20
Jonathan
23'''

#soultion
file = open('golf.txt', 'w')
players_num = int(input('Enter number of players:'))
for i in range(1, players_num+1):
  name = input('Enter name of player number {}:'.format(str(i)))
  score = input('Enter score of player number {}:'.format(str(i)))
  file.write(name)
  file.write('\n')
  file.write(score)
  file.write('\n')
  
file.close()

#practice
outfile = open("golf.txt.", "w")
num = int(input("Enter number of players:"))

for i in range(1,num+1):
  name = input("Enter name of player number " + str(i) + ":")
  score = input("Enter score of player number " + str(i) + ":")
  outfile.write(name + "\n") # Add new line
  outfile.write(score + "\n") # Also add new line
  

