# Strings
#   data that falls within "" marks

# Concatenation
#  Put 2 or more strings together

firstName = "Fred"
LastName = "Flintstone"

fullName = firstName + " " + LastName

print(fullName)

# Repetition
#   repetition operator: *

print("Hip" *2 + "Horray!")

def rowYourBoat():
    print("Row, "*3 + ' your boat')
    print("Gently down the stream")
    print("Merrily, "*4)
    print("Life is but a dream")

rowYourBoat()

# Indexing

# Indexing gives us the ability to access any individual thing in a string
#   like to ask a string how long it is

name = "Roy G Biv"
FirstChar = name[0]
print(FirstChar)
middleIndex = len(name) // 2
# len is how you find out the length
print(middleIndex)
print(name[middleIndex])

print(name[-1])

for i in range(len(name)):
    print(name[i])

# Slicing and Dicing
#   slicing operator: :
#    slicing lets us make substrings

print(name[0:3])
print(name[:5])
print(name[6:9])
print(name[6:])
print(name[0:])

for i in range(1, len(name)+1):
    print(name[0:i])

# Searching inside of strings
#True or false questions about string
print("biv" in name)
print("v" not in name)

if "y" in name:
    print("The letter y is in name")
else:
    print("The letter y is not in name")

    # String Methods to investigate:
    # Method        Use Example         Explanation
    # center        aStr.center(w)      Center is just another way to use a string to plug in things like letters or words
    # ljust         aStr.ljust(w)
    # rjust         aStr.rjust(w)
    # upper         aStr.upper()
    # lower         aStr.lower()
    # index         aStr.index(item)
    # rindex        aStr.rindex(item)
    # find          aStr.find(item)
    # rfind         aStr.rfind(item)
    # replace       aStr.replace(old, new)  this can replace old words or phrases with new words or phrases

    # Be sure to include multiple examples of all of them in use

str = ("I just wanted to say hi")
print(str.replace("hi", "bye"))


