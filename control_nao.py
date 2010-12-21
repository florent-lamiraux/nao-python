#!/usr/bin/python

from math import pi, cos, sin
from naoqi import ALProxy

IP = "192.168.1.63"
PORT = 9559

mp = ALProxy("ALMotion", IP, PORT)
zeroStiffness = len(mp.getStiffnesses("BodyJoints")) * [0.]

    
def playMotion(motion, time):
    mp.setStiffnesses("Head", [0.5, 0.5])
    mp.angleInterpolation("Head", motion, time, True)
    mp.setStiffnesses("BodyJoints", zeroStiffness)

motion = []
time = []
timeSteps = []
yaws = []
pitches = []
dt = 0.01

for i in range(1,801):
    t = dt*i
    omega = 0.25*pi
    yaw = 0.2*(1. - cos(omega*t))
    pitch = 0.2*sin(omega*t)
    yaws.append(yaw)
    pitches.append(pitch)
    timeSteps.append(t)

motion.append(yaws)
motion.append(pitches)
time.append(timeSteps)
time.append(timeSteps)

#playMotion(motion, time)
