file = open("input.txt")

wordList = list()
totalWords = 0
borrowedWords = 0
quotedWords = 0
numBorrowedSections = 0
inBorrowed = False
inQuoted = False

# Puts all words (seperated by spaces) into a list.
for line in file:
    wordList = wordList + line.split()

# For every word in the document, check if it is a marker.
# If it's not, then increment the appropriate counter by 1.
for word in wordList:
    if word.rfind('"') != None:
        inQuoted = not inQuoted
    if word == "{":
        inBorrowed = True
    elif word == "}":
        inBorrowed = False
        numBorrowedSections += 1
    else:
        totalWords += 1
        if inBorrowed == True:
            borrowedWords += 1
            if inQuoted == True:
                quotedWords += 1

# Display the results.
print("Using '{' and '}' as markers.")
print("Number of words borrowed: " + str(borrowedWords))
print("Number of words in total: " + str(totalWords))
print("Percentage borrowed (rounded to 1/1000s):  " + str(round(borrowedWords/totalWords*100,3)) + "%")
print("For reference, there were " + str(numBorrowedSections) + " sections containing borrowed text")
print("There were " + str(quotedWords) + " words in quotes.")
input()
