import RPi.GPIO as GPIO
import time

led_pin = 7

def setup():
  GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
  GPIO.setup(led_pin, GPIO.OUT)   # Set led_pin's mode is output
  GPIO.output(led_pin, GPIO.HIGH) # Set led_pin high(+3.3V) to turn on led

def blink():
  while True:
    print('on')
    GPIO.output(led_pin, GPIO.HIGH)  # led on
    time.sleep(1)
    print('off')
    GPIO.output(led_pin, GPIO.LOW) # led off
    time.sleep(1)
    
def destroy():
  GPIO.output(led_pin, GPIO.LOW)   # led off
  GPIO.cleanup()                  # Release resource
if __name__ == '__main__':     # Program start from here
  setup()
  try:
    blink()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()
