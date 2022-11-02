# CHALLENGES

#? 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
  sum = 0 
  for num in range(1, (n + 1)):
    sum += num
  return sum

print(sum_to(6))
print(sum_to(10))


