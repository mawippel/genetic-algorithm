import random

POPULATION_SIZE = 20
CROMOSSOMES_SIZE = 20
CITIES_SIZE = 20
population = []

def generateFirstPopulation():
  # For each position, generates a new possible path
  for j in range(1, POPULATION_SIZE + 1):
    generatePossiblePath()

def generatePossiblePath():
  path = []
  for x in range(1, CITIES_SIZE + 1):
    randomNum = random.randint(1, 21) # generates a new number between 1 - 20
    while(numberExistsInPath(path, randomNum)): # while the generated number exists in the list, generates a new one
      randomNum = random.randint(1, 20)
    path.append(randomNum)
  population.append(path)

def numberExistsInPath(path, number):
  for i in path:
    if i == number:
      return True
  return False

if __name__ == "__main__":
  generateFirstPopulation()
  print(population)