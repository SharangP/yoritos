import time
try:
    import RPi.GPIO as GPIO
except ImportError:
    import fakegpio as GPIO

from flask import Flask

# only buttons 0-6 and 8 are used
# (button, gpio pin)
PIN_MAP = [
    (1, 3),
    (2, 5),
    (3, 7),
    (4, 8),
    (5, 10),
    (6, 12),
    (8, 11),
    (0, 13)
]

VALID_IDS = [10, 11, 20, 21, 30, 31, 40, 41, 50, 51, 60, 61, 80, 81, 82, 83, 84, 85]

class Vendor(object):
    def __init__(self, high_side=True):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(True)
	self.high_side = high_side

        for button, pin in PIN_MAP:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW if self.high_side else GPIO.HIGH)

    def cleanup(self):
        GPIO.cleanup()

    def press(self, num, timeout=0.2):
        for button, pin in PIN_MAP:
            if num == button:
                GPIO.output(pin, GPIO.HIGH if self.high_side else GPIO.LOW)
                time.sleep(timeout)
                GPIO.output(pin, GPIO.LOW if self.high_side else GPIO.HIGH)
                return
        assert False, "Invalid pin"

vendor = Vendor()

app = Flask(__name__)

@app.route("/vend/<int:id>")
def vend(id):
  if not id in VALID_IDS:
    d1 = id / 10
    d2 = id % 10
    vendor.press(d1)
    time.sleep(0.1)
    vendor.press(d2)
    return "vended"
  else:
    return "invalid id"

app.run(host='0.0.0.0', port=80, debug=True)
