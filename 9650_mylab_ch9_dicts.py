# chap9 programming projects
# 71414
room_dict = {
'CS101': '3004',
'CS102': '4501',
'CS103': '6755',
'NT110': '1244',
'CM241': '1411'
}
inst_dict = {
'CS101': 'Haynes',
'CS102': 'Alvarado',
'CS103': 'Rich',
'NT110': 'Burke',
'CM241': 'Lee'
}
meet_dict = {
'CS101': '8:00am',
'CS102': '9:00am',
'CS103': '10:00am',
'NT110': '11:00am',
'CM241': '1:00pm'
}

key = input('Enter a class name:')
print('Class:', key)
print('Room:', room_dict.get(key))
print('Instructor'. inst_dict.get(key))
print('Time:', meet_dict.get(key))

# progrmming projects
# 71414
'''
Harry Potter
theboywholived@hogwarts.edu
Hermione Granger
brightestwitch@hogwarts.edu
Ron Weasley
roonilwazlib@hogwarts.edu
Draco Malfoy
myfatherwillhearaboutthis@hogwarts.edu
Severus Snape
halfbloodprince@hogwarts.edu
Albus Dumbledore
alasearwax@hogwarts.edu'''

# try to read the file 'phonebook.in'
infile = open("phonebook.in", "r")
mylist = infile.readline()

mylist[0::2]
mylist[1::2]

infile.close()

# another try to read the file 'phonebook.in' - better one
infile = open("phonebook.in", "r")
mylist = infile.read()
mylist = mylist.split('\n') # be careful the last empty one because of \n

infile.close()

mylist[0::2] # only name
mylist[1::2] # only email

my_dt = zip(mylist[0::2], mylist[1::2])
my_dt = dict(my_dt) # convert it to dict


# let's apply def and solution
def get_phonebook():
  infile = opne("phonebook.in", "r")
  mylist = infile.read().split('\n')
  my_dt = dict(zip(mylist[0::2], mylist[1::2]))
  infile.close()
  return my_dt

def email_lookup(my_dt):
  name = input("Enter a name:")
  my_dt.get(name, "Sorry, no contact exists under that name.")
  
def add_name_email(my_dt):
  name = input("Enter name:")
  email = input("Enter email address:")
  my_dt[name] = email
  
def change_email(my_dt):
  name = input("Enter name:")
  email = input("Enter new email address:")
  my_dt[name] = email

def del_name(my_dt):
  name = input("Enter name:")
  del my_dt[name]
  
def save_phonebook(my_dt):
  outfile = open("phonebook.out", "w")
  for k,v in sorted(my_dt.items()):
    outfile.write(k + "\n")
    outfile.write(v + "\n")
  outfile.close()
  
def display_menu():
  print("Enter")
  print("1) look up an email address")
  print("2) add a new name and email address")
  print("3) change an email address")
  print("4) delete a name and email address")
  choice = input("5) save address book and exit") # it's a choice
  return choice

def main():
  phone_dt = get_phonebook()
  while True:
    choice = display_menu()
    if choice == "1":
      email_lookup(phone_dt)
    elif choice == "2":
      add_name_email(phone_dt)
    elif choice == "3":
      change_email(phone_dt)
    elif choice == "4":
      del_name(phone_dt)
    elif choice == "5":
      save_phonebook(phone_dt)
      break

main()
