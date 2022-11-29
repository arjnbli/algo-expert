# O(n) time | O(1) space
# n is the number of cities
def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    startingCity = 0
    currentFuel = 0
    for i in range(len(distances)):
        if currentFuel < 0:
            startingCity = i
            currentFuel = 0
        currentFuel += ((fuel[i] * mpg - distances[i]) / mpg)
        print(startingCity, currentFuel)
    return startingCity

# O(n) time | O(n) space
# n is the number of cities
def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    minFuelRemaining = 0
    fuelRemaining = 0
    startingCity = 0
    for i in range(1, len(distances)):
        fuelRemaining += (fuel[i - 1] * mpg  - distances[i - 1])/ mpg
        if fuelRemaining < minFuelRemaining:
            minFuelRemaining = fuelRemaining
            startingCity = i
        print(startingCity, fuelRemaining)
    return startingCity
