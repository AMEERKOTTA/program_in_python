## calculate the average height of students
## from the list of heights given.

students_heights = [165,167,170,175,177,180,185,190]

## without using the len function
## using for loops

total_height = 0
number_of_students = 0
for height in students_heights:
    total_height += height

for height in students_heights:
    number_of_students += 1

average_height = total_height / number_of_students


print("Total Height of all students : ", total_height)
print("Total Number of Students : ", number_of_students)
print("Average Height : ", average_height)