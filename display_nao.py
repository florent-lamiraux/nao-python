#!/usr/bin/python
"""
Read position of joints and display robot configuration in KiteLab
"""
from naoqi import ALProxy
import hpp.corbaserver as hpc

IP = "192.168.1.63"
PORT = 9559

def connect(host, port):
    global memProxy
    memProxy = ALProxy("ALMemory", host, port)

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
    jointNames = (
        # right leg
        "Device/SubDeviceList/RHipYawPitch/Position/Sensor/Value",
        "Device/SubDeviceList/RHipRoll/Position/Sensor/Value",
        "Device/SubDeviceList/RHipPitch/Position/Sensor/Value",
        "Device/SubDeviceList/RKneePitch/Position/Sensor/Value",
        "Device/SubDeviceList/RAnklePitch/Position/Sensor/Value",
        "Device/SubDeviceList/RAnkleRoll/Position/Sensor/Value",
        # left arm
        "Device/SubDeviceList/LShoulderPitch/Position/Sensor/Value",
        "Device/SubDeviceList/LShoulderRoll/Position/Sensor/Value",
        "Device/SubDeviceList/LElbowYaw/Position/Sensor/Value",
        "Device/SubDeviceList/LElbowRoll/Position/Sensor/Value",
        "Device/SubDeviceList/LWristYaw/Position/Sensor/Value",
        # left leg
        "Device/SubDeviceList/LHipYawPitch/Position/Sensor/Value",
        "Device/SubDeviceList/LHipRoll/Position/Sensor/Value",
        "Device/SubDeviceList/LHipPitch/Position/Sensor/Value",
        "Device/SubDeviceList/LKneePitch/Position/Sensor/Value",
        "Device/SubDeviceList/LAnklePitch/Position/Sensor/Value",
        "Device/SubDeviceList/LAnkleRoll/Position/Sensor/Value",
        # right arm
        "Device/SubDeviceList/RShoulderPitch/Position/Sensor/Value",
        "Device/SubDeviceList/RShoulderRoll/Position/Sensor/Value",
        "Device/SubDeviceList/RElbowYaw/Position/Sensor/Value",
        "Device/SubDeviceList/RElbowRoll/Position/Sensor/Value",
        "Device/SubDeviceList/RWristYaw/Position/Sensor/Value",
        # head
        "Device/SubDeviceList/HeadYaw/Position/Sensor/Value",
        "Device/SubDeviceList/HeadPitch/Position/Sensor/Value"
        )
    config = [0.,0.,0.,0.,0.,0.]
    for n in jointNames:
        config.append(memProxy.getData(n))
    config[6] = config[17]
    config[17] *= -1.
    return config

def trackRobot():
    client = hpc.Client()
    for i in range(5000):
        config = getConfiguration()
        client.robot.setCurrentConfig(0, config)
