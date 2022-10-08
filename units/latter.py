import units.sonar as sonar
import units.settings as settings

class LatterCounter:
    def __init__(self): # init  cointer
        self.__counter = 0
        
    def getCounter(self): #return num of letter on box
        return self.__counter
    
    def increaseCounter(self): #up counter on the box
        self.__counter += 1
        
    def clearCounter(self):
        self.__counter = 0

class LatterDetector:
    def __init__(self):
        self.__prevDist = 0
        self.__letterCounter = LatterCounter() 
        
    def getLatterCounter(self):
        return self.__letterCounter
        
    def latterInserted(self, dist):
        latterSettings = settings.height["latter"] #get seting  min and max disdancer
        return latterSettings["min"] <= dist < latterSettings["max"] # if the distance between min to max than into letter in box mail
        
    def detect(self):
        dist = sonar.readDist() #get distance
        print(dist)
        detected = self.latterInserted(dist) and not self.latterInserted(self.__prevDist) # get there was inserted 
        if detected:
            self.__letterCounter.increaseCounter() #counter up
        self.__prevDist = dist #now dis it is a prevDist on the next distance
        return detected #return the distance
