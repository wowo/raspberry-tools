import RPi.GPIO as GPIO
import time

class PeriodicOutput:
    DURATION_FAST = 0.1
    DURATION_MEDIUM = 0.25
    DURATION_SLOW = 0.5
    DURATION_OUT = 0.5
    
    def __init__(self, gpio_pin):
        self.gpio_pin = gpio_pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        GPIO.setup(self.gpio_pin, GPIO.OUT)
        GPIO.output(self.gpio_pin, GPIO.LOW)

    def __out(self, period, pause, out = None):
        if out is None:
            out = self.DURATION_OUT

        cycles = int(period / (out+ pause))
        for x in range(0, cycles):
            GPIO.output(self.gpio_pin, GPIO.HIGH)
            time.sleep(out)
            GPIO.output(self.gpio_pin, GPIO.LOW)
            time.sleep(pause)
    
    def fast(self, period):
        self.__out(period, PeriodicOutput.DURATION_FAST, PeriodicOutput.DURATION_FAST)
    
    def medium(self, period):
        self.__out(period, PeriodicOutput.DURATION_MEDIUM)
    
    def slow(self, period):
        self.__out(period, PeriodicOutput.DURATION_SLOW)
