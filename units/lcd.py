import RPi.GPIO as GPIO
from RPLCD import CharLCD
import units.settings as settings

lcd = CharLCD(numbering_mode = GPIO.BCM, #init lcd
              pin_rs=settings.pins["lcd"]["rs"],
              pin_e=settings.pins["lcd"]["en"],
              pins_data=settings.pins["lcd"]["data"],
              cols=40, rows=2)

def clearLine(line): # clear lcd
    lcd.cursor_pos = (line, 0)
    lcd.write_string(' ' * 40)
    lcd.cursor_pos = (line, 0)
    
def writeLine(line, msg): #write on the lcd
    lcd.cursor_pos = (line, 0)
    msg += (' ' * (40 - len(msg)))
    lcd.write_string(msg)