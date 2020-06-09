import random
print("This is a dice stimulator")
m="y"
while m=="y":
    x=random.randint(1,6)
    if x==1:
        print("----------")
        print("|        |")
        print("|   O    |")
        print("|        |")
        print("----------")
    if x==2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
    if x==3:
        print("----------")
        print("|    O   |")
        print("|    O   |")
        print("|    O   |")
        print("----------")
    if x==4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
    if x==5:
        print("----------")
        print("|   O    |")
        print("| O    O |")
        print("| O    O |")
        print("----------")
    if x==6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")
    m=input("Press y to roll again : ")
