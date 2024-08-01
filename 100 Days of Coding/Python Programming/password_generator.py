#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
           'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
           'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

## password should be (nr_letters + nr_symbols + nr_nnumbers)
## step 1 : generating alphabets in randomly from the letters list.
random_letters = random.sample(letters, nr_letters)
## join that letter together
alphabets_ = "".join(random_letters)
print("The Selected Alphabets : ",alphabets_)

## step 2 : generating numbers from the number list
random_numbers = random.sample(numbers, nr_numbers)
## join that together
number_ = "".join(random_numbers)
print("The Selected Numbers : ",number_)

random_symbols = random.sample(symbols, nr_symbols)
## join them together
symbols_ = "".join(random_symbols)
print("The Selected Symbols : ",symbols_)


password = alphabets_ + number_ + symbols_
print("Generated Password is : ",password)

## now i have the password
## i want to shuffle it
char_list = list(password)
print("The List of Charachters in the Selected Password : ", char_list)
## now shuffle the list
random.shuffle(char_list)
print("List of Shuffled Charecters : ", char_list)
## combine them together again
password_ = "".join(char_list)
print(f"The Required Password is : {password_}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P