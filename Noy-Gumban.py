#Simplified calculator

#method for addition
def add(*x):
    counter = 1
    count = 0
    total = numList[count]
    for i in range(num - 1):
        total = total + numList[counter]
        counter += 1
    print(total)
    pass

#method for subtraction
def subtract(*x):
    counter = 1
    count = 0
    total = numList[count]
    for i in range(num - 1):
        total = total - numList[counter]
        counter += 1
        
    print(total)
    pass

#method for multiplication
def multiply(*x):
    counter = 1
    count = 0
    total = numList[count]
    for i in range(num - 1):
        total = total * numList[counter]
        counter += 1
        
    print(total)
    pass

#method for division
def divide(*x):
    counter = 1
    count = 0
    total = float(numList[count])
    for i in range(num - 1):
        total = total // numList[counter]
        counter += 1
        
    print(total)
    pass

#Asks for how many integers to be calculated
num = int(input("How many integers to be calculated: "))
numList = []
count = 1
#loop for asking the numbers
for i in range(num):
    x = float(input("Enter number " + str(count) + ": "))
    numList.append(x)
    count += 1

#Prints the choices of method
print("Choose what operation to use: ")
print("1. Addition ")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


#Conditional statements to determine the choice of the user
method = int(input("Enter number of your choice: "))
while method >= 1 or method <= 4:
    if method == 1:
        add()
        operation = "Addition"
        break
    elif method == 2:
        subtract()
        operation = "Subtraction"
        break
    elif method == 3:
        multiply()
        operation = "Multiplication"
        break
    elif method == 4:
        divide()
        operation = "Division"
        break
    else:
        print("Invalid choice")
        method = int(input("Enter number of your choice: "))




with open('log.txt', 'w') as logfile:
    logfile.write("Numbers in the list: \n")
    logfile.write(str(numList))
    logfile.write("\nOperation Used: " + operation)
    

