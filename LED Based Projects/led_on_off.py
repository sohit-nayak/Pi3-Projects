from gpiozero import LED
from time import sleep

led = LED(2)

led.on()
sleep(5)
led.off()
