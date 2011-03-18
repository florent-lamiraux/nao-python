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

import sys
sys.path.append('/home/florent/devel/nao/aldebaran-sdk-1.8.11-linux-i386/lib/python2.6')
sys.path.append('/home/florent/devel/nao/aldebaran-sdk-1.8.11-linux-i386/lib')

IP_cable = "192.168.31.6"
IP_wifi = "192.168.31.5"
IP = IP_cable

port = 9559

allJoints = ['RHipYawPitch', 
             'RHipRoll',
             'RHipPitch',
             'RKneePitch',
             'RAnklePitch',
             'RAnkleRoll',
             'LShoulderPitch',
             'LShoulderRoll',
             'LElbowYaw',
             'LElbowRoll',
             'LWristYaw',
             'LHipYawPitch',
             'LHipRoll',
             'LHipPitch',
             'LKneePitch',
             'LAnklePitch',
             'LAnkleRoll',
             'RShoulderPitch',
             'RShoulderRoll',
             'RElbowYaw',
             'RElbowRoll',
             'RWristYaw',
             'HeadYaw',
             'HeadPitch']

legJoints = ['RHipYawPitch', 
              'RHipRoll',
              'RHipPitch',
              'RKneePitch',
              'RAnklePitch',
              'RAnkleRoll',
              'LHipYawPitch',
              'LHipRoll',
              'LHipPitch',
              'LKneePitch',
              'LAnklePitch',
              'LAnkleRoll']

upperJoints = ['LShoulderPitch',
              'LShoulderRoll',
              'LElbowYaw',
              'LElbowRoll',
              'LWristYaw',
              'RShoulderPitch',
              'RShoulderRoll',
              'RElbowYaw',
              'RElbowRoll',
              'RWristYaw',
              'HeadYaw',
              'HeadPitch']

halfSitting = [4.1961669921875e-05, 0.0092459619045257568, -0.38660997152328491, 0.94498598575592041, -0.55526602268218994, -0.0076280385255813599, 1.8254181146621704, 0.20244604349136353, -1.4788179397583008, -0.5123140811920166, -0.019983962178230286, -4.1961669921875e-05, 0.0092459619045257568, -0.38652604818344116, 0.94183409214019775, -0.55688399076461792, -0.0076280385255813599, 1.8208999633789062, -0.19946196675300598, 1.478734016418457, 0.54000997543334961, 0.055182039737701416, -0.001575961709022522, 0.0091620385646820068]
