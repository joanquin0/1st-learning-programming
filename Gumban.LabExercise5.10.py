first = input("Enter path of first file:")
second = input("Enter path of second file:")

f = open(first,"r")
text = f.read().split("\n")
s = open(second, "r")
text2 = f.read().split("\n")

if text == text2:
    print("Yes")
else:
    print("No")
