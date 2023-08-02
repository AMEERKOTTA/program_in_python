## create a password generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
           'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
           'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

## import the random module
import random

## get the letters sequence
letter_number = int(input("Enter the number of letters needed in the Password : ???"))
letters_ = ""
for loop in range(0, letter_number + 1):
    random_letter = random.choice(letters)
    letters_ += random_letter
    
print(letters_)

## get the number sequence
number_number = int(input("Enter the number of numbers needed in the Password : ???"))
numbers_ = ""
for loop in range(0, number_number + 1):
    random_number = random.choice(numbers)
    numbers_ += random_number

print(numbers_)

## get the symbol sequence
sequence_number = int(input("Enter the number of symbols needed in the password : ???"))
symbols_ = ""
for loop in range(0, sequence_number + 1):
    random_symbols = random.choice(symbols)
    symbols_ += random_symbols

print(symbols_)

password = letters_ + numbers_ + symbols_
print(password)


## shuffle the password
## using the shuffling method of random module
password_ = list(password)
random.shuffle(password_)
password_ = "".join(password_)
print(f"The Password is given by : {password_}")