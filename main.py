import random
import copy
import math

POPULATION_SIZE = 20
CITIES_SIZE = 20
population = []
x = []
y = []
parentsOne = None
parentsTwo = None
dCidade = [[0 for x in range(POPULATION_SIZE)] for y in range(POPULATION_SIZE)]
distances = [0 for x in range(POPULATION_SIZE)]


def generateFirstPopulation():
    # For each position, generates a new possible path
    for _ in range(1, POPULATION_SIZE + 1):
        generatePossiblePath()


def generatePossiblePath():
    path = []
    for _ in range(1, CITIES_SIZE + 1):
        # generates a new number between 1 - 20
        randomNum = random.randint(1, 20)
        # while the generated number exists in the list, generates a new one
        while(numberExistsInPath(path, randomNum)):
            randomNum = random.randint(1, 20)
        path.append(randomNum)
    population.append(path)


def numberExistsInPath(path, number):
    for i in path:
        if i == number:
            return True
    return False


def generateXandY():
    for _ in range(CITIES_SIZE):
        randomNumber = random.random()
        randomNumber = round(randomNumber, 2)
        x.append(randomNumber)

        randomNumber = random.random()
        randomNumber = round(randomNumber, 2)
        y.append(randomNumber)

# mutate a random's position value
def mutate(matrix):
    for i in range(0, len(matrix)):
        ranNum = random.randint(1, 100)
        if ranNum >= 1 and ranNum <= 5:
            indexOne = random.randint(0, 9)
            indexTwo = random.randint(0, 9)
            auxOne = matrix[i][indexOne]
            auxTwo = matrix[i][indexTwo]
            matrix[i][indexOne] = auxTwo
            matrix[i][indexTwo] = auxOne

# Returns the updated tour matrix
def getTour():
    tour = copy.deepcopy(population)

    for ways in tour:
        first = ways[0]
        ways.append(first)
    return tour

# Generates an array with the sum of each way
def calculateDistances():
    global distances
    distances = [0 for x in range(POPULATION_SIZE)]
    for i in range(len(population)):
        for j in range(len(population[i])):
            firstPos = 19 if getTour()[i][j] == 20 else getTour()[i][j]
            secondPos = 19 if getTour()[i][j+1] == 20 else getTour()[i][j+1]
            distances[i] += dCidade[firstPos][secondPos]
    dict_dist = { i : distances[i] for i in range(0, len(distances) ) }
    distances = copy.deepcopy(dict_dist)
    return sorted(distances.items(), key=lambda kv: kv[1])

# Generate the identity matrix (dCidade)
def fitnessFunction():
    for i in range(len(population)):
        for j in range(len(population[i])):
            dCidade[i][j] = math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
    return calculateDistances()

def rouletteFunction(sorted_x):
    arr = []
    rouletteArr = []
    for i in range(10):
        arr.append(sorted_x[i][0])
    for j in range(len(arr)):
        for _ in range(10 - j):
            rouletteArr.append(arr[j])
    global parentsOne
    global parentsTwo
    parentsOne = createParents(rouletteArr)
    parentsTwo = createParents(rouletteArr)

def createParents(rouletteArr):
    parentArr = []
    for _ in range(5):
        parentArr.append(rouletteArr[random.randint(0, 54)])
    return parentArr

def hasDuplicity(auxArray, usedIndexes):
    for i in range(len(auxArray)):
        for j in range(i, len(auxArray)):
            if i != j and auxArray[i] == auxArray[j]:
                if i in usedIndexes:
                    return j
                else:
                    return i
    return -1

def doCycle(sorted_x):
    global population
    children = []

    # percorrer ate 5
    for i in range(5):
        parentOneAux = parentsOne[i]
        parentTwoAux = parentsTwo[i]
        usedIndexes = []
    
        randomIndexInsideCromossomus = random.randint(0, POPULATION_SIZE - 1)

        usedIndexes.append(randomIndexInsideCromossomus)

        childOne = copy.deepcopy(population[parentOneAux])
        childTwo = copy.deepcopy(population[parentTwoAux])

        valAuxOne = childOne[randomIndexInsideCromossomus]
        valAuxTwo = childTwo[randomIndexInsideCromossomus]

        childOne[randomIndexInsideCromossomus] = valAuxTwo
        childTwo[randomIndexInsideCromossomus] = valAuxOne

        while(hasDuplicity(childOne, usedIndexes) != -1):
            newIndex = hasDuplicity(childOne, usedIndexes)
            usedIndexes.append(newIndex)

            valAuxOne = childOne[newIndex]
            valAuxTwo = childTwo[newIndex]

            childOne[newIndex] = valAuxTwo
            childTwo[newIndex] = valAuxOne

        # apos gerar os filhos, ordena a populacao, e adiciona os filhos
        # updates the population array

        children.append(childOne)
        children.append(childTwo)
    
    #for i in population:
     #   print(i)

    mutate(children)
    for i in range(10):
        population[i] = copy.deepcopy(population[sorted_x[i][0]])

    # Ajustar a populacao
    for j in range(10, POPULATION_SIZE):
        population[j] = copy.deepcopy(children[j - 10])

def main():
    # runs only once
    generateFirstPopulation()
    generateXandY()

    # runs in a loop 0 - 9999
    for i in range(10):
        sorted_x = fitnessFunction()
        rouletteFunction(sorted_x)
        doCycle(sorted_x)
        #print(i)

    print(sorted_x)
    for i in population:
        print(i)

if __name__ == "__main__":
    main()
