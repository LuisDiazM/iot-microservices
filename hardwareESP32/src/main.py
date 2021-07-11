import machine
import time
import infraestructure.mpynats as nats
import domain.hardwareActions as hardware
import ujson

nats_URL = 'nats://192.168.1.56:4222'
subject_id = 'iot.devices.esp32'

try:
    connection = nats.Connection(url=nats_URL, verbose=True)
    connection.connect()
    while True:
        try:
            photo_resistor_voltage = hardware.read_Analog(39)
            if photo_resistor_voltage > 0 and photo_resistor_voltage <= 1.56:
                connection.publish(subject_id, ujson.dumps({"voltage": photo_resistor_voltage, "state":"HIGH"}) )
                hardware.on_LED(32)
            elif photo_resistor_voltage > 1.56 and photo_resistor_voltage <= 2.29:
                connection.publish(subject_id, ujson.dumps({"voltage": photo_resistor_voltage, "state":"MEDIUM"}) )
                hardware.on_LED(14)
            else:
                connection.publish(subject_id, ujson.dumps({"voltage": photo_resistor_voltage, "state":"LOW"}) )
                hardware.on_LED(15)
        except:
            hardware.all_Leds()
except:
    hardware.all_Leds()



