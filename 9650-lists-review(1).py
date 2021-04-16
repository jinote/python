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
