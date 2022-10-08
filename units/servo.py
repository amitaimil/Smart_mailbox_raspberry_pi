import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# the servo work 180 angales and we uses offest 90 angels from -90 angels to 90 angals

class Servo:
    def __init__(self, pin, freq): 
        GPIO.setup(pin, GPIO.OUT)
        self.__angle = 0
        self.__servo = GPIO.PWM(pin, freq)
        self.__servo.start(self.__getDutyFromAngle())
        
    def __getDutyFromAngle(self): # the servo work whit duty cycle change, rmote angle to the duty cycle
        return self.__angle * 5 / 90 + 7.5
    
    def setAngle(self, angle):
        self.__angle = angle
        self.__servo.ChangeDutyCycle(self.__getDutyFromAngle())
#         time.sleep(0.5)
