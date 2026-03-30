# Peter wants to generate some prime numbers for his cryptosystem. Help him! Your task is to generate all prime numbers between two given numbers!

# Input
# The input begins with the number t of test cases in a single line (t ≤ 10). In each of the next t lines there are two numbers m and n (1 ≤ m ≤ n ≤ 1000000000, n-m ≤ 100000) separated by a space.

# Output
# For every test case print all prime numbers p such that m ≤ p ≤ n, one number per line, test cases separated by an empty line.
import math

a = int(input())
b = int(input())

for num in range(a, b+1):
    
    if num < 2:
        continue
    
    prime = True
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            prime = False
            break
    
    if prime:
        print(num)

    