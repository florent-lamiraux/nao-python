#!/usr/bin/python

# Copyright (c) 2010, 2011 CNRS
# Author: Florent Lamiraux
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:

# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from math import pi, cos, sin
from naoqi import ALProxy
from nao import allJoints, legJoints, upperJoints, halfSitting, IP, port

mp = ALProxy("ALMotion", IP, port)
tts = ALProxy("ALTextToSpeech", IP, port)
ad = ALProxy('ALAudioDevice', IP, port)
memProxy = ALProxy('ALMemory', IP, port)
zeroStiffness = len(mp.getStiffnesses(allJoints)) * [0.]
halfStiffness = len(mp.getStiffnesses(allJoints)) * [0.7]
    
def setStiffness(jointList, value):
    """
    Set the same stiffness value for a list of joints
    """
    mp.setStiffnesses(jointList, len(jointList)*[value])

def closeHand(inHand):
    mp.closeHand(inHand)
    mp.setStiffnesses(inHand, 1.)

def closeHands():
    closeHand('RHand')
    closeHand('LHand')

def releaseHands():
    mp.setStiffnesses(['RHand', 'LHand'], [0.,0.])
    
    
def playMotion(motion, time):
    setStiffness(allJoints, 0.8)
    mp.angleInterpolation(allJoints, motion, time, True)

def testMotion(motion, time):
    setStiffness(allJoints, 0.4)
    mp.angleInterpolation(allJoints, motion, time, True)
    setStiffness(allJoints, 0.)

def standUp():
    setStiffness(allJoints, 0.8)
    mp.angleInterpolation(allJoints, halfSitting,
                          len(allJoints)*[[2.]], True)

def pathToMotion(path, timeStep):
    motion = list(map(list, zip(*path)))
    motion = motion[6:]
    times = len(motion)*[[timeStep*(i+1) for i in range(len(path))]]
    return (motion, times)


#mp.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION",False]]) 
