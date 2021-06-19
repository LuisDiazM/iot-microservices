import machine
import time

def on_LED(gpio_pin):
    # red gpio#15
    # green gpio#32
    # yellow gpio#14
    pin = machine.Pin(gpio_pin, machine.Pin.OUT)
    pin.on()
    time.sleep(10)
    pin.off()
    time.sleep(1)

def read_Analog(gpio_pin=39):
    #default pin 39 -> A3 ->ADC #1
    adc = machine.ADC(machine.Pin(gpio_pin))        
    adc.read()                 
    adc.atten(machine.ADC.ATTN_11DB) #3.6 V max input
    adc.width(machine.ADC.WIDTH_12BIT) #12 bits resolution
    voltage = (adc.read()/2**12)*3.6
    return voltage    

def all_Leds():
    pin_red = machine.Pin(15, machine.Pin.OUT)
    pin_green = machine.Pin(32, machine.Pin.OUT)
    pin_yellow = machine.Pin(14, machine.Pin.OUT)
    pin_red.on()
    pin_green.on()
    pin_yellow.on()
    time.sleep(10)
    pin_red.off()
    pin_green.off()
    pin_yellow.off()
    time.sleep(1)