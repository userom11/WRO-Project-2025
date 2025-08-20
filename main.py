#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize
leftMotor = Motor(Port.1)
rightMotor = Motor(Port.4)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
Cage = Moter(Port.A, Direction.CLOCKWISE)
frontSensor = ColorSensor(Port.3)
backSensor = ColorSensor(Port.A)

# Work
# robot.settings() will tweak later, check https://pybricks.com/ev3-micropython/robotics.html
robot.turn(-21)
robot.straight(750)
squareColours = ("RED","YEllOW","GREEN","BLUE")
inFront = frontSensor(color)
Behind = backSensor(color)
Cage(run_angle(speed=, rotational_angle=,wait=true))

ev3.speaker.beep()
