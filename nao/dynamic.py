#!/usr/bin/python
#
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

from nao.config import allJoints, halfSitting
from dynamic_graph.sot.core import FeatureGeneric, Task
from dynamic_graph.sot.dynamics.parser import Parser
from dynamic_graph.sot.dynamics.humanoid_robot import AbstractHumanoidRobot

# --- Coumpound drive ---------
class CompoundDrive (FeatureGeneric):
    def __init__(self, name, robot):
        FeatureGeneric.__init__(self, name)
        self.robot = robot
        self.index1 = 6 + allJoints.index('RHipYawPitch')
        self.index2 = 6 + allJoints.index('LHipYawPitch')

    def update(self):
        q = self.robot.signal('state').value
        i1 = self.index1
        i2 = self.index2
        self.signal('errorIN').value = (q[i2]+q[i1],)
        self.signal('jacobianIN').value = (i1*(0.,) + (1.,) +
                                           (i2-i1-1)*(0.,) + (1.,) +
                                           (6+len(allJoints)-i2-1)*(0.,),)

class Nao(AbstractHumanoidRobot):
    """
    This class instanciates a Nao robot as a humanoid robot
    """

    halfSitting = tuple([0.,0.,.31,0.,0.,0.] + halfSitting)

    def __init__(self, name, simulation, filename):
        AbstractHumanoidRobot.__init__(self, name, simulation)

        p = Parser(self.name + '.dynamics', filename)
        self.dynamic = p.parse()
        self.dimension = self.dynamic.getDimension()
        if self.dimension != len(self.halfSitting):
            raise "invalid half-sitting pose"
        self.initializeRobot()
        self.compoundDrive = CompoundDrive(self.name + 'compoundDrive',
                                           self.simu)
        self.compoundDriveTask = Task(self.name + 'compoundDriveTask')
        self.compoundDriveTask.add(self.name + 'compoundDrive')
        self.compoundDriveTask.signal('controlGain').value = 1.

