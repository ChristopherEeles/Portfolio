####### Excerises 4 ########

#### Revision ####

# Spell


def spell():
    import random
    words = []
    with open("Files/words.txt") as f:
        for word in f:
            words += [word.rstrip("\n")]
    # print(words)
    print("-".join(list(random.choice(words).rstrip("\n\r"))))


spell()

#### Functions ####

# Longest word


def longestWord():
    import random
    words = []
    longestWord = 0
    with open("Files/words.txt") as f:
        for word in f:
            words += [word.rstrip("\n\r")]
    for word in words:
        if longestWord < len(word):
            longestWord = len(word)
        else:
            next
    return longestWord


print(longestWord())

# Standard deviation


def stdDev(sample):
    import math
    sumSquares = []
    mean = sum(sample) / len(sample)
    print(mean)
    for observation in sample:
        sumSquares += [(observation - mean)**2]
    return math.sqrt(sum(sumSquares) / len(sample))


print(stdDev([1, 3, 5, 7, 13, 17]))

# Greatest common denominator


def greatestCD():
    denom1, denom2 = [int(x) for x in input("Enter two integers: ").split()]
    remainder1, remainder2, divisor, factors = 1, 1, 1, []
    while(divisor <= min(denom1, denom2)):
        divisor += 1
        remainder1 = denom1 % divisor
        remainder2 = denom2 % divisor
        if (remainder1 == 0 and remainder2 == 0):
            factors += [divisor]
        else:
            next
    return str(max(factors))


print(greatestCD())

# Euclids Algorithm:


def GCD(denominators):
    if denom2 == 0:
        return denom1
    else:
        return GCD(denom2, denom1 % denom2)


print(GCD(12, 9))

#### Advanced: Map and Reduce ####

#### Map ####


def map(f, xs):
    ys = []
    for x in xs:
        ys = ys + [f(x)]
    return ys

# Squares


def squareInt(n):
    return n ** 2


def squareList(ls):
    sqr = map(squareInt, ls)
    return sqr


print(squareList([1, 2, 3, 4, 5]))

# Maps


def map(f, xs):
    ys = []
    for x in xs:
        ys = ys + [f(x)]
    return ys


def operations(n):
    return [n, n**2, n*2, int(n/2), n**3]


def mapList(ls):  # Can I make this more concise?
    inpt, squares, doubles, halves, cubes = [], [], [], [], []
    results = map(operations, ls)
    for i in range(len(results)):
        inpt += [results[i][0]]
        squares += [results[i][1]]
        doubles += [results[i][2]]
        halves += [results[i][3]]
        cubes += [results[i][4]]
    print("Input: " + str(inpt))
    print("Squares: " + str(squares))
    print("Doubles: " + str(doubles))
    print("Halves: " + str(halves))
    print("Cubes: " + str(cubes))


mapList([1, 2, 3, 4, 5])

#### Reduce ####


def reduce(f, xs):
    y = xs[0]
    for i in range(1, len(xs)):
        y = f(y, xs[i])
    return y

# Product


def product(x):
    def multiply(a, b):
        c = a*b
        return c
    return reduce(multiply, x)


# print(product([1, 2, 3, 4, 5, 6]))  # Could just use this to do factorial

# Factorial with product


def factorial(n):
    ls = range(1, n + 1)
    return product(ls)


print(factorial(6))

# Reduce GCD


def greatestCD(ls):  # Without map or product
    divisor = min(ls)
    while(divisor > 0):
        remainders = []
        for value in ls:
            remainders += [value % divisor]
        if sum(remainders) == 0:
            return divisor
        else:
            divisor -= 1


print(greatestCD([12, 18, 24, 36, 42]))
