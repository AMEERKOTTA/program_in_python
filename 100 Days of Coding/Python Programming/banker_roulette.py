## You are going to write a program that will select a random name from a list of names. 
## The person selected will have to pay for everybody's food bill.
## Important: You are not allowed to use the choice() function.

import random

name_list = input("Give the names of People had Food seperated by comma : ")
print(name_list)
names = name_list.split(",")
print(names)

## choose a random index from the list
## then ghet the random name from list.
random_index = random.randint(0, len(names) - 1)
random_name = names[random_index]

print(f"Today, the Bill will be Paid by {random_name}")

