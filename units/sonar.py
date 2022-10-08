from Bluetin_Echo import Echo
import units.settings as settings

sonarPins = settings.pins["sonar"] # get pins ultrasonic
sonar = Echo(trigger_pin = sonarPins["trigger"], echo_pin = sonarPins["echo"], mPerSecond = 343) #init ultraSonic

def readDist():
    return sonar.read(settings.sonar["unit"], settings.sonar["samples"]) #return distance whit avrage on num of sample