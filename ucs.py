import string
import random
import sys
import time
import os

class Person:
    def __init__(self, name, parent, summedComfortVal):
        self.name = name
        self.parent = parent
        self.summedComfortVal = summedComfortVal

# returns the possible children for a particular person given the pairComfort matrix
def getChildren(pairComfort, currentPerson):
    children = []
    for [m, n, c] in pairComfort:
        if m == currentPerson.name:
            children.append(
                Person(n, currentPerson.name, currentPerson.summedComfortVal + c)
            )
        elif n == currentPerson.name:
            children.append(
                Person(m, currentPerson.name, currentPerson.summedComfortVal + c)
            )
    return children

# returns the comfort value of a pairing based on the pairComfort matrix
def getComfortValue(pairComfort, name0, name1):
    for [m, n, c] in pairComfort:
        if [name0, name1] == [m, n] or [name1, name0] == [m, n]:
            return c

# returns a list of all unique persons based on pairComfort
def getPersons(pairComfort):
    persons = []
    for [name0, name1, c] in pairComfort:
        if name0 not in persons:
            persons.append(name0)
        elif name1 not in persons:
            persons.append(name1)
        else:
            continue

    return persons

# returns a list of the best seatingArrangements and their respective overallComfortValue
# calls ucs function for each unique person in the list of persons to be seated
def findSeatingArrangements(pairComfort):
    possibleSeating = []
    bestSeating = []
    persons = getPersons(pairComfort)

    for personName in persons:
        seatedNames, overallComfortValue = ucs(pairComfort, personName, len(persons))
        possibleSeating.append([seatedNames, overallComfortValue])

    possibleSeating.sort(key=lambda x: x[1], reverse=True)

    for [a, b] in possibleSeating:
        if possibleSeating[0][1] == b:
            bestSeating.append([a, b])

    actions = (len(possibleSeating) - 1) * len(possibleSeating)

    return bestSeating, actions

# returns a matrix of randomised comfortValues for a set of persons based on the number of persons desired
def getOneWayComfortMatrix(numOfPersons):
    oneWayPairComforts = []
    personNames = string.ascii_letters
    for i in range(numOfPersons):
        for j in range(numOfPersons):
            oneWayPair = []
            oneWayPair.append(personNames[i])
            if j == i:
                continue
            oneWayPair.append(personNames[j])
            oneWayPair.append(random.randint(-5, 5))
            oneWayPairComforts.append(oneWayPair)

    return oneWayPairComforts

# returns two way comfort values based on a one way pair comfort matrix
def getPairComforts(oneWayPairComforts):
    pairComforts = []
    availableComparisons = oneWayPairComforts[:]
    for [a, b, c] in oneWayPairComforts:
        for [x, y, z] in availableComparisons:
            if a == y and b == x:
                pairComfort = [a, b, c + z]
                pairComforts.append(pairComfort)
                availableComparisons.remove([a, b, c])
                availableComparisons.remove([x, y, z])
                break
    
    return pairComforts

# formats seating arrangments into a more easily readable string
def formatArrangements(seatingArrangments):
    formattedSeatingArrangments = []
    for [arrangement, overallComfortValue] in seatingArrangments:
        formattedArrangement = ' -> '.join(arrangement)
        formattedSeatingArrangments.append([formattedArrangement, overallComfortValue])

    return formattedSeatingArrangments

# formats one way pair comforts into a more easily readable string
def formatPairComforts(oneWayPairComforts):
    formattedOneWayPairComforts = []
    for [a, b, c] in oneWayPairComforts:
        formattedPairing = ' -> '.join([a, b])
        formattedOneWayPairComforts.append([formattedPairing, c])
    
    return formattedOneWayPairComforts

# UCS algorithm
# no specific goal state
# the goal is to choose the highest comfort value at each expansion
# and seat all persons
# prioritises highest cost/comfort value, not lowest
def ucs(pairComfort, initialPerson, numOfPersons):
    frontier = []
    seated = []
    frontier.append(Person(initialPerson, None, 0))

    while True:
        if len(seated) == numOfPersons:
            break
        frontier.sort(key=lambda x: x.summedComfortVal, reverse=True)

        children = getChildren(pairComfort, frontier[0])

        seated.append(frontier[0])
        frontier = []

        for child in children:
            # does not consider persons who have already been seated
            if child.name in [s.name for s in seated]:
                continue
            else:
                frontier.append(child)

    overallComfortValue = seated[-1].summedComfortVal + getComfortValue(
        pairComfort, initialPerson, seated[-1].name
    )

    seatedNames = [x.name for x in seated]

    return seatedNames, overallComfortValue

if __name__ == "__main__":
    # user input loop
    # verifies if input is valid
    while True:
        print("Please enter the number of persons to be seated. Minimum number of persons is 4 and maximum number of persons is 52.")
        print("Type 'exit' to quit.\n")
        i = input()
        try:
            if i == 'exit':
                sys.exit(0)
            numOfPersons = int(i)
            if numOfPersons > 52 or numOfPersons < 4:
                print('Minimum number of persons is 4 and maximum number of persons is 52.\n')
                continue
            break
        except ValueError:
            print('\nYou did not enter a valid integer\n')

    # program flow
    oneWayPairComforts = getOneWayComfortMatrix(numOfPersons)
    formattedOneWayPairComforts = formatPairComforts(oneWayPairComforts)
    pairComforts = getPairComforts(oneWayPairComforts)
    formattedTwoWayPairComforts = formatPairComforts(pairComforts)
    startTimeMs = time.time()*1000 # used to determine time taken
    bestSeatings, actions = findSeatingArrangements(pairComforts)
    endTimeMs = time.time()*1000 # used to determine time taken
    duration = round(endTimeMs - startTimeMs, 5)
    formattedBestSeatings = formatArrangements(bestSeatings)

    # formatting for printing to console
    print('One Way Comfort Values:')
    for [pair, value] in formattedOneWayPairComforts:
        print(f'{pair}: {value}')
    print('\nPress any key to show Two Way Pair Comforts')
    input()
    os.system('cls||clear\n')

    print('Two Way Pair Comforts: ')
    for [pair, value] in formattedTwoWayPairComforts:
        print(f'{pair}: {value}')
    print('\nPress any key to show All Optimal Arrangements')
    input()
    os.system('cls||clear')

    print('All Optimal Arrangements:\n')
    for formattedBestSeating in formattedBestSeatings:
        print(f'Optimal Arrangement: {formattedBestSeating[0]}')
        print(f'Overall Comfort Value: {formattedBestSeating[1]}\n')
    print(f'Number of Actions Taken: {actions}')
    print(f'UCS Time Taken: {duration}ms')
    