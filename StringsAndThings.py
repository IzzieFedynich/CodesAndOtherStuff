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
    # ljust         aStr.ljust(w)       the w is the width and it returns the string left
    # rjust         aStr.rjust(w)       the w is the width and it returns the string right
    # upper         aStr.upper()        this string returns the string and makes the all the characters uppercased
    # lower         aStr.lower()        this string returns the string and makes the all the characters lowercased
    # index         aStr.index(item)    this returns the lowest index in that list
    # rindex        aStr.rindex(item)   this returns the last index where str is found
    # find          aStr.find(item)     this can tell you if string occurs in a substring or in a string
    # rfind         aStr.rfind(item)    returns the last index where str is found or -1
    # replace       aStr.replace(old, new)  this can replace old words or phrases with new words or phrases

    # Be sure to include multiple examples of all of them in use

str = "this is string example....wow!!!"
print("str.center(40, 'a') : ", str.center(40, 'a'))

str = "this is string example....wow!!!";
print(str.ljust(50, '0'))

str = "this is string example....wow!!!";
print(str.rjust(50, '0'))

str = "this is string example....wow!!!";
print("str.capitalize() : ", str.upper())

aList = [123, 'xyz', 'zara', 'abc'];
print("Index for xyz : ", aList.index('xyz'))
print("Index for zara : ", aList.index('zara'))

str1 = "this is string example....wow!!!";
str2 = "is";

print(str1.rindex(str2))
print(str1.index(str2))

str1 = "this is string example....wow!!!";
str2 = "exam";

print(str1.find(str2))
print(str1.find(str2, 10))
print(str1.find(str2, 40))

str1 = "this is really a string example....wow!!!";
str2 = "is";

print(str1.rfind(str2))
print(str1.rfind(str2, 0, 10))
print(str1.rfind(str2, 10, 0))

print(str1.find(str2))
print(str1.find(str2, 0, 10))
print(str1.find(str2, 10, 0))

str = ("I just wanted to say hi")
print(str.replace("hi", "bye"))

# Character Functions

print(ord('B'))
# Wil give you the character like the number

print(chr(97 + 13))
# Will give you the ord according to the number you gave it
# A=65 a=97

# print(str(12548))
# Gives you the string 12548

# testing functions from mapper.py

from mapper import *

print(letterToIndex('P'))
print(indexToLetter(10))

# this_is_a_secret_message_that_i_want_to_transmit
#   you have to break the message up into 2 parts/ find the middle
#       you then want to add underscores as spaces
#           you want to delete a letter of each word
#

# How to decrypt
#   Find the middle
#       find out which letter was missing
# hsi__ertmsaeta__att_rnmtti_sasce_esg_htiwn_otasi

from Crypto import *

print(scramble2Encrypt("GOOD MORNING LADIES AND GENTLEMEN"))

print(scramble2Decrypt("ODMRIGLDE N ETEEGO ONN AISADGNLMN"))


# writie a stripSpace(text) function here

print("Happy Birthday!")
print("Happy Birthday!". replace(" ", ""))

# write a ceasarEncrypt(plainText, shift)
# write a caesarDecrypt(cipherText, shift)

