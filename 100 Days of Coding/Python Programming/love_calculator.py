## You are going to write a program that tests the compatibility between two people.
## To work out the love score between two people:
## Take both people's names and check for the number of times the letters in the word TRUE occurs. 
## Then check for the number of times the letters in the word LOVE occurs. 
## Then combine these numbers to make a 2 digit number.
## For Love Scores less than 10 or greater than 90, the message should be:
## "Your score is **x**, you go together like coke and mentos."
## For Love Scores between 40 and 50, the message should be:
## "Your score is **y**, you are alright together."
## Otherwise, the message will just be their score. e.g.:
## "Your score is **z**."

name1 = input("Enter the your Name : ")
name2 = input("Enter your Lover Name : ")

name = name1 + name2

name_ = name.lower()

t = name_.count("t")
r = name_.count("r")
u = name_.count("u")
e = name_.count("e")

true = t + r + u + e
print(f"Number of Count in TRUE : {true}")

l = name_.count("l")
o = name_.count("o")
v = name_.count("v")
e = name_.count("e")

love = l + o + v + e
print(f"Number of count in LOVE : {love}")

# love_score = 
love_score = int(str(true) + str(love))
print(f"The Love score is : {love_score}")

if (love_score < 10 or love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos")

elif (love_score > 40 and love_score < 50):
    print(f"Your score is {love_score}, you are alright together.")

else:
    print(f"Your score is {love_score}.")