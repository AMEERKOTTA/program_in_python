## You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
## Thus, the first even number would be 2 and the last one is 100:

even_sum = 0

for number in range(0,101):
    if number % 2 == 0:
        even_sum += number
    else:
        pass

print(even_sum)