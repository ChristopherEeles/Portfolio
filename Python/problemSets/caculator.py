######## Exercises 1 ########

#### Input and Output ####

# Write a program called "hello.py" which asks the user for a name, and then personally greets them.

i = input("Enter your name: ")

print("Hello ", i, "!", sep='')

# Write a program called repeater.py which reads a stirng and then prints it out twice.

i = input("Enter a string: ")
print(i*2, sep=' ')

# Write a program called multiplyer.py which reads a number, then prints out double that number.

i = int(input("Enter a number: "))
print(i*2)

#### Box Printing ####

# Write a program which prints a box. You should use the plus, minus and pipe characters.

print("+---+\n|   |\n+---+\n")

# Write a program which reads a string and prints a box around it.

i = input("Enter a string: ")
l = len(i) + 2

print("+", "-"*l, "+", sep='')
print("| ", i, " |", sep='')
print("+", "-"*l, "+", sep='')

#### Calculator ####

# Write a program which reads two numbesr and prints their sum.

#a = int(input("Enter a number: "))
#b = int(input("Enter a number: "))
#print(a + b)

a, b = [int(a)
        for a in input("Enter two numbers separated by a space: ").split()]
print(a + b)

# Subtract
print(a-b)

# Multiply
print(a*b)

# Divide
print(a/b)

# General purpose calculator

a, o, b = [x for x in input(
    "Enter a mathematical expression separated by spaces: ").split()]
a = int(a)
b = int(b)

if o == "/" or o == "\\":
    print(a/b)
elif o == "+":
    print(a+b)
elif o == "-":
    print(a-b)
elif o == "*" or o == "+":
    print(a*b)
else:
    print("Invalid input!")


def calculator():
    # Calculator any notation!
    opr = []
    nmbr = []

    for val in input("Enter a mathematical expression separated by spaces: ").split():
        check = list(val)
        # print(check)
        test = True
        for char in check:
            # print(ord(char),ord("0"),ord("9"))
            if ord(char) not in range(ord("0"), ord("9")):
                test = False
        # print(test)
        if test == False:
            opr = opr + [val]
        else:
            nmbr = nmbr + [int(val)]

    # print(opr,nmbr)

    for i in range(len(opr)):
        if i == 0:
            if opr[i] == "/" or opr[i] == "\\":
                res = nmbr[i]/nmbr[i+1]
            elif opr[i] == "+":
                res = nmbr[i]+nmbr[i+1]
            elif opr[i] == "-":
                res = nmbr[i]-nmbr[i+1]
            elif opr[i] == "*" or opr[i] == "+":
                res = nmbr[i]*nmbr[i+1]
            else:
                return("Invalid input!")
        else:
            if opr[i] == "/" or opr[i] == "\\":
                res = res + nmbr[i+1]
            elif opr[i] == "+":
                res = res + nmbr[i+1]
            elif opr[i] == "-":
                res = res - nmbr[i+1]
            elif opr[i] == "*" or opr[i] == "+":
                res = res * nmbr[i+1]
            else:
                return("Invalid input!")

    print("Result is", res)


calculator()
