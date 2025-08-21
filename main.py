#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase


# Initialise.
ev3 = EV3Brick()

leftMotor = Motor(Port.1)
rightMotor = Motor(Port.4)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
Cage = Moter(Port.A, Direction.CLOCKWISE)
frontSensor = ColorSensor(Port.3)
backSensor = ColorSensor(Port.A)

# Work.

# challenge #1
robot.straight(1300)
Cage.run_angle(rotational_angle=100,wait=true)
robot.straight(-300)
robot.turn(-90)
robot.straight(800)
robot.turn(135) # go and place yellow
robot.straight(80)
cage.run_angle(rotational_angle=-100,wait=true)
robot.straight(-30)
cage.run_angle(rotational_angle=100, wait=true)
robot.straight(-50)
robot.turn(-90) # go and place red
robot.straight(80)
cage.run_angle(rotational_angle=-100,wait=true)
robot.straight(-80)

# challenge #2
robot.straight(-110)
# cage.run_angle(rotational_angle=-100,wait=true)
robot.turn(-45)
robot.straight(-20)
# cage.run_angle(rotational_angle=-100,wait=true)
robot.straight(-30)

# challenge #3
robot.turn(-45)
robot.staight(250)
robot.turn(-45)
robot.straight(150)
squareAling = backSensor.color() # color we want in facing front
robot.straight(500)

squareColours = ("YELLOW","GREEN","BLUE","RED")
if squareAling == "YELLOW":
  robot.straight(100)
  robot.turn(-90)
  cage.run_angle(rotational_angle=100,wait=true)
if squareAling == "GREEN":
  robot.straight(100)
  robot.turn(-90)
  robot.staight(100)
  robot.turn(-90)
  cage.run_angle(rotational_angle=100,wait=true)
  robot.staight(100)
  robot.turn(90)
if squareAling == "BLUE":
  robot.turn(-90)
  robot.straight(100)
  robot.turn(90)
  robot.straight(100)
  robot.turn(90)
  cage.run_angle(rotational_angle=100,wait=true)
  robot.turn(180)
  robot.straight(-10)
if squareAling == "RED":
  robot.turn(-90)
  robot.straight(100)
  robot.turn(90)
  cage.run_angle(rotational_angle=100,wait=true)
  robot.turn(-90)
  robot.straight(-20)
robot.turn(-100)
robot.straight(500)
cage.run_angle(rotational_angle=-100,wait=true)

# challenge #4
robot.straight(-250)
roboot.turn(-90)
robot.straight(300)
robot.straight(-30)
robot.turn(90)
robot.straight(60)
robot.turn(-90)
# cage.run_angle(rotational_angle=-100,wait=true)
# robot.straight()
# cage.run_angle(rotational_angle=-100,wait=true)

# challenge #5
robot.turn(90)
robot.straight(350)
robot.turn(90)
robot.straight(-50)
C = backSensor.color()
robot.straight(-50)
A = backSensor.color()
robot.turn(-90)
robot.straight(150)
robot.turn(-90)
B = backSensor.color()
robot.straight(-50)
D = backSensor.color()
robot.straight(-50)
robot.turn(-90)
robot.straight(800)
robot.turn(90)
cage.run_angle(rotational_angle=100,wait=true)
robot.turn(90)
ev3.speaker.beep()
