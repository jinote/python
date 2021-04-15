# string testing methods

isalnum()
isalpha()
isdigit()
islower()
isspace()
isupper()

# example
zipcode = "12345"
zipcode.isdigit()
-> True


# string modification methods
lower()
lstrip()
lstrip("char")
rstrip()
rstrip("char")
strip()
strip("char")
upper()

# find
mystr = 'one fish two fish'
mystr.find('one')
-> 0
mystr.find('fish')
-> 4
mystr.find('fisn', 8) # after 8th
-> 13
mystr.find('fish', 20)
-> -1 # bcz there is no 'fish' after 20th

# bring a file
infile = open("52weeklow.txt", "r")
mystr = infile.read()
mystr
-> 'AA\nAIES\nAKAO\nAMWD\NAN..........

print(mystr)
->
AA
AIES
AKAO
.
.
.

# replace
mystr.replace("\n", " ") # replaced "\n" with " "
-> AAA AEIS AKAO AMG AMWD AN AOS ...........

# split()
mystr = "one fish two fish"
mystr.split()
-> ["one", "fish", "two", "fish"]

## myprgramminglab 71412
'''Many companies use telephone numbers like 555-GET-FOOD so the number is easier
for their customers to remember. On a standard telephone, the alphabetic
letters are mapped to numbers in the following fashion:

A, B, C: 2
D, E, F: 3
G, H, I: 4
J, K, L: 5
M, N, O: 6
P, Q, R, S: 7
T, U, V: 8
W, X, Y, Z: 9

Write a program that asks the user to enter a 10-character telephone number in
the format XXX-XXX-XXXX. The application should display the telephone
number with any alphabetic characters that appeared in the original translated
to their numeric equivalent.

example:
Enter a phone number to be translated:555-GET-FOOD
555-438-3663'''

# 1. look through the given phone number (555-GET-FOOD)
# 2. send each char to the function
# 3. function will go through the tiers
          # return number or the original char

# answer
def replace(ch):
  if ch in "ABC":
    return "2"
  elif ch in "DEF":
    return "3"
  elif ch in "GHI":
    return "4"
  elif ch in "JKL":
    return "5"
  elif ch in "MNO":
    return "6"
  elif ch in "PQRS":
    return "7"
  elif ch in "TUV":
    return "8"
  elif ch in "WXYZ":
    return "9"
  else:
    return ch
  
def main():
  phone = input("Enter a phone number to be translated:")
  newstr = ""
  for i in phone:
    newstr = newstr + replace(i)
  print(newstr)
  
main()

# 71413
'''Write a program with a function that accepts a string as an argument and
returns a copy of the string with the first character of each sentence
capitalized. The program should let the user enter a string and then pass
it to the function, printing out the modified string.

example:
Enter sentence to be capitalized:hello. my name is Joe. what is your name?
Hello. My name is Joe. What is your name?'''

mystr = "hello. my name is Joe. what is your name?"
#index   0123456789

# try
newstr = mystr[0].upper()
newstr = newstr + mystr[1:7]
newstr = newstr + mystr[7].upper()

# solution1
sentence = "hello. my name is Joe. what is your name?"
i = 1
new_sentence = sentence[0].upper()

while i < len(sentence):
  if sentence[i] == ".":
    new_sentence = new_sentence + ". " + sentence[i+1].upper()
    i += 3
  else:
    new_sentence += sentence[i]
    i += 1
    
# solution2
def capitalize(sentence):
  for i in range(len(sentence)):
    if i == 0:
      sentence = sentence[0].upper() + sentence[1:]
    elif sentence[i] == "." and i != len(sentence) -1:
      sentence = sentence[:i+2] + sentence[i+2].upper() + sentence[i+3:]
  return sentence

s = input("Enter sentence to be capitalized:")
s = capitalize(s)
print(s)

# explanation for solution2
sentence = 'hello. my name is Joe. what is your name?'
#index      012345678
sentence[0].upper()
-> H

sentence = sentence[0].upper() + sentence[1:]
print(sentence[:5+2])
sentence[5+2].upper()
-> 'M'
sentence[5+3]
-> 'y'
sentence[5+3:]
-> 'y name is Joe. what is your name?'

# 51005
'''Given a variable s that is associated with non-empty string, 
write some statements that use a while loop to associate a variable vowel_count 
with the number of lower-case vowels ("a","e","i","o","u") in the string .'''
s = "one fish two fish"
i = 0
vowel_count = 0

while i < len(s):
  if s[i] in "aeiou":
    vowel_count += 1
  i += 1

print(vowel_count)

# 51758
'''write an expression that returns False 
if the str associated with s begins with "ecto"'''

not s.startswith('ecto')

#51279 
'''duplicates'''
has_dups = False
my_str = 'one fish two fish'

for ch in my_str:
  if my_str.count(ch) > 1:
    has_dups = True
