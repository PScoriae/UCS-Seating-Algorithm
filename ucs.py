import string
import random

class Person:
    def __init__(self, name, parent, summedComfortVal):
        self.name = name
        self.parent = parent
        self.summedComfortVal = summedComfortVal

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

def getCost(pairComfort, name0, name1):
    for [m, n, c] in pairComfort:
        if [name0, name1] == [m, n] or [name1, name0] == [m, n]:
            return c

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

    return bestSeating

def getOneWayComfortMatrix(numOfPersons):
    oneWayPairComforts = []
    personNames = string.ascii_uppercase
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

def getPairComforts(numOfPersons):
    oneWayPairComforts = getOneWayComfortMatrix(numOfPersons)
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
            if child.name in [s.name for s in seated]:
                continue
            else:
                frontier.append(child)

        # print("Seated:", [e.name for e in seated])
        # print("Frontier:", [f.name for f in frontier])
        # print("Children:", [c.name for c in children])
        # print("")

    overallComfortValue = seated[-1].summedComfortVal + getCost(
        pairComfort, initialPerson, seated[-1].name
    )

    seatedNames = [x.name for x in seated]

    return seatedNames, overallComfortValue

if __name__ == "__main__":
    pairComforts = getPairComforts(5)
    print(pairComforts)
    print()
    bestSeating = findSeatingArrangements(pairComforts)

    print(f'Optimal Arrangement(s): {bestSeating}')