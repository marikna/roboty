#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from random import randint

# Create your objects here.
ev3 = EV3Brick()

# Configure 2 motors on Ports A and D.  Set the motor directions to
# counterclockwise, so that positive speed values make the robot move
# forward.  These will be the left and right motors of Tankbot.
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)


# The wheel diameter of Tankbot is about 54 mm.
WHEEL_DIAMETER = 54

# The axle track is the distance between the centers of each of the
# wheels.  This is about 200 mm for Tankbot.
AXLE_TRACK = 200

# The Driving Base is comprised of 2 motors.  There is a wheel on each
# motor.  The wheel diameter and axle track values are used to make the
# motors move at the correct speed when you give a drive command.
robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, AXLE_TRACK)

# Set up the Timer.  It is used to move for a random time.
timer = StopWatch()

# Write your program here.
# Łączenie się z klientem 
from pybricks.messaging import (BluetoothMailboxServer, 
BluetoothMailboxClient, Mailbox, TextMailbox, NumericMailbox, LogicMailbox)

server = BluetoothMailboxServer()
server.wait_for_connection(1)

steering = NumericMailbox('move', server)
# This is the main part of the program.  It is a loop that repeats
# endlessly.
# 78:DB:2F:18:8B:6E

ev3.speaker.beep()

while True:
    steering.wait()
    steer_read = steering.read()
    if steer_read == 1:
        # Turn right.
        robot.drive(0, 250)
        # print("Odczytano 1 pzdr")
    
    elif steer_read == 2:   
        # Turn left.
        robot.drive(0, -250)
        # print("Odczytano 2")

    elif steer_read == 3:
        robot.drive(-500, 0)
        # print("Odczytano 3")

    elif steer_read == 4:
        robot.drive(500, 0)
        # print("Odczytano 4")

    elif steer_read == 5:
        robot.stop()
        # print("Odczytano 5")
    # jazda prosto
    # pelny obrot 
    # beepniecie
    # jazda do tylu
