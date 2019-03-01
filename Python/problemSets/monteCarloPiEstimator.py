######## Exercises 3 ########

#### Revision ####

# Count words in text file

import random


def wc_file(fl):

    lines = 0
    words = 0
    characters = 0

    with open(fl) as f:
        for line in f:
            lines += 1
            # Note: split() turns a string into a list, so using [ ] will make a list of a list and return 1
            words += len(line.split())
            # You cannot split on empty strings in Python, use list instead
            characters += len(list(line))
        print("Lines:", lines, "Words:", words, "Characters:", characters)


wc_file("Files/words.txt")
wc_file("Files/file.txt")

#### Reading Text Files ####

# Print first and last word in file

lines = []
with open("Files\words.txt") as f:
    for line in f:
        lines += [line]
    print(lines[0])
    print(lines[-1])

# Print random word from file

lines = []
with open("Files\words.txt") as f:
    for line in f:
        lines += [line]
    # Syntax is random.choice not random.randchoice
    print(random.choice(lines).rstrip("\n\r"))

# Censor

lines = []
with open("Files\words.txt") as f:
    for line in f:
        lines += [line]

    rand = random.choice(lines)
    ind = lines.index(rand)
    # Syntax is random.choice not random.randchoice
    print("Original:", rand.rstrip("\n\r"))

    for letter in rand:
        if letter in "aeiou":
            lines[ind] = lines[ind].replace(letter, "*")

    # Syntax is random.choice not random.randchoice
    print("Censored:", lines[ind].rstrip("\n\r"))

# First letter


def firstLetter(fl):

    words = []
    with open(fl) as f:
        for word in f:
            words += [word]

    letter = input("Enter a letter: ")

    for word in words:
        letters = list(word)
        if letters[0] == letter:
            print(word, end='')
        else:
            next
    print()


firstLetter("Files\words.txt")

#### Games ####

# High-low


def highLow():
    import random
    print("I have thought of an integer between 0 and 100.")
    number = random.randint(0, 100)
    while(True):
        guess = int(input("Guess: "))
        if guess == number:
            break
        elif guess > number:
            print("Too high.")
        else:
            print("Too low.")

    print("You got it!")


highLow()


def guessWord():
    import random
    words = []
    with open('Files\words.txt') as f:
        for word in f:
            words += [word]

    uncensored = random.choice(words)
    censored = uncensored

    for char in uncensored:  # Python automatically makes uncensored string into list of characters
        if char in "aeiou":
            # You must declare variables outside of loop if you want to use them outside loop
            censored = censored.replace(char, "*")
        else:
            next

    print("Censored: " + censored)

    while(True):
        guess = input("Guess the word: ")
        # This comparison considers newline characters, therefore need to use .rstrip() string method
        if guess.rstrip("\n\r") == uncensored:
            break
        else:
            print("Nope, try again.")
    print("You got it!")


guessWord()

#### Advanced ####

# Hang-man


def hangMan():
    import random
    words = []
    with open("words.txt") as f:
        for word in f:
            words += [word]

    correct = random.choice(words).strip()
    censored = list("*"*(len(correct)))
    guessed = []

    while(True):
        guess = input("Guess a letter: ").rstrip("\n\r")
        guessed += guess
        count = 0
        for char in correct:
            if guess == char:
                censored[count] = censored[count].replace("*", char)
            count += 1
        if ''.join(censored) == correct:
            break
        else:
            print("Guessed: ", guessed, sep='')
            print("Word: " + ''.join(censored))
    print("You won!")


hangMan()

# Pi with Monte Carlo Methods

# a = pi*r^2 for circle, therefore radius 1 reduces to pi
# a = x*y for a square, therefore square of side length 2 a = 2*2 = 4
# P(insideCircle) = a(circle)/a(square) = pi / 4
# Therefore pi = P(insideCircle)*4
# r = x^2 + y^2, therefore 1 = x^2 + y^2


def estimatePi():
    import random
    for i in range(2, 10):
        print("Estimate for", 10**i, "iterations")
        occurences = 0
        for j in range(1, ((10**i)+1)):
            radius = sum([random.uniform(0, 1)**2, random.uniform(0, 1)**2])
            if radius < 1:
                occurences += 1
            else:
                next
        print("Estimated pi is:", (occurences/(10**i))*4)
        check = input(
            'Do you want increase interations by a factor of 10? [y/n]')
        if check == "Y" or check == "y":
            next
        else:
            break
    print("Maximum value reached!")
    exit


estimatePi()

# Barebones


def estimatePiBB():
    import random
    for i in range(2, 10):
        occurences = 0
        for j in range(1, ((10**i)+1)):
            radius = sum([random.uniform(0, 1)**2, random.uniform(0, 1)**2])
            if radius < 1:
                occurences += 1
        print("Estimated pi for", 10**i,
              "iterations is:", (occurences/(10**i))*4)


estimatePiBB()
