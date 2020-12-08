from random import randint

a = randint(1,6)
b = randint(1,6)
c = int(input("Please enter money in the pot:"))
sum = a+b


i = 0
while c > 0:
    print("You have", "$", c, "in the pot")
    c -= 1
    if sum == 7:
        print("won")
        break
    else:
        print("loss")
    while True:
        br = c
        d = input("Enter YES if you want to continue and NO if not:")
        if d == "yes":
            br = True
            break
        else:
            br = False
            break





