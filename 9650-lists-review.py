# lists are mutable 

list_a = ['jan', 'feb', 'mar', 'apr']
for i,e in enumerate(list_a):
  print(i)
  print(a)
  
# slice: a span of items that are taken from a sequence

list_a = ['a','b','c','d']
list_a[0:2]
-> ['a', 'b']
list_a[0:3]
-> ['a','b','c']

# reverse
list_a[::-1]
-> ['d','c','b','a']

# list methods: adding elements
# list.append(item)
# list.extend(item)
# list.insert(index, 

total = []
total.append('a')
total.append('b')
total.append('c')
total
-> ['a','b','c']

# list doesn't care about the uniquness
total.append('c')
total
-> ['a','b','c','c']

list_b = ['jan', 'feb', 'mar']
list_b.append('apr')
list_b
-> ['jan', 'feb', 'mar', 'apr']

# extend() <- it's good for list + list
list_b.extend('may')
list_b
-> ['jan', 'feb', 'mar', 'apr', 'm', 'a', 'y']

list_c = ['apr', 'may', 'jun']
list_b.extend(list_c)
list_b
-> ['jan', 'feb', 'mar', 'apr', 'may', 'jun']

# add one more variable
list_b + 'jul'
-> ERROR!

list_b + ['jul']
list_b
-> ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul']
list_b = list_b + ['jul']
list_b
-> ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul']

# comparison of extend() and append()
list_b.extend(['aug'])
list_b
-> ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug']

list_b.append(['sep'])
list_b
-> ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', ['sep']]

# insert
list_b.insert(4, 'dec') # don't need to add []
-> ['jan', 'feb', 'mar', 'apr', 'dec', 'may', 'jun', 'jul', 'aug', ['sep']]

# list methods: searching

# list.index(item)
list_b.index('dec')
-> 4

# list.count(item)
list_b.count('aug')
-> 1

# list.sort()
# cannot sort mix types
list_b[-1] = 'sep'
list_b
-> ['jan', 'feb', 'mar', 'apr', 'dec', 'may', 'jun', 'jul', 'aug', 'sep']

list_b.sort() # alphabet order
-> ['apr', 'aug', 'dec', 'feb', 'jan', 'jul', 'jun', 'mar', 'may', 'sep'] 

# reverse()
list_b.sort(reverse=Ture)
-> ['sep', 'may', 'mar', ........ 'aug', 'apr'] 

list_b.reverse() # modified
-> ['sep', 'may', 'mar', ........ 'aug', 'apr'] 

# but when you use 
list_b[::-1] # it's just a copy so,
list_b = list_b[::-1] # saved now
-> ['sep', 'may', 'mar', ........ 'aug', 'apr'] 

# Delete elements

# list.remove(item) - NOT index
list_b.remove('dec')
-> ['apr', 'aug', 'feb', 'jan', 'jul', 'jun', 'mar', 'may', 'sep'] 

list_c = [1,2,3,4]
list_c.pop(-1)
-> 4
list_c
-> [1,2,3]
list_d = []
list_d.append(list_c.pop(-1))
list_d.append(list_c.pop(-1))
list_d.append(list_c.pop(-1))
list_c
-> [] # empty
list_d
-> [3,2,1] # fill

# del statement
del list_b[-1]
-> ['apr', 'aug', 'feb', 'jan', 'jul', 'jun', 'mar', 'may'] 

# math functions for lists
grades = [99,98,88,76]
sum(grades)
-> 361
sum(grades)/len(grades)
-> 90.25
max(grades)-min(grades)
-> 23
list_b = ['jan', 'feb', 'mar', 'apr']
list_b.sort()
list_b
-> ['apr', 'feb', 'jan', 'mar']


# list comprehension
doubles_odds = []
for n in numbers:
  if n % 2 == 1:
    doubled_odds.append(n*2)
    
doubled_odds = [n * 2 for n in numbers if n % 2 == 1]

# different filtering list problems
old_list = [1,3,5,7,8,23,66]
new_list = []
for n in old_list:
  if n > 8:
    new_list.append(n)
    
print(new_list)

# list comprehendsion
old_list = [1,3,5,7,8,23,66]
new_list = [n for in old_list if n == 8 or n == 66]
print(new_list)
-> [8, 66]

years = [str(n) for n in range(2000,2022)]
years
-> ['2000', '2001', '2002', '2003', '2004'.....'2021']

infile = oepn("c:\\temp\\52weekslow.txt","r")
mylist = infile.readlines()

newlist = [for n in mylist if n.startswith("A")]
newlist
['AA', 'AEIS', 'AMG', 'AMWD', 'AN', 'AOS'......]

# two-dimensional lists
mx = [[1,2,3],[4,5,6],[7,8,9]]
mx[0]
-> [1,2,3]
mx[1]
-> [4,5,6]
type(max[0])
-> <class 'list'>


