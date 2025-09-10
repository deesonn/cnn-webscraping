'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000. 
'''

# if num % num == 0
total = 0

for num in range(1,1000):
    if num % 3 == 0 or num % 5 == 0:
        total += num
        
print(total)

total = 0
i = 0
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        total += i
    i += 1

print(total)