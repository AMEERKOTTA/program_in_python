## You are going to write a virtual coin toss program. 
## It will randomly tell the user "Heads" or "Tails".

import random

## choose a number 0 or 1 randomly
## then if the number is 0
## print "TAIL"
## else print "HEAD"

random_number = random.randint(0,1)
print(random_number)

if random_number == 0:
    print("TAILS")
else:
    print("HEADS")