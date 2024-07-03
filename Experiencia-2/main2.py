#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor, Motor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
md = Motor(Port.B)
mi = Motor(Port.C)
robot = DriveBase(mi,md,55.5,104)

color_sensor = ColorSensor(Port.S3)

while True:
    color = color_sensor.color()

    if color == Color.BLACK: #si detecta el color negro
           md.run(speed=90) 
           mi.run(speed=300)
    else:
            md.run(speed=300)
            mi.run(speed=90)
            wait(10)