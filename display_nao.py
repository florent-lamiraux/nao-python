#!/usr/bin/python
"""
Read position of joints and display robot configuration in KiteLab
"""
from naoqi import ALProxy
import hpp.corbaserver as hpc

IP = "192.168.1.63"
PORT = 9559

jointNames = ['RHipYawPitch', 
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

def connect(host, port):
    global motionProxy
    motionProxy = ALProxy("ALMotion", host, port)

def loadRobot():
    """
    Load robot into HPP by sending a corba request
    """
    client = hpc.Client()
    client.problem.parseFile("/home/florent/devel/nao/model/nao.kxml")

def getConfiguration():
    """
    Read Nao's encoders and return configuration as a tuple of float.
    """
    config = [0.,0.,0.,0.,0.,0.]
    jointAngles = motionProxy.getAngles(jointNames, True)
    config.extend(jointAngles)
    config[6] = config[17]
    config[17] *= -1.
    return config

def trackRobot():
    client = hpc.Client()
    for i in range(500):
        config = getConfiguration()
        client.robot.setCurrentConfig(0, config)
