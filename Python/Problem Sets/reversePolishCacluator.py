######## Exercises 2 ########

#### Revision ####

# Divide


def rem():

    a, b = [int(x) for x in input(
        "Enter two numbers separated by a space: ").split()]
    print(a//b, " times with remainder: ", a % b, sep="")


rem()


def div_check():
    a, b = [int(x) for x in input(
        "Enter two numbers separated by a space: ").split()]
    print(a//b, " times with remainder: ", a % b, sep="")
    print("Check: ", b, " * ", a//b, " = ", b*(a//b), sep='')
    print(b*(a//b), " + ", a % b, " = ", b*(a//b)+(a % b))


div_check()

#### Input and Lists ####

# Word counter


def wc():
    i = [x for x in input("Enter a sentence: ").split()]
    print(len(i))


wc()

# Sum list


def sum_ls():
    i = [int(x) for x in input(
        "Enter a comma separated list of numbers: ").split(',')]
    result = 0

    for x in i:
        result = result + x
    print(result)


sum_ls()

#### Accumulator ####

# Accumulate in list


def accumulate():

    acc = []
    while(True):

        i = [int(x) for x in input("Enter a number: ").split()]

        if i == []:
            break
        else:
            acc = acc + i
            print(acc)


accumulate()

# Clean accumulate


def acc_cl():

    acc = []
    while(True):

        i = [int(x) for x in input("Enter a number: ").split()]
        sum_acc = 0
        str_acc = []

        if i == []:
            break
        else:
            acc = acc + i
            for num in acc:
                sum_acc = sum_acc + num
                str_acc = str_acc + [str(num)]
            print(" + ".join(str_acc), " = ", sum_acc, sep=' ')


acc_cl()

#### Word Count ####


def word_count():

    lines, characters, words = 0, 0, 0

    while(True):

        i = [x for x in input("Enter a sentence: ").split()]

        if i == []:
            break

        words = words + len(i)
        lines = lines + 1

        for word in i:
            characters = characters + len(word)

        print("Lines: ", lines, "Words: ", words, "Characters: ", characters)


word_count()

#### Read Code ####

# What does the code do.

marks = []

while True:
    x = int(input())

    for i in range(len(marks)):
        if x < marks[i]:
            marks.insert(i, x)
            break

    if x not in marks:
        marks = marks + [x]

    print(marks)

#### Advanced ####

# Sized box


def makeBox():
    horiz = abs(int(input()))
    vert = horiz//2 + 1

    print("+", "-"*horiz, "+", sep='')
    for x in range(1, (vert)):
        print("|", " "*horiz, "|", sep='')
    print("+", "-"*horiz, "+", sep='')


makeBox()

# Reverse Polish Notation Calculator

nmbr = []
opr = []
res = 0

while(True):
    i = input()

    if i == "":
        break

    test = list(i)
    check = False

    for char in test:
        if ord(char) not in range(ord("0"), (ord("9")+1)):
            check = True

    if check == True:
        opr = opr + [i]
    else:
        nmbr = nmbr + [int(i)]

    count = 0

    for val in opr:
        if count == 0:
            if val == "+":
                res = nmbr[count] + nmbr[count + 1]
            elif val == "-":
                res = nmbr[count] - nmbr[count + 1]
            elif val == "*":
                res = nmbr[count] * nmbr[count + 1]
            elif val == "/":
                res = nmbr[count] / nmbr[count]
            count = count + 2
            next
        elif count >= 2:
            if val == "+":
                res = res + nmbr[count]
            elif val == "-":
                res = res - nmbr[count]
            elif val == "*":
                res = res * nmbr[count]
            elif val == "/":
                res = res * nmbr[count]
            count = count + 1

str_nmbr = []

for num in nmbr:
    str_nmbr = str_nmbr + [str(num)]

for op in range(len(opr)):
    if op == 0:
        str_nmbr.insert((op+1), opr[op])
    else:
        str_nmbr.insert((op+2), opr[op])


print(" ".join(str_nmbr), "=", res)
