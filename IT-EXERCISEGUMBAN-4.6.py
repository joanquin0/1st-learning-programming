x = int(input("Enter iterations:"))

for x in range(a):
    dtor = ((2 * x ) + 1 * (-1)** x)
    if dtor == 1:
        print(dtor, end="")
    elif dtor > 0:
        nrator = 1
        print("+", nrator, "/",dtor, end="")
    else:
        nrator = 1
        d = dtor * -1
        print("-", nrator, "/", d, end="")

