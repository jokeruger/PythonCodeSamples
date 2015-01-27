#Created by Joe Kruger
#gold ~1410 / troy oz, 19.3 g/cc = 10.16832739419022 troy oz / inch3
#silver ~35 / troy oz, 10.49 g/cc = 5.526723024096136 troy oz / inch3
#copper $4.02 / lb, 8.94g/cc = 0.3229779904807482 lbs / inch3
#aluminum $1 / lb, 2.7 g/cc = 0.097543688400226 lbs / inch3

goldPrice = input("Enter the price (USD) of one troy ounce of gold: ")
goldPrice = float(goldPrice)
silverPrice = input("Enter the price (USD) of one troy ounce of silver: ")
silverPrice = float(silverPrice)
copperPrice = input("Enter the price (USD) of one pound of copper: ")
copperPrice = float(copperPrice)
aluminumPrice = input("Enter the price (USD) of one pound of aluminum: ")
aluminumPrice = float(aluminumPrice)
total = input("Total value of metal desired ($): ")
total = float(total)

goldDensity = 10.16832739419022 #troy oz / cubic inches
silverDensity = 5.526723024096136 #troy oz / cubic inches
copperDensity = 0.3229779904807482 # pounds / cubic inches
aluminumDensity = 0.097543688400226 # pounds / cubic inches

#calculate the mass from the value wanted
goldMass = total/goldPrice
silverMass = total/silverPrice
copperMass = total/copperPrice
aluminumMass = total/aluminumPrice

#calculate volume from mass
goldVol = goldMass/goldDensity
silverVol = silverMass/silverDensity
copperVol = copperMass/copperDensity
aluminumVol = aluminumMass/aluminumDensity

#calculate cube side length from volume
import math
goldLength = math.pow(goldVol,1.0/3)
silverLength = math.pow(silverVol,1.0/3)
copperLength = math.pow(copperVol,1.0/3)
aluminumLength = math.pow(aluminumVol,1.0/3)

print()
print("Metal     Value       $%.2f" % (total))
print("-----     -----       -----------")

#checks length for necessity of using feet
if goldLength>=12:
    goldFeet=int(goldLength)/12
    goldInches=goldLength%12
    print("Gold      $%-10.2f A cube %d ft, %.2f inches to a side" % (goldPrice, goldFeet, goldInches))
else: print("Gold      $%-10.2f A cube %.2f inches to a side" % (goldPrice, goldLength))

if silverLength>=12:
    silverFeet=int(silverLength)/12
    silverInches=silverLength%12
    print("Silver    $%-10.2f A cube %d ft, %.2f inches to a side" % (silverPrice, silverFeet, silverInches))
else: print("Silver    $%-10.2f A cube %.2f inches to a side" % (silverPrice, silverLength))

if copperLength>=12:
    copperFeet=int(copperLength)/12
    copperInches=copperLength%12
    print("Copper    $%-10.2f A cube %d ft, %.2f inches to a side" % (copperPrice, copperFeet, copperInches))
else: print("Copper    $%-10.2f A cube %.2f inches to a side" % (copperPrice, copperLength))

if aluminumLength>=12:
    aluminumFeet=int(aluminumLength)/12
    aluminumInches=aluminumLength%12
    print("Aluminum  $%-10.2f A cube %d ft, %.2f inches to a side" % (aluminumPrice, aluminumFeet, aluminumInches))
else: print("Aluminum  $%-10.2f A cube %.2f inches to a side" % (aluminumPrice, aluminumLength))
