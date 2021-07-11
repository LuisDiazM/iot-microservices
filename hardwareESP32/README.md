# ESP32 with micropython

- Install esptool `pip install esptool`

- Erase firmware from board `esptool.py --port /dev/ttyUSB0 erase_flash`

- To write the firmware on board (.bin file is the firmware that has micropython installed, if you are interested in other firmwares you can download in the next [link](https://micropython.org/download/esp32/)) `esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20210418-v1.15.bin` NOTE: OS windows use serial ports COM, OS based on linux use serial ports /dev/ttyUSB{}

- Install rshell for communicate with the ESP32 `pip install rshell`

- Comunicate with the board `rshell --buffer-size=30 -p /dev/ttyUSB0`

You can check the board using `boards`, the folder where our scripts will run is `/pyboard`
all the scripts need to be copy using the `cp <file> /pyboard`, by example:

* In the folder `src` is the scripts that contain the code for send information via NATS publish and control I/O porst `cp -r * /pyboard`

* If you want to check the script run over board is necesary connect via `repl` and import the program or using soft rebot with CTRL + D command.

## Important
`boot.py` is the script that runs when the board is ON


## References

If you want more information you can visit the links:

* Config the host to comunicate the ESP32 via serial port [link](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html#esp32-intro)

* Video to connect ESP32 with micropython [link](https://www.youtube.com/watch?v=w15-EQASP_Y)
