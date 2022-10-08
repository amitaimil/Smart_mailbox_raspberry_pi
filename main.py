import RPi.GPIO as GPIO
from pad4pi import rpi_gpio as RPG
import units.settings as settings
from units.settings import defaultPassword as password
from units.door import Door
from units.lcd import lcd, clearLine, writeLine
from units.utils import DetectChange
from units.latter import LatterCounter, LatterDetector
import time

currentPass = 0

GPIO.setup(settings.pins["door"], GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # init door 1 on ,0/null off
GPIO.setup(settings.pins["buzzer"], GPIO.OUT) # init buzzer pin
buzzer = GPIO.PWM(settings.pins["buzzer"], settings.buzzerFreq) 
buzzer.start(0) # duty cycle=0


#init kaypad ,init 4 buttons 1,2,3,4,the kaypad consist of a combination of rows and columns
keypad = RPG.Keypad(keypad=[[1, 2, 3, 4]], row_pins=settings.pins["keypad"]["rows"], col_pins=settings.pins["keypad"]["cols"])
doorLock = Door(settings.pins["servo"], settings.servoFreq) #init object for the servo
doorDetector = DetectChange() #init object with which we will check if there has been a change in the opening and closing of the door

lcd.clear() # clear lcd 
writeLine(0, '') #write null lcd  because invalid valuse


latterDetector = LatterDetector() # init num of letter in mail box =0 

def keypress(key):
    global password, currentPass
    doorClosed = GPIO.input(settings.pins["door"])
    if doorClosed:
        if currentPass == 0: # if dor is lock and no pasword
            writeLine(1, 'password:     ') # write on lcd on row 1
            lcd.cursor_pos = (1, 10)
        lcd.write_string('*') 
        currentPass = currentPass * 10 + key
        if 1000 <= currentPass < 10000: # the password  contains 4 digit
            if not doorLock.isLock(): # if the door dont lock
                password = currentPass
                time.sleep(.5)
                doorLock.lock()
                lcd.clear()
                writeLine(0, 'Door locked')
                writeLine(1, 'successfully!')
                time.sleep(1.5)
                lcd.clear()
                writeLine(0, 'Number of')
                writeLine(1, ('latters: %i') % latterDetector.getLatterCounter().getCounter())
            else: # the door is lock
                if password == currentPass: # the door is lock and the passowrd is true
                    time.sleep(.5)
                    doorLock.unlock()
                    lcd.clear()
                    writeLine(0, 'Door unlocked')
                    writeLine(1, 'successfully.')
                    time.sleep(1.5)
                    lcd.clear()
                    writeLine(0, 'Take out')
                    writeLine(1, 'the latters')
                else:# the door is lock and the passowrd is not true
                    time.sleep(.5)
                    lcd.clear()
                    writeLine(0, 'Wrong password!')
                    for _ in range(3):
                        buzzer.ChangeDutyCycle(50)
                        time.sleep(1)
                        buzzer.ChangeDutyCycle(0)
                        time.sleep(1)
                        lcd.clear()
                        writeLine(0, 'Number of')
                        writeLine(1, ('latters: %i') % latterDetector.getLatterCounter().getCounter())
                    
            currentPass = 0

def doorChanged(pin):
    global currentPass
    result, doorClosed = doorDetector.detect(GPIO.input(pin))
    if result and not doorClosed: # if the door is open ,rest the counter letter
        latterDetector.getLatterCounter().clearCounter()
    if result and not doorLock.isLock(): # if detect door  and the soor is not lock
        currentPass = 0
        if doorClosed:
            lcd.clear()
            writeLine(0, 'Enter password')
            writeLine(1, 'to lock the door.')
        else:
            lcd.clear()
            writeLine(0, 'Mail box:')
            writeLine(1, 'Close the door.')
            

keypad.registerKeyPressHandler(keypress) #input from keypad
GPIO.add_event_detect(settings.pins["door"], GPIO.BOTH, callback=doorChanged) # event to the pin of door and up to the function doorChanged

doorChanged(settings.pins["door"])

try:
    while True:
        if latterDetector.detect() and doorLock.isLock(): # if the door lock and the Detect of the door
            lcd.clear()
            writeLine(0, 'Number of')
            writeLine(1, ('latters: %i') % latterDetector.getLatterCounter().getCounter())

except KeyboardInterrupt:
    GPIO.cleanup()

