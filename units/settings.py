import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#*************** digit pin**********


sonar = {#unit [cm]
    "unit": "cm",
    "samples": 3
}

height = {
    "latter": {
        "max": 6,
        "min": 4.5,
    },
    "box": 16
}

pins = {
    "door": 4,
    "servo": 3,
    "buzzer": 21,
    "keypad": {
        "rows": [5],
        "cols": [26, 19, 13, 6],
    },
    "sonar": {
        "echo": 12,
        "trigger": 16
    },
    "lcd": {
        "rs": 17,
        "en": 27,
        "data": [11, 9, 10, 22]
    }
}

servoFreq = 50
buzzerFreq = 1000

defaultPassword = 1234