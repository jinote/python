# Exercise 51178
'''Fibonacci numbers are a sequence of integers, starting with 1, 
where the value of each number is the sum of the two previous numbers, 
e.g. 1, 1, 2, 3, 5, 8, etc. Write a function called fibonacci that takes a parameter, n, 
which contains an integer value, and have it return the nth Fibonacci number. 
(There are two ways to do this: one with recursion, and one without.)'''

# first answer
def fibonacci(n):
  a = 0
  b = 1
  for i in range(1, n+1):
    total = a + b
    a = b
    b = total
  return a

def main():
  n = int(input("Enter a number:"))
  fibonacci(n)
  
main()

# second answer
def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
 
def main():
  n = int(input('Enter a number'))
  print(fibonacci(n))
  
  
# 71404 tuition increase each year (5 years)
year = 1
tuition = 8000 # each year
while year <= 5:
  if year == 1:
    tuition = 1.03 * tuition
    print("In ", year, "the tuition will be $", tuition, ".", sep="")
    year = year + 1
  else:
    tuition = 1.03 * tuition
    print("In ", year, " years, the tuition will be $", tuition, ".", sep="")

    
