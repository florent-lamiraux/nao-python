#from naoqi import ALProxy
from hpp.corbaserver import Client
from hpp_corbaserver.hpp import Configuration
from nao.config import allJoints, upperJoints, legJoints, halfSitting

client = Client()
timeStep = .02

def loadRobot():
    client.problem.parseFile("/home/florent/devel/nao/model/nao-hpp.kxml")

def setRobotHalfSitting():
    client.robot.setCurrentConfig(0, 2*[0.] + [0.31] + 3*[0.] + halfSitting)

def createSmallBox():
    client.obstacle.createBox('object', 0.05, 0.05, 0.05)
    client.obstacle.addObstacle('object')
    cfg = Configuration(trs = [.2, 0., 0.4], 
                        rot = [1., 0., 0., 0., 1., 0., 0., 0., 1.])
    client.obstacle.moveObstacleConfig('object', cfg)

def seqplay(pathId, time):
    """
    Play a motion computed by KineoPathPlanner
    """
    path = []
    pathLength = client.problem.pathLength(0, pathId)
    nbSteps = int(time/timeStep)
    for s in range(nbSteps):
        u = s*pathLength/nbSteps
        config = client.problem.configAtDistance(0, pathId, u)
        path.append(config[6:])
    motion = list(map(list, zip(*path)))
    times = len(motion)*[[timeStep*(i+1) for i in range(len(path))]]
    return motion, times

    
