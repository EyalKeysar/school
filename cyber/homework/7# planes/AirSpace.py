import CrazyPlane
import AirCube
class AirSpace:
    __airGrid: list
    __crazyPlanes: list
    
    def __init__(self):
        for i in range(10):
            for r in range(10):
                self.__airGrid[i, r] = AirCube()
        for i in range(4):
            self.__crazyPlanes[i] = CrazyPlane()
            
    def mainLoop(self):
        loopBool = True
        while(loopBool):
            print()