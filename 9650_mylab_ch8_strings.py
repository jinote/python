# 9650_mylab_ch8_strings

# programming_projects_71412
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
to their numeric equivalent.'''

# 1) loop through the given phone number (555-GET-FOOD)
# 2) send each char to the function
# 3) function will go through the tiers
      # return number or the original char
  
  
def replace(ch):
  if ch in 'ABC':
    return '2'
  elif ch in 'DEF':
    return '3'
  elif ch in 'GHI':
    return '4'
  elif ch in 'JKL':
    return '5'
  elif ch in 'MNO':
    return '6'
  elif ch in 'PQRS':
    return '7'
  elif ch in 'TUV':
    return '8'
  elif ch in 'WXYZ':
    return '9'
  else:
    return ch
  
phone = input("Enter a phone number to be translated:")
for i in phone:
  print(replace(i), end="")
  
# 2nd try for the for loop
phone_num = ""
for ch in phone:
  phone_num += replace(ch) # You need to apply the def
print(phone_num)
  
 
# 3rd try for the for loop
def main():
  phone = input("Enter a phone number to be translated:")
  phone_num = ""
  for ch in phone:
    phone_num += replace(ch)
  print(phone_num)
  
main()


# 71413
'''Write a program with a function that accepts a string as an argument and
returns a copy of the string with the first character of each sentence
capitalized. The program should let the user enter a string and then pass
it to the function, printing out the modified string.'''

# First answer
def cap_first(st):
  cap_list = []
  split_st = st.split(". ")
  for x in split_st:
    
  cap_list.append(x[0].capitalize()+x[1:])
  cap_st = ". ".join(cap_list)
  return cap_st

s = input("Enter sentence to be capitalized:")
print(cap_first(s))

# practice
mystr = "hello. my name is Joe. what is your name?"
mystr.split(". ")
# ['hello', 'my name is Joe', 'what is your name?']
newstr = ""
newstr = mystr[0].upper()
newstr
# H

newstr = newstr + mystr[1:7] # because m is 6th
newstr
# 'Hello. '
newstr = newstr + mystr[7].upper()
# 'Hello. M'
newstr = newstr + mystr[8]

# second answer
sentence = input("Enter sentence to be capitalized:")
i = 1
new_sentence = sentence[0].upper()

while i < len(sentence):
  if sentence[i] == "." and i < len(sentence)-2:
    new_sentence = new_sentence + ". " + sentence[i+2].uuper()
  else:
    new_sentence = sentence[i]
    i += 1
    
print(new_sentence)

# third try
def capitalize(sentence):
  for i in range(len(sentence)):
    if i == 0:
      sentence = sentence[0].upper() + sentence[1:]
    elif sentence[i] == "." and i != len(sentence)-1:
      sentence = sentence[:i+2] + sentence[i+2].upper() + sentence[i+3:]
  return sentence

s = input("Enter sentence to be capitalized:")
s = capitalize(s)
print(s)

# 51005
s = "one fish two fisn"
i = 0
vowel_count = 0
while i < len(s):
  if s[i] in 'aeiou':
    vowel_count += 1
  i += 1
  
# 51279
has_dups = False
my_str = "one fish two fish"
for ch in my_str:
  if my_str.count(ch) > 1:
    has_dups = True

print(has_dups)
