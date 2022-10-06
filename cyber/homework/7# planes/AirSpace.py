from CrazyPlane import CrazyPlane
from AirCube import AirCube
from typing import *

class AirSpace:
    
    def __init__(self):
        self.__airGrid: List[List[AirCube]] = [[]]
        self.__crazyPlanes: List[CrazyPlane] = []


        for i in range(10):
            for r in range(10):
                self.__airGrid[i][r] = AirCube(i, r)
        for i in range(4):
            self.__crazyPlanes[i] = CrazyPlane()
            
    def mainLoop(self):
        loopBool = True
        while(loopBool):
            for plane in self.__crazyPlanes:
                plane.update()