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
# 라즈베리파이에서만 실행되는 코드이기 때문에 코드이식은 나중에 하고
# 패키지를 먼저 만들어 모듈을 import 하는 과정만 진행하였습니다.
import sys
sys.path.append("D:/user/workspace")

from Pythonwork.input import input
from Pythonwork.output import output
from Pythonwork.process import process

input.input_test()
output.output_test()
process.process_test()
