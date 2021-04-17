# Dictionaries
## object that stores a collection of data
dictionary = {k1:v1, k2:v3, k3:v3}

# each element consists of a key(k) and a value(v) pair
# dictionaries are very fast - implemented using a technique called hashing
# keys must be immutable objects (no lists)
      # values can be any type of object
      # keys must be unique
# keys and values can be of different data types

dt = {}
# add new key and values
dt['Joe'] = ['111-111-1111', 'joe@gmail.com']
dt
-> {'Joe': ['111-111-1111', 'joe@gmail.com']}
dt['Bob': ['222-222-2222', 'bob@gmail.com']}
dt['Don': ['333-333-3333', 'don@gmail.com']}
dt
-> {'Joe': ['111-111-1111', 'joe@gmail.com'], 'Bob': ['222-222-2222', 'bob@gmail.com'], 'Don': ['333-333-3333', 'don@gmail.com']}

# print dict is ugly so make it better using pprint
import pprint
pprint.pprint(dt)
-> {'Joe': ['111-111-1111', 'joe@gmail.com'], 
    'Bob': ['222-222-2222', 'bob@gmail.com'], 
    'Don': ['333-333-3333', 'don@gmail.com']} # much better
   
# update bob's email address
dt['Bob'] = ['222-222-2222', 'bob2@gmail.com']
pprint.pprint(dt)
-> {'Joe': ['111-111-1111', 'joe@gmail.com'], 
    'Bob': ['222-222-2222', 'bob2@gmail.com'], # now updated  
    'Don': ['333-333-3333', 'don@gmail.com']} 

# retrieving a value
# get method
dt.get('john') # will show nothing because there is no john
dt.get('john', 'nothing found') # build a sentence that you want if there is no value 
-> 'nothing found'
dt.get('Bob')
-> ['Bob': ['222-222-2222', 'bob2@gmail.com']

# looping by key 1) 
for x in dt:
    print(x)
-> Joe
   Bob
   Don
    
# looping by key 2) 
for x in dt.keys():
    print(x)
-> Joe
   Bob
   Don

# lopping by value
for z in dt.values():
    print(z)
-> ['111-111-1111', 'joe@gmail.com'], 
   ['222-222-2222', 'bob2@gmail.com'],  
   ['333-333-3333', 'don@gmail.com']
    
# looping with both keys and values
for k,v in dt.items():
    print(k)
    print(v)
-> Joe
   ['111-111-1111', 'joe@gmail.com'], 
   Bob
   ['222-222-2222', 'bob2@gmail.com'],  
   Don    
   ['333-333-3333', 'don@gmail.com']
    
for k,v in dt.items():
    if k == "Joe" or "joe@gmail.com" in v[1]:
      print(v[0])
-> 111-111-1111
    
# deleting values
# del dt[key]
del dt['Bob']

# pop()
value = dt.pop(key, default_value)
    
 
