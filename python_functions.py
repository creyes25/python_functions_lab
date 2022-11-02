# CHALLENGES

#? 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
  sum = 0 
  for num in range(1, (n + 1)):
    sum += num
  return sum

print('Sum: ' ,sum_to(6))
print('Sum: ' ,sum_to(10))


#? 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(nums):
  large = 0
  for num in nums:
    if num > large:
      large = num
  return large

print('Largest Number: ' ,largest([1,3,6,4, 0]))
print('Largest Number: ' ,largest([1, 2, 3, 4, 0]))
print('Largest Number: ' ,largest([10, 4, 2, 231, 91, 54]))

#? 3. Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

def occurrences(str1, str2):
  return(str1.count(str2))
  
print('Number of occurrences: ', occurrences('fleep floop', 'p')   )
print('Number of occurrences: ', occurrences('fleep floop', 'e'))   
print('Number of occurrences: ', occurrences('fleep floop', 'ee') ) 
print('Number of occurrences: ', occurrences('fleep floop', 'fe') ) 