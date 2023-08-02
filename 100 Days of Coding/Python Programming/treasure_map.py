## You are going to write a program that will mark a spot with an X.
## In the starting code, you will find a variable called map.
## This map contains a nested list. When map is printed this is what the nested list looks like:
## [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
## This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}" to format the 3 lists to be printed as a 3 by 3 square, each on a new line. 
## ['⬜️', '⬜️', '⬜️']
## ['⬜️', '⬜️', '⬜️']
## ['⬜️', '⬜️', '⬜️']

## Now it looks a bit more like the coordinates of a real map:




row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


horizontal = int(position[0])
print(horizontal)
vertical = int(position[1])
print(vertical)

selected_row = map[vertical-1]
selected_row[horizontal-1] = "X"

## print the output
print(f"{row1}\n{row2}\n{row3}")