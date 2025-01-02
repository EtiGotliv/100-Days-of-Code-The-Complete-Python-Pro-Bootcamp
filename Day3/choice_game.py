print("""  ad88                               88 88
  d8"                                 "" 88
  88                                     88
MM88MMM ,adPPYYba, 88,dPYba,,adPYba,  88 88 8b       d8
  88    ""     `Y8 88P'   "88"    "8a 88 88 `8b     d8'
  88    ,adPPPPP88 88      88      88 88 88  `8b   d8'
  88    88,    ,88 88      88      88 88 88   `8b,d8'
  88    `"8bbdP"Y8 88      88      88 88 88     Y88'
                                                d8'
                                               d8'   """)
print("""*******************************************************************************
Welcome to Treasure Island.
Your mission is to find the treasure.""")
choice = input("""You're at a cross road. Where do you want to go?
      Type \"left\" or \"right\"""").lower()

if choice =="left":
    choice_two = input("""You've come to a lake. There is an island in the middle of the lake.
                    Type \"wait\" to wait for a boat.
                    Type \"swim\" to swim across.""").lower()
    if choice_two == "wait":
        col_choice = input("""You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue.
                 Which color do you choose?""").lower()
        if col_choice == "red":
            print("It's a room full of fire.Game Over!")
        elif col_choice == "yellow":
            print("You found thr treasure. You Win!")
        elif col_choice == "blue":
            print("You enter a room of beasts.Game Over!")
        else:
            print("You chose a door that doesn't trout. Game Over!")
    else:
        print("You got attacked by an angry trout.Game Over!")
else:
    print("You fell in to a hole.Game Over!")