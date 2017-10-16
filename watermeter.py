"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # BCM mode setup
GPIO.setup(26, GPIO.IN) # 26pin input

NUM_CYCLES = 10 #
total = 0 # Global var clear

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

while True:
    try:
        detect()

    except KeyboardInterrupt:
        wt = open("water.txt", 'w')
        wt.write(str(total))
        wt.close()
        print("=" * 20)
        print("Saved!")
        print("Total = %.2fL" % total)
        print("=" * 20)
        total = 0
        continue
"""

import sys
sys.path.append("/home/pi")

from Pythonwork.input import mod1
from Pythonwork.output import output
from Pythonwork.process import process



a = mod1.Datain()
a.detect()

b = output.Output()
b.output2()

c = process.Process()
c.process2()


while True:
    try:
        a.detect()

    except KeyboardInterrupt:
        a.renew()
        continue
