## Create a program using maths and f-Strings that tells us how many days, 
## weeks, months we have left if we live until 90 years old.
## It will take your current age as the input and output a message with our time left in this format:
## You have x days, y weeks, and z months left.
## Where x, y and z are replaced with the actual calculated numbers.

## define the age right now from the user
age = int(input("Enter your Age : "))

## define the maximum age
age_max = 90

## so the remaining years you have is (age_max - age).
remaining_years = age_max - age
print(f"The Remaining years you have left is : {remaining_years}")

## calculate the years in months, weeks and days
remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 52
remaining_days = remaining_years * 365

print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months to live !!!")