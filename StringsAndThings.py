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
