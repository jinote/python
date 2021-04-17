# Programming projects
# 71410
'''If you have downloaded the source code from this book's companion web site, you
will find the following files in the Chapter 07 folder:

• GirlNames.txt--This file contains a list of the 200 most popular names given to
girls born in the United States from the year 2000 through 2009.
• BoyNames.txt--This file contains a list of the 200 most popular names given to
boys born in the United States from the year 2000 through 2009.

Write a program that reads the contents of the two files into two separate
lists, allows a user to input either a girl's name, a boy's name, or
both, then tells the user whether the name(s) was/were popular between 2000 and
2009.

First, the program should prompt the user to choose a girl's name, a boy's name,
or both by entering either 'girl', 'boy', or 'both.'

Once they have chosen, they should be able to input a name. If the name was
a popular name, like Jacob or Sophia, the program should print "Jacob was a
popular boy's name between 2000 and 2009." or "Sophia was a popular girl's name
between 2000 and 2009."

If the name was not a popular name, like Voldemort, the program should print
"Voldemort was not a popular boy's name between 2000 and 2009."

If the user chooses to input both a girl and boy's name, ask for the boy's name,
then the girl's name, and print two statements in the form mentioned above on
two separate lines, with the statement about the boy's name coming first.
For example, if the user inputs Voldemort and then Sophia, print:

Voldemort was not a popular boy's name between 2000 and 2009.
Sophia was a popular girl's name between 2000 and 2009.'''

def search_boys():
  infile = open("c:\\temp\\BoyNames.txt", "r")
  boylist = infile.read()
  boylist = boylist.split('\n') # make the file nice and neat
  inflie.close() # better to close right away

  name = input("Enter a boy's name:")
  name = name.title() # handy function

  if name in boylist:
    print(name, "was a popular boy's name between 2000 and 2009.")
  else:
    print(name, "was not a popular boy's name between 2000 and 2009.")


def search_girls():
  infile = open("c:\\temp\\GirlNames.txt", "r")
  girllist = infile.read()
  girllist = girllist.split('\n') # make the file nice and neat
  inflie.close() # better to close right away

  name = input("Enter a girl's name:")
  name = name.title() # handy function

  if name in girllist:
    print(name, "was a popular girl's name between 2000 and 2009.")
  else:
    print(name, "was not a popular girl's name between 2000 and 2009.")

def main():
  choice = input("Enter 'boy', 'girl', or ' both':")
  if choice == 'boy':
    search_boys()
  elif choice == 'girl':
    search_girls()
  elif choice == 'both':
    search_boys
    search_girls
  else:
    print("invalid choice")
    
# 51287
'''A geometric progression is a sequence of numbers in which each value (after the first) is obtained 
by multiplying the previous value in the sequence by a fixed value called the common ratio. 
For example the sequence 3, 12, 48, 192, ... is a geometric progression in which the common ratio is 4.

Given the positive integer ratio greater than 1, and the non-negative integer n, 
create a list consisting of the geometric progression of numbers between (and including) 1 and n with a common ratio of ratio. 
For example, if ratio is 2 and n is 8, the list would be [1, 2, 4, 8].

Associate the list with the variable geom_prog.'''

ratio = 2
n = 8
total = 1
geom_prog = []

while total <= n:
  geom_prog.append(total)
  total = total * ratio

print(geom_prog)
