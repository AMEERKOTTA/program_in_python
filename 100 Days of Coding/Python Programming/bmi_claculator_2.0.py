## Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
## It should tell them the interpretation of their BMI based on the BMI value.

## Under 18.5 they are underweight
## Over 18.5 but below 25 they have a normal weight
## Over 25 but below 30 they are slightly overweight
## Over 30 but below 35 they are obese
## Above 35 they are clinically obese.

## collect height and weight from the user
weight = float(input("Enter Your Weight in KG: ??"))
height = float(input("Enter Your Height in metres : ??"))

## develop a function to calculate the BMI
# def bmi_calculator(weight, height):

#     bmi_value = (weight / (height ** 2))
#     ## round the value to two decimal places 
#     bmi_value = round(bmi_value, 2)

#     return bmi_value

# print(bmi_calculator(weight, height))

bmi_value = (weight / (height ** 2))
## round the bmi value to 2 decimal places
bmi_value = round(bmi_value, 2)


if bmi_value < 18.5:
    print(f"Your bmi value is {bmi_value}, YOU ARE UNDER WEIGHT !!")
elif bmi_value < 25:
    print(f"Your bmi value is {bmi_value}, YOU ARE NORMAL WEIGHT !!")
elif bmi_value < 30:
    print(f"Your bmi value is {bmi_value}, YOU ARE SLIGHTLY OVERWEIGHT")
elif bmi_value < 35:
    print(f"Your bmi value is {bmi_value}, YOU ARE OBESE")
else:
    print(f"Your bmi value is {bmi_value}, YOU ARE CLINICALLY OVERWEIGHT")