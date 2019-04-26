import random
import copy
import math

POPULATION_SIZE = 20
CITIES_SIZE = 20
population = []
x = []
y = []
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
        randomNum = random.randint(0, 20)
        randonPos = random.randint(0, 20)
        matrix[i][randonPos] = randomNum

# iterate through each line and swap randomly two values


def permute(matrix):
    for i in range(0, len(matrix)):
        firstRandom = random.randint(0, 20)
        secondRandom = random.randint(0, 20)
        backup = matrix[i][firstRandom]
        matrix[i][firstRandom] = matrix[i][secondRandom]
        matrix[i][secondRandom] = backup

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
    for i in range(len(population)):
        for j in range(len(population[i])):
            firstPos = 19 if getTour()[i][j] == 20 else getTour()[i][j]
            secondPos = 19 if getTour()[i][j+1] == 20 else getTour()[i][j+1]
            distances[i] += dCidade[firstPos][secondPos]
    dict_dist = { i : distances[i] for i in range(0, len(distances) ) }
    distances = dict_dist
    sorted_x = sorted(distances.items(), key=lambda kv: kv[1])
    print(sorted_x)

# Generate the identity matrix (dCidade)
def fitnessFunction():
    for i in range(len(population)):
        for j in range(len(population[i])):
            dCidade[i][j] = math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
    calculateDistances()


def main():
    # runs only once
    generateFirstPopulation()
    generateXandY()

    # runs in a loop 0 - 9999
    fitnessFunction()


if __name__ == "__main__":
    main()
