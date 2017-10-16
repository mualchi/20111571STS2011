"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # BCM mode setup
GPIO.setup(26, GPIO.IN) # 26pin input

NUM_CYCLES = 10 #

def detect():
    global total
    start = time.time()

    for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(26, GPIO.FALLING)

    duration = time.time() - start
    freq = NUM_CYCLES / duration
    print("freq = %.1fHz, Q = %.2fL/min" % (freq, freq/43))
    total += freq * (duration + 0.5) / 2580
    print("duration = %.5f" % duration)
    print("Total = %.2fL" % total)
    time.sleep(0.5)
    return
"""
import RPi.GPIO as GPIO
import time

class Datain:

    def __init__(self):
        self.total = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.IN)
        self.NUM_CYCLES = 10
        
    def detect(self):
        start = time.time()

        for impulse_count in range(self.NUM_CYCLES):
            GPIO.wait_for_edge(26, GPIO.FALLING)
            
        duration = time.time() - start
        freq = self.NUM_CYCLES / duration
        print("freq = %.1fHz, Q = %.2fL/min" % (freq, freq/43))
        self.total += freq * (duration + 0.5) / 2580
        print("duration = %.5f" % duration)
        print("Total = %.2fL" % self.total)
        time.sleep(0.5)

    def renew(self):
        self.total = 0
