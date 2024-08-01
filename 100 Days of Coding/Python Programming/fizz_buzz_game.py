# FIZZ BUZZ GAME
# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 
# then instead of the number it should print "FizzBuzz"

## define the number n so that user can selecty the number
n = int(input("Enter the Number : "))
## then loop through the range of that number.
for number in range(1,n+1):
    ## if number is both divisible by 3 and 5
    ## print FIZZ BUZZ
    if (number % 3 == 0) and (number % 5 == 0):
        print("FIZZ BUZZ")
    ## if the number is divisible by 3 only
    ## print FIZZ
    elif number % 3 == 0:
        print("FIZZ")
    ## if the number is divisible by 5 only
    ## print BUZZ
    elif number % 5 == 0:
        print("BUZZ")
    ## if nothing happens, print the number.
    else:
        print(number)