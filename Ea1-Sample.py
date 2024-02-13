#Rhys Johnsen Exploration Activity 1
import numpy as np

#Decides starting ages
ages = np.random.randint(2, 6, (10,10))

#Decides starting weights
weights = np.random.randint(1250, 1750, (10,10)).astype(float)

#Sets up the sickness array
sick = np.zeros((10, 10))

#Decides starting production
production = np.random.randint(175, 225, (10,10)).astype(float)

#Decides generally how production will grow/shrink. The numbers below were chosen to be small enough changes to keep things from getting too exponential
ptrends = np.random.rand(10, 10)
ptrends = np.multiply(ptrends, 0.015625) #number is 1/2^6
ptrends = np.add(ptrends, 0.9921875) #number is 1 - 1/2^7

#Passes a week. Will decide new productions, weights, production trends, sickness, and will increase the cattle's age.
def week():
    global production
    global ptrends
    global ages
    global weights
    sickness()
    #makes new weekly production, decides generally how it will change next week
    production = np.multiply(production, ptrends)
    trendsChange = np.random.rand(10, 10)
    trendsChange = np.multiply(trendsChange, 0.05)
    trendsChange = np.add(trendsChange, 0.975)
    #keeps production from getting exponentially larger/smaller
    lowr, lowc = np.where(production < 135)
    trendsChange[lowr, lowc] += 0.9
    highr, highc = np.where(production > 250)
    trendsChange[highr, highc] -= 0.05
    #lowers production when sick
    sickr, sickc = np.where(sick > 0)
    trendsChange[sickr, sickc] -= 0.4
    #changes weight
    changeWeights = np.random.randint(95, 106, (10, 10)).astype(float)
    changeWeights = np.divide(changeWeights, 100)
    weights = np.multiply(weights, changeWeights)
    lowr, lowc = np.where(weights < 1150)
    weights[lowr, lowc] *= 1.05
    highr, highc = np.where(weights > 1750)
    weights[highr, highc] *= 0.95
    #lowers weight when sick
    weights[sickr, sickc] *= 0.95

    ptrends = np.multiply(ptrends, trendsChange)
    ages = np.add(ages, 0.02)
    doAlerts()

#Makes cows sick
def sickness():
    global sick
    makeSick = np.random.rand(10, 10)
    chosenr, chosenc = np.where(makeSick > 0.995) #Every cow has a .5% chance of getting sick every week.
    sick[chosenr, chosenc] = 1

#Cures a cow of the user's choice
def doCure():
    global sick
    toCure = int(input("Which cow would you like to cure? "))
    toCure -= 1
    toCurer, toCurec = np.unravel_index(toCure, production.shape)
    if(sick[toCurer][toCurec] > 0):
        print("This cow was sick")
        sick[toCurer][toCurec] = 0
    else:
        print("This cow was not sick")

#Alerts the user if anything happened that week.
def doAlerts():
    isFine = True

    aged = np.flatnonzero(ages > 6)
    aged = np.add(aged, 1)
    lowProd = np.flatnonzero(production < 150)
    lowProd = np.add(lowProd, 1)
    lowWeight = np.flatnonzero(weights < 1150)
    lowWeight = np.add(lowWeight, 1)
    if(aged.size > 0):
        isFine = False
        print("The following cow(s) have gotten too old:")
        print(aged)
    if(lowProd.size > 0):
        isFine = False
        print("The following cow(s) have produced too little:")
        print(lowProd)
    if(lowWeight.size > 0):
        isFine = False
        print("The following cow(s) weigh too little:")
        print(lowWeight)
    findSick = np.append(lowProd, lowWeight)
    if(findSick.size > 0):
        #Gets a list of matching elements from two arrays, lowProd and lowWeight, in only four lines total
        afflicted, sickCounts = np.unique(findSick, return_counts = True)
        sickindex = np.where(sickCounts > 1)
        areSick = afflicted[sickindex]
        if(areSick.size > 0):
            print("The following cow(s) are likely sick:")
            print(areSick)
    if(isFine):
        print("All is normal")


running = True

#Input loop
while(running):
    choice = input("Input: ").lower()
    match choice:
        case "next":
            week()
        case "age":
            print("Ages of cattle (in years):")
            print(ages)
        case "prod":
            print("Production of cattle (in litres):")
            print(production)
        case "weight":
            print("Weight of cattle (in lbs):")
            print(weights)
        case "sick":
            print("State of wellness:")
            print(sick)
        case "cure":
            doCure()
        case "end":
            running = False