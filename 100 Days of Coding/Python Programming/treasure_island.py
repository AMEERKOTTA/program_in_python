## this is game to find the treasure island
## here is the link to the flow chart diagram
## https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

## choose between left or right,
## if you choose right, you will fall into a holl. the game will be over.
## if you choose left, there will be next step

## step 1 
print("You are in a position to where you can choose to move left or right to get the Treasure!!")
level_1 = input("Choose betweeen left or right : ???")

## make the step 1 to lower case
level_1 = level_1.lower()

if level_1 == "left":
    print("You have reached near a Pond, You can either Wait or Swim through the Pond!!!")
    level_2 = input("Choose between Swim or Wait ???")
    ## make the choice in lower letters
    level_2 = level_2.lower()
    if level_2 == "wait":
        print("A boat will arrive and pick you up")
        print("And you will be moved to a Hall")
        print("There you can find three Doors")
        print("Choose between the Doors, Red, Blue and Yellow ???")
        level_3 = input("Choose between doors (red/blue/yellow) : ???")
        level_3 = level_3.lower()
        if level_3 == "yellow":
            print("YOU WIN, YOU GOT THE TREASURE!!!")
        elif level_3 == "blue":
            print("Eaten by a Beast, Game over !!!")
        elif level_3 == "red":
            print("Burned by Fire, Game over !!!")
        else:
            print("Game Over    !!!!!")
    else:
        print("Attacked by a Trout, Game over !!!")
else:
    print("You fall into a Holl, Game Over !!!")
