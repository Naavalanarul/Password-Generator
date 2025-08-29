import random
from os import WCONTINUED

alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j" ,"k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C" ,"D", "E", "F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to pyPassword Generator :)")
req_letters = int(input("Enter the number of letters you want to generate: "))
req_numbers = int(input("Enter the number of digits you want to generate: "))
req_symbols = int(input("Enter the number of symbols you want to generate: "))

password = []
#randomIndex = []
#finalPass = []

for char in range(1, req_letters + 1):
    randomAlpha = random.choice(alphabets)
    password.append(randomAlpha)
for digit in range(1, req_numbers + 1):
    randomNum = random.choice(numbers)
    password.append(randomNum)
for symbol in range(1, req_symbols + 1):
    randomSymbol = random.choice(symbols)
    password.append(randomSymbol)

listPass = [password[i] for i in password]
#########################################################################################################

#for i in range(len(password) + 1):
    #index = 0
    #randomIndex = random.randint(0, len(password) - 1)
    #if password[randomIndex] not in finalPass:
    #    finalPass.append(password[randomIndex])
    #else:
    #    continue

#random.shuffle(password)

#for i in password:
    #print(i,end="")

#for i in range(len(password) - 1):
    #randomIndex.append(random.randint(0, len(password) - 1))
    #password += password[randomIndex[i]]

#for i in password:
    #print(i , end="")

#for choice in range(req_letters + 1):
    #chosenChoice = random.choice(chosenPass)
    #lengthChoice = len(chosenChoice)
    #password += chosenChoice[lengthChoice-1]

######################################################### Own Algorithm Developed ##########################################################

randomIndex = []
finalPass = []
length = req_letters + req_numbers + req_symbols

while length > len(randomIndex) - 1:
    if length != len(randomIndex):
        randomNum = random.randrange(len(password))
        if randomNum not in randomIndex:
            randomIndex.append(randomNum)
        else:
            continue
    if length == len(randomIndex):
        break

for i in range(length):
    finalPass.append(password[randomIndex[i]])

for j in finalPass:
    print(j, end="")

#print(randomIndex)