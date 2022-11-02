# CHALLENGES

#? 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
  sum = 0 
  for num in range(1, (n + 1)):
    sum += num
  return sum

print(sum_to(6))
print(sum_to(10))


#? 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(nums):
  large = 0
  for num in nums:
    if num > large:
      large = num
  return large

print(largest([1,3,6,4, 0]))
print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))

