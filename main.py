import random

POPULATION_SIZE = 20
CITIES_SIZE = 20
population = []
x = []
y = []
tour = []

def generateFirstPopulation():
  # For each position, generates a new possible path
  for _ in range(1, POPULATION_SIZE + 1):
    generatePossiblePath()

def generatePossiblePath():
  path = []
  for _ in range(1, CITIES_SIZE + 1):
    randomNum = random.randint(1, 20) # generates a new number between 1 - 20
    while(numberExistsInPath(path, randomNum)): # while the generated number exists in the list, generates a new one
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
    randomNumber = round(randomNumber,2)
    x.append(randomNumber)

    randomNumber = random.random()
    randomNumber = round(randomNumber,2)
    y.append(randomNumber)

def main():
  generateFirstPopulation()
  generateXandY()
  print(x)
  print(y)
  print(population)

if __name__ == "__main__":
  main()