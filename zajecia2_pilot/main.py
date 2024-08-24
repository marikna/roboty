#!/usr/bin/env pybricks-micropython

# Remote control code
# Don't pick it up until it beeps, or the Gyro calibration will be off.

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

gyro = GyroSensor(Port.S1)
ts = TouchSensor(Port.S4)

motor_d = Motor(Port.A)  # duzy silnik  - pokrętło
motor_s = Motor(Port.D)  # sredni silnik - wajcha


# Write your program here.

from pybricks.messaging import BluetoothMailboxServer, BluetoothMailboxClient, Mailbox, TextMailbox, NumericMailbox, LogicMailbox

# Replace this by the Bluetooth address of the tankbot
# Remember to pair both EV3 bricks first.

tankbot = "78:DB:2F:28:6E:C6" 

client = BluetoothMailboxClient()
client.connect(tankbot)
ev3.speaker.beep()
print("Connected to {}".format(tankbot))

steering =  NumericMailbox('move', client)

while True:
    if motor_d.speed() > 0:
        steering.send(1)
        print("wyslalem wiadomosc na prawe kolo #1")

    elif motor_d.speed() < 0:
        steering.send(2)
        print("wyslalem wiadomosc na lewe kolo #2")

    elif gyro.angle() > 20:
        steering.send(3)
        print("Wyslalem wiadomosc na kola #3")
    
    elif gyro.angle() < -20:
        steering.send(4)
        print("Wyslalem wiadomosc na kola #4")

    elif ts.pressed():
        steering.send(5)
        print("Wyslalem wiadomosc na #5")
    
    else:
        steering.send(5)