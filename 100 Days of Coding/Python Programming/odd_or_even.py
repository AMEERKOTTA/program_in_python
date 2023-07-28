## Write a program that works out whether if a given number is an odd or even number.

## get the integer number from the user
number = int(input("Enter the Your Choice of Number : "))

## checking whether the number is even or odd
## even number can be divided by 2 completely
## odd number will leave a reminder if we divide by 2

## checking using the conditional statements
def even_odd(number):

    if number % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

print(f"The number {number} you selected is an {even_odd(number)}")