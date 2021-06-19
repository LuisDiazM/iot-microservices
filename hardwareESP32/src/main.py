import machine
import time
import infraestructure.mpynats as nats
import domain.hardwareActions as hardware
import ujson

try:
    nats_URL = 'nats://192.168.1.56:4222'
    subject_id = 'iot.devices.esp32'
    connection = nats.Connection(url=nats_URL, verbose=True)
    connection.connect()
except:
    pass

while True:
    try:
        time.sleep(1)
        photo_resistor_voltage = hardware.read_Analog(39)
        if photo_resistor_voltage > 0 and photo_resistor_voltage <= 1.56:
            hardware.on_LED(32)
            connection.publish(subject_id, ujson.dumps({"voltage": photo_resistor_voltage, "state":"HIGH"}) )
        elif photo_resistor_voltage > 1.56 and photo_resistor_voltage <= 2.29:
            hardware.on_LED(14)
            connection.publish(subject_id, ujson.dumps({"voltage": photo_resistor_voltage, "state":"MEDIUM"}) )
        else:
            hardware.on_LED(15)
            connection.publish(subject_id, ujson.dumps({"voltage": photo_resistor_voltage, "state":"LOW"}) )
    except:
        hardware.all_Leds()
        nats_URL = 'nats://192.168.1.56:4222'
        subject_id = 'iot.devices.esp32'
        connection = nats.Connection(url=nats_URL, verbose=True)
        connection.connect()


