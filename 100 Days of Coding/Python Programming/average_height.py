## You are going to write a program that calculates the average student height from a List of heights.
## e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
##The average height can be calculated by adding all the heights together and dividing 
        ## by the total number of heights.

## e.g.180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
## There are a total of 7 heights in student_heights
##  1146 ÷ 7 = 163.71428571428572

## Average height rounded to the nearest whole number = 164

## Important You should not use the sum() or len() functions in your answer. 
## You should try to replicate their functionality using what you have learnt about for loops.

## the split will split the string by comma.
student_heights = input("Input a list of student heights seperated by comma").split(",")
print(student_heights)

## converting the string to integer
for height in range(0, len(student_heights)):
    student_heights[height] = int(student_heights[height])

print(student_heights)

## taking the sum using the for loop instead of using sum function
height_sum = 0
for heights in student_heights:
    print(heights)
    height_sum += heights
print(f"The Total Height of the Students is {height_sum}")


## takinhg the count of number of students without using len function
## initiate number of students = 0
num_of_students = 0
for student in student_heights:
    num_of_students += 1
print(f"The Number of Students is {num_of_students}")

## taking the average
## round the value using the round function
average_height = round(height_sum / num_of_students)
print(f"Average Height is given by : {average_height}")