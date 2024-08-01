## write a program to add even and odd numbers from a range of 1 to n.
## sum of all even numbers from 1 to n
## sum of all odd numbers from 1 to n

## even numbers 
def even_sum(n):
    even_sum = 0
    for number in range(0,n+1):
        if number % 2 == 0:
            even_sum += number

    return even_sum

## odd numbers
def odd_sum(n):
    odd_sum = 0
    for number in range(0,n+1):
        if number % 2 != 0:
            odd_sum += number

    return odd_sum

print("The Sum of Even Numbers from 1 to 100 is : ", even_sum(100))
print("The Sum of Odd Numbers from 1 to 100 is : ", odd_sum(100))


