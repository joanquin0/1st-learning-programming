f1 = input("Enter file 1: ")
f2 = input("Enter file 2: ")
content = input("Enter contents of file 1 and 2:")

f = open(f1, "w")
f.write(content)

f = open(f2, "w")
f.write(content)
