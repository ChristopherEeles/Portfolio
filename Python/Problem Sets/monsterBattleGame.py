######## Exercises 5 ########

#### Revision ####

# Sherlock - open "holmes.txt" file, read in the lines, select and prints the line and number of characters in the line


def randLineCharCount(fl):  # Reads blank lines
    lines = []
    charCount = 0

    with open(fl) as f:
        for line in f:
            lines += [line.strip("\n\r")]

    import random
    randLine = random.choice(lines)
    print("The line is: ", randLine)
    for char in randLine:
        charCount += 1
    print("There are", charCount, "characters in: ", randLine)


randLineCharCount("Files\holmes.txt")


def randLineCharCountSkip(fl):  # Skips blank lines
    lines = []
    charCount = 0

    with open(fl) as f:
        for line in f:
            # Need to strip or empty lines will contain 1 or 2 charaters ("\n" or "\n\r")
            line = line.strip("\n\r")
            if len(line) == 0:
                next
            else:
                lines += [line]

    import random
    randLine = random.choice(lines)
    print("The line is: ", randLine)
    for char in randLine:
        charCount += 1
    print("There are", charCount, "characters in: ", randLine)


randLineCharCountSkip("Files\holmes.txt")


def randWordCharCountSkip(fl):  # Random word from random line with char count
    lines = []
    words = []
    charCount = 0

    with open(fl) as f:
        for line in f:
            # Need to strip or empty lines will contain 1 or 2 charaters ("\n" or "\n\r")
            line = line.strip("\n\r")
            if len(line) == 0:
                next
            else:
                lines += [line]

    import random
    import string
    randLine = random.choice(lines)
    # print("The line is: ", randLine)
    words += randLine.split()
    randWord = random.choice(words).strip(string.punctuation)
    print("The word is: ", randWord)
    for char in randWord:
        charCount += 1
    print("There are", charCount, "characters in: ", randWord)


randWordCharCountSkip("Files\holmes.txt")

#### Dictionaries ####

# Favorite animal survey


def animalSurvey():
    import string
    animals = {}

    while(True):
        current = input("What is your favourite animal? ").rstrip(
            "\n\r").lower()
        if len(current) == 0:
            break

        if current in animals:
            animals[current] += 1
        else:
            animals[current] = 1

        for animal in animals:
            print(animal, ":", animals[animal])


animalSurvey()

# Histogram of survey results


def animalSurveyHist():
    import string
    animals = {}

    while(True):
        current = input("What is your favourite animal? ").rstrip(
            "\n\r").lower()
        if len(current) == 0:
            break

        if current in animals:
            animals[current] += "#"
        else:
            animals[current] = "#"

        maxLength = len(max(animals))

        for animal in animals:
            dots = maxLength - len(animal)
            print(animal + "."*dots + "|" + animals[animal])


animalSurveyHist()

# English to Cockney slang


def toCockney(str):  # Fix with regex to retain punctuation
    import string
    slang = {}

    with open("cockney.csv") as f:  # Initialize dictionary from csv
        for line in f:
            a, b = [x for x in line.split(",")]
            slang[a] = b

    words = str.strip("\n\r").split(" ")

    for word in words:
        for key in slang.keys():
            if word.lower().strip(string.punctuation) == key:
                words[words.index(word)] = slang[key].strip("\n\r")

    words[0] = words[0][0].upper() + words[0][1:]
    print(" ".join(words))


# Currently deletes all punctuation
toCockney("Look at my hair. I believe it's better than my wife!")

#### Objects and Classes ####

# Pocket Monsters


class PocketMonster:
    # Constructor
    def __init__(self, name, hp, attack, defense):  # Self refers to current object
        self.items = {"name": name, "hp": hp,
                      "attack": attack, "defense": defense}
        self.alive = True

    # Descriptor
    def describe(self):
        return self.items["name"] + ' (HP=' + str(self.items["hp"]) + ')'

    # Getters
    def getName(self):
        return self.items["name"]

    def getHp(self):
        return self.items["hp"]

    def getAttack(self):
        return self.items["attack"]

    def getDefense(self):
        return self.items["defense"]

    def getAlive(self):
        return self.items["alive"]

    def getAll(self):
        self.getName()
        self.getHp()
        self.getAttack()
        self.getDefense()

    # Setters
    def setName(self, name):
        self.items["name"] = name

    def setHp(self, hp):
        self.items["hp"] = hp

    def setAttack(self, attack):
        self.items["attack"] = attack

    def setDefense(self, defense):
        self.items["defense"] = defense

    # Interfaces

    def Attack(self):
        import random
        return random.randint(0, self.items["attack"])

    def Defend(self):
        import random
        return random.randint(0, self.items["defense"])


class MonsterBattle:
    def __init__(self, mon1, mon2):
        i = 0
        while (True):
            i += 1
            print(mon1.describe(), "vs.", mon2.describe())
            if i % 2 != 0:
                atk = mon1.Attack()
                df = mon2.Defend()
                if atk > df:
                    mon2.items["hp"] -= atk
                    print(mon1.items["name"] +
                          "'s attack is effective for", atk, "damage!")
                else:
                    print("It's not very effective...")
            else:
                atk = mon2.Attack()
                df = mon1.Defend()
                if atk > df:
                    mon1.items["hp"] -= atk
                    print(mon2.items["name"] +
                          "'s attack is effective for", atk, "damage!")
                else:
                    print("It's not very effective...")
            if (mon2.items["hp"] <= 0):
                print(mon2.items["name"], "has died!")
                print(mon1.items["name"], "is victorious.")
                break
            elif (mon1.items["hp"] <= 0):
                print(mon1.items["name"], "has died!")
                print("You lose the battle to", mon2.items["name"] + "...\n")
                break


# Initialize monsters
pika = PocketMonster("Pikachu", 10, 10, 5)
mudkip = PocketMonster("Mudkip", 9, 12, 4)

# Start battle
battle = MonsterBattle(pika, mudkip)

#### Advanced: Word Clouds ####

# Counts number of times words appear in 'holmes.txt'

# Count from word


def countWords():
    import string
    countOfWords = {}
    fileWords = []
    with open("holmes.txt") as f:
        for line in f:
            fileWords += line.split()
        for i in range(len(fileWords)):
            fileWords[i] = fileWords[i].strip(string.punctuation)
        uniqueFileWords = set(fileWords)
        for wrd in uniqueFileWords:
            countOfWords[wrd] = 0
        for wrd in fileWords:
            countOfWords[wrd] += 1

    while(True):
        word = input("Select a word: ").strip("\n\r")
        if word == '':
            break
        elif word in countOfWords:
            print(countOfWords[word])
        else:
            print("Word not in 'holmes.txt'")


countWords()

# Word from count


def wordFromCount():
    import string
    countOfWords = {}
    fileWords = []
    with open("holmes.txt") as f:
        for line in f:
            fileWords += line.split()
        for i in range(len(fileWords)):
            fileWords[i] = fileWords[i].lower().strip(string.punctuation)
        uniqueFileWords = set(fileWords)
        for wrd in uniqueFileWords:
            countOfWords[wrd] = 0
        for wrd in fileWords:
            countOfWords[wrd] += 1

    while(True):
        words = []
        count = int(input("Select a count: ").strip("\n\r"))
        if count == None:
            break
        for word in countOfWords.keys():
            if countOfWords[word] == count:
                words += [word]
            else:
                next
        print(", ".join(words))


wordFromCount()

# All word for each count


def wordsForCount():
    import string
    countOfWords = {}
    fileWords = []
    with open("holmes.txt") as f:
        for line in f:
            fileWords += line.split()
        for i in range(len(fileWords)):
            fileWords[i] = fileWords[i].lower().strip(string.punctuation)
        uniqueFileWords = set(fileWords)
        for wrd in uniqueFileWords:
            countOfWords[wrd] = 0
        for wrd in fileWords:
            countOfWords[wrd] += 1

        for count in reversed(sorted(set(countOfWords.values()))):
            words = []
            for word in countOfWords.keys():
                if countOfWords[word] == count:
                    words += [word]
                else:
                    next
            print(str(count) + " : " + ", ".join(words) + "\n")


wordsForCount()

# Excluding words in 'common.txt'


def wordsForCountRestricted():
    import string
    countOfWords = {}
    fileWords = []
    commonWords = []
    with open("common.txt") as fl:
        for line in fl:
            commonWords += [line.strip("\n\r")]
        # print(", ".join(commonWords))

    with open("holmes.txt") as f:
        for line in f:
            fileWords += line.split()
        for i in range(len(fileWords)):
            fileWords[i] = fileWords[i].lower().strip(string.punctuation)
        uniqueFileWords = set(fileWords)
        for wrd in uniqueFileWords:
            if wrd in commonWords:  # Skips words in "common.txt"
                next
            else:
                countOfWords[wrd] = 0
        for wrd in fileWords:
            if wrd in commonWords:  # Skips words in "common.txt"
                next
            else:
                countOfWords[wrd] += 1

        for count in reversed(sorted(set(countOfWords.values()))):
            words = []
            for word in countOfWords.keys():
                if countOfWords[word] == count:
                    words += [word]
                else:
                    next
            print(str(count) + " : " + ", ".join(words) + "\n")


wordsForCountRestricted()

# Word cloud


def topTwentyWords():
    import string
    countOfWords = {}
    fileWords = []
    commonWords = []
    with open("common.txt") as fl:
        for line in fl:
            commonWords += [line.strip("\n\r")]
        # print(", ".join(commonWords))

    with open("holmes.txt") as f:
        for line in f:
            fileWords += line.split()
        for i in range(len(fileWords)):
            fileWords[i] = fileWords[i].lower().strip(string.punctuation)
        uniqueFileWords = set(fileWords)
        for wrd in uniqueFileWords:
            if wrd in commonWords:  # Skips words in "common.txt"
                next
            else:
                countOfWords[wrd] = 0
        for wrd in fileWords:
            if wrd in commonWords:  # Skips words in "common.txt"
                next
            else:
                countOfWords[wrd] += 1
        countDict = {}
        wordCount = 0
        maxWords = 20
        for count in reversed(sorted(set(countOfWords.values()))):
            words = []
            for word in countOfWords.keys():
                if countOfWords[word] == count:
                    words += [word]
                    wordCount += 1
                else:
                    next
                if (wordCount >= maxWords):
                    break
            print(str(count) + " : " + ", ".join(words) + "\n")
            countDict[count] = words
            if (wordCount >= maxWords):
                break

    output = open("wordCloud.html", "w")
    countDict = sorted(countDict)
    for count in countDict.keys():
        for val in countDict[count]:
            output.write('<span style="font-size:' +
                         str(count)+'">'+val+'</span>'+"\n")


topTwentyWords()
