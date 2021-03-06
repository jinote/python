# 9650_mylab_ch6
#71408
'''Assume that a file containing a series of integers is named numbers.txt. Write
a program that calculates the average of all the numbers stored in the file.'''

outfile = open('numbers.txt', 'r')
total = 0
count = 0 
for num in outfile:
  num = int(num) # required
  total += num
  count += 1

average = total / count
print(average)


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



