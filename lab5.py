# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it
"""
So, this one confused me... I will have to revist this soon. Before the next unit of course. 

"""

fib1 , fib2 =0,1

while fib2  <50:
    print(f'term: {fib1 + fib2 } / number: {fib2 +1}')
    fib1, fib2 = fib1, fib2+1
    


#the solution below gave me an endless loop of epic portions
#     fibterm = 0
# fib1, fib2 = 1, 2

# while fibterm <= 50:
#     print(f'term: {fib1 + fib2 } / number: {fib2 +1}')
#     fib1, fib2 = fib1, fib2+fib2
