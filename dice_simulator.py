import random

print("\n\t\tDice Simulator\t\t")

again=True

while again:
    a=int(input("\nChoose a number from 1 to 6 -: "))

    if a>0 and a<7:
        b=random.randint(1,6)
        print("You choose",a,"You get",b)
        if a==b:
            print("\nCongratulations you guess the right number\n")
        else:
            print("\nOops! you guess wrong")
        another_roll=input("want to roll the dice again?  (y/n): ")
        if another_roll.lower() == "y":
            continue
        else:
            break
    else:
        print("Out of range")
