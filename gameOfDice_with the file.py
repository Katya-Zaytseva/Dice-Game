#! The program for rolling the dice

#importing random function to generate the rolls of the dice
import random

#importing numpy function to change numerical array to string format
import numpy

#removing the file, if it exists
import os.path
file_exists = os.path.exists("numberRolls.txt")

if file_exists == True:
    import os
    os.remove("numberRolls.txt")

#Welcoming a user and enquiring about rolling of a dice
print("Welcome to the Dice-Rolling program!")
roll = input("Would you like to roll the dice? ")

#creating an array to story rolls of the dice
storageOfDiceRolls = []
i = 0

#function to determine the numbers on the dice 
def gameOfDice(number, storage):
    while number > 0:
        numberOnDice = random.randint(1,6)
        storage.append(numberOnDice)
        number = number - 1
    return number

#function to calculate sum of all the rolls and average of the rolls
def operationsOfRolls():
    sum=0
    for i in storageOfDiceRolls:
        sum = sum + i
    #print ("The sum of all dice rolls are", sum)
    ave = sum/len(storageOfDiceRolls)
    #print("Average number of rolled dice number", round(ave,2))
#changing numerical array into the list
    # storage = numpy.array(storageOfDiceRolls)
    # content = str(storage)
#opening the file and appending the content
    sumMain = str(sum)
    aveMain = str(ave)
    with open("numberRolls.txt", "a") as file:
        file.write('The sum of the rolls ')
        file.write(sumMain)
        file.write('\n')
        file.write('Average number ')
        file.write(aveMain)
        file.write('\n')
        file.write('\n')
        file.close()
    return 0
    
#main program
while roll == "yes" or roll == "Yes" or roll == "YES":
    numberOfRolls = int(input("Enter how many times do you want to roll the dice? "))
#calling for the main function to throw the dice
    gameOfDice(numberOfRolls, storageOfDiceRolls)
#changing numerical array into the list
    storage = numpy.array(storageOfDiceRolls)
    content = str(storage)
#opening the file and appending the content
    with open("numberRolls.txt", "a") as file:
        file.write("This is your game number ")
        i +=1
        numberOfGames=str(i)
        file.write (numberOfGames)
        file.write('\n')
        file.write(content)
        file.write('\n')
        file.close()
#returning number of rolls
    numberOfRolls=operationsOfRolls()

#Asking the user if they would like to roll the dice again
    if numberOfRolls == 0:
        roll = input("Would you like to roll the dice again? ") 
        storageOfDiceRolls.clear()

print("_____READING FROM THE FILE_____")
file = open("numberRolls.txt", "r")
print(file.read())
file.close()
print ("Thank you for the game!")        