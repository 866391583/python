import os
import sys
import sets
import random
import string
import matplotlib.pyplot as plt
from string import *
from math import *
BestTour = []                   # store the best path
CitySet = sets.Set()            # city set
CityList = []                   # city list
PheromoneTrailList = []         # pheromone trail list
PheromoneDeltaTrailList = []    # delta pheromone trail list
CityDistanceList = []           # city distance list
AntList = []                   # ants
cityPosX=[]
cityPosY=[]
cityPosXX=[]
cityPosYY=[]
a2c=[]
class BACA:
    "implement basic ant colony algorithm"
    # following are some essential parameters/attributes for BACA
    def __init__(self, cityCount=51, antCount=51, q=100,
                 alpha=1, beta=5, rou=0.3, nMax=100):
        self.CityCount = cityCount
        self.AntCount = antCount
        self.Q = q
        self.Alpha = alpha
        self.Beta = beta
        self.Rou = rou
        self.Nmax = nMax
        self.Shortest = 10e6
        # set random seed
        random.seed()

        # init global data structure
        for nCity in range(self.CityCount):
            BestTour.append(0)

        for row in range(self.CityCount):
            pheromoneList = []
            pheromoneDeltaList = []
            for col in range(self.CityCount):
                pheromoneList.append(100)               # init pheromone list to const 100
                pheromoneDeltaList.append(0)            # init pheromone delta list to const 0
            PheromoneTrailList.append(pheromoneList)
            PheromoneDeltaTrailList.append(pheromoneDeltaList)

    def ReadCityInfo(self, fileName):
        file = open(fileName)
        #print file.readlines()
        #CityList = []

        for line in file.readlines():
            cityN,cityX,cityY = line.strip('\n').split(' ')

            #print cityN,cityX,cityY
            CitySet.add(atoi(cityN))                # add into city set
            CityList.append((atoi(cityN),atoi(cityX),atoi(cityY)))
            cityPosX.append(atoi(cityX))
            cityPosY.append(atoi(cityY))
        #print cityList
        #print CitySet
        plt.plot(cityPosX,cityPosY,'go')
        plt.show()
        for row in range(self.CityCount):
            distanceList = []
            for col in range(self.CityCount):
                distance = sqrt(pow(CityList[row][1]-CityList[col][1],2)+pow(CityList[row][2]-CityList[col][2],2))
                distanceList.append(distance)
            CityDistanceList.append(distanceList)
        #print CityDistanceList

    def PutAnts(self):
        chooseCity=range(1,52)
        random.shuffle(chooseCity)
        for antNum in range(self.AntCount):
            ant=ANT(chooseCity[antNum])
            AntList.append(ant)
##        """randomly put ants on cities"""
##        for antNum in range(self.AntCount):
##            city = random.randint(1, self.CityCount)
##            ant = ANT(city)
##            AntList.append(ant)
##            #print ant.CurrCity
    def Search(self):
        """search solution space"""
        for iter in range(self.Nmax):
            self.PutAnts()
            for ant in AntList:
                for ttt in range(len(CityList)):
                    ant.MoveToNextCity(self.Alpha, self.Beta)
                ant.UpdatePathLen()
            tmpLen = AntList[0].CurrLen
            tmpTour = AntList[0].TabuCityList
            for ant in AntList[1:]:
                if ant.CurrLen < tmpLen:
                    tmpLen = ant.CurrLen
                    tmpTour = ant.TabuCityList
            if tmpLen < self.Shortest:
                self.Shortest = tmpLen
                BestTour = tmpTour
            print iter,":",self.Shortest,":",BestTour
            if iter==self.Nmax-1:
                for nn in BestTour:
                    cityPosXX.append(cityPosX[nn-1])
                    cityPosYY.append(cityPosY[nn-1])
                cityPosXX.append(cityPosXX[0])
                cityPosYY.append(cityPosYY[0])
                plt.plot(cityPosXX,cityPosYY,'g-')
                plt.show()




            self.UpdatePheromoneTrail()
##            for ant in AntList:
##                city = ant.TabuCityList[-1]
##                ant.ClearTabu()
##                ant.AddCity(city)
    def UpdatePheromoneTrail(self):
        for ant in AntList:
            for city in ant.TabuCityList[0:-1]:
                idx = ant.TabuCityList.index(city)
                nextCity = ant.TabuCityList[idx+1]
                PheromoneDeltaTrailList[city-1][nextCity-1] = self.Q/ant.CurrLen
                PheromoneDeltaTrailList[nextCity-1][city-1] = self.Q/ant.CurrLen
            lastCity = ant.TabuCityList[-1]
            firstCity = ant.TabuCityList[0]
            PheromoneDeltaTrailList[lastCity-1][firstCity-1] = self.Q/ant.CurrLen
            PheromoneDeltaTrailList[firstCity-1][lastCity-1] = self.Q/ant.CurrLen
        for (city1,city1X,city1Y) in CityList:
            for (city2,city2X,city2Y) in CityList:
                PheromoneTrailList[city1-1][city2-1] = ((1-self.Rou)*PheromoneTrailList[city1-1][city2-1] +
                                                    PheromoneDeltaTrailList[city1-1][city2-1])
                PheromoneDeltaTrailList[city1-1][city2-1] = 0

class ANT:
    "implement ant individual"
    def __init__(self, currCity = 0):
        # following are some essential attributes for ant
        self.TabuCitySet = sets.Set()            # tabu city set
        self.TabuCityList = []                   # tabu city list
        self.AllowedCitySet = sets.Set()         # AllowedCitySet = CitySet - TabuCitySet
        self.TransferProbabilityList = []        # transfer probability list
        self.CurrCity = 0                        # city which the ant current locate
        self.CurrLen = 0.0                       # current path len
        self.AddCity(currCity)
        pass
    def SelectNextCity(self, alpha, beta):
        """select next city to move to"""
        #MAXLEN = 1e6
        if len(self.AllowedCitySet) == 0:
            return (0)
        sumProbability = 0.0
        #
        for city in self.AllowedCitySet:
            sumProbability = sumProbability + (pow(PheromoneTrailList[self.CurrCity-1][city-1], alpha)
                                            * pow(1.0/CityDistanceList[self.CurrCity-1][city-1], beta))
        self.TransferProbabilityList = []
        for city in self.AllowedCitySet:
            transferProbability = (pow(PheromoneTrailList[self.CurrCity-1][city-1], alpha)
                                * pow(1.0/CityDistanceList[self.CurrCity-1][city-1], beta))/sumProbability
            self.TransferProbabilityList.append((city, transferProbability))
        # determine next city
        select = 0.0
        for city,cityProb in self.TransferProbabilityList:
            if cityProb > select:
                select = cityProb
        threshold = select * random.random()
        for (cityNum, cityProb) in self.TransferProbabilityList:
            if cityProb >= threshold:
                return (cityNum)
        return (0)
    def MoveToNextCity(self, alpha, beta):
        """move the ant to next city"""
        nextCity = self.SelectNextCity(alpha, beta)
        if nextCity > 0:
            self.AddCity(nextCity)
    def ClearTabu(self):
        """clear tabu list and set"""
        self.TabuCityList = []
        self.TabuCitySet.clear()
        self.AllowedCitySet = CitySet - self.TabuCitySet
    def UpdatePathLen(self):
        """sum up the path length"""
        for city in self.TabuCityList[0:-1]:
            nextCity = self.TabuCityList[self.TabuCityList.index(city)+1]
            self.CurrLen = self.CurrLen + CityDistanceList[city-1][nextCity-1]
        lastCity = self.TabuCityList[-1]
        firstCity = self.TabuCityList[0]
        self.CurrLen = self.CurrLen + CityDistanceList[lastCity-1][firstCity-1]
    def AddCity(self,city):
        """add city to tabu list and set"""
        if city <= 0:
            return
        self.CurrCity = city
        self.TabuCityList.append(city)
        self.TabuCitySet.add(city)
        self.AllowedCitySet = CitySet - self.TabuCitySet
if __name__ == "__main__":
    theBaca = BACA()
    theBaca.ReadCityInfo(r"eil51.tsp")
    theBaca.Search()
    print BestTour
    for nn in BestTour:
        cityPosXX.append(cityPosX[nn-1])
        cityPosYY.append(cityPosY[nn-1])
    plt.plot(cityPosXX,cityPosYY,'go')
    plt.show()
##    os.system("pause")
