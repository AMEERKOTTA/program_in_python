## write a program to calculate the bmi value of a person.
## bmi = body mass index
## bmi = weight in kg / (height in m)^2

weight = float(input("Enter your Weight in Kg : "))
height = float(input("Enter your Height in metres : "))

## calculating bmi
## round the values into two decimal places

bmi = weight / (height ** 2)

print(f"Your BMI is given by : {round(bmi,2)}")

