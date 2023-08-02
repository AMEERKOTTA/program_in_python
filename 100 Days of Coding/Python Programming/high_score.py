## You are going to write a program that calculates the highest score from a List of scores.
## e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

## Important you are not allowed to use the max or min functions. 
## The output words must match the example. i.e
##The highest score in the class is: x

## it will be splitted by comma.
student_scores = input("Input a list of student scores seperated by comma :  ").split(",")

## convert the each score from string to integer
for score in range(0, len(student_scores)):
      student_scores[score] = int(student_scores[score])
print(student_scores)

## lets assume the highest is the first one in the list
highest_score = student_scores[0]

## looping through the scores
for score in student_scores:
    #print(score)
    if score > highest_score:
        highest_score = score
        
print(f"The Highest Score is given by {highest_score}")