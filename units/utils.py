class DetectChange:
    def __init__(self): #init of yhe door
        self.__prevValue = None
        
    def detect(self, value): # check if have a detect on the door.
        if value != self.__prevValue:
            self.__prevValue = value
            return True, value
        else:
            return False, None
