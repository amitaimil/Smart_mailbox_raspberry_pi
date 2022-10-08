from units.servo import Servo
import units.settings as settings

class Door:
    def __init__(self, pin, freq): #init the door
        self.__door = Servo(pin, freq) #object on the servo
        self.unlock()# unlock the door
        
    def isLock(self):
        return self.__locked #return if the door is lock or unlock
        
    def lock(self): # the 0 angelas the door is unlock -true
        self.__door.setAngle(0)
        self.__locked = True
    
    def unlock(self): # the -90 angelas the door is unlock - false
        self.__door.setAngle(-90)
        self.__locked = False