BOARD = 1
BCM = 2

OUT = 3
IN = 4

HIGH = True
LOW = False

def setmode(mode):
    print "setmode(%s)" % ("BOARD" if mode == 1 else "BCM")

def setwarnings(enable):
    print "setwarnings(%s)" % ("True" if enable else "False")

def setup(pin, type, initial=HIGH):
    print "setup(%d, %s, initial=%s)" % (pin, "OUT" if type == OUT else "IN", "HIGH" if initial else "LOW")

def cleanup():
    print "cleanup()"

def output(pin, val):
    print "output(%d, %s)" % (pin, "HIGH" if val else "LOW")
