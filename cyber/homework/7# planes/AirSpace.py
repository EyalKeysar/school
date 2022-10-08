from CrazyPlane import CrazyPlane
from AirCube import AirCube
from typing import *

class AirSpace:
    def __init__(self):
        self.__airGrid = [[AirCube(x, y) for x in range(10)] for y in range(10)]  # Define 10 by 10 AirCube array.
        self.__crazyPlanes: List[CrazyPlane] = [CrazyPlane(0), CrazyPlane(1),CrazyPlane(2),CrazyPlane(3)]

    def mainLoop(self):
        loopBool = True
        while(loopBool):
            for plane in self.__crazyPlanes:
                plane.update()
    
    def getCube(self, x: int, y: int) -> AirCube:
        for i in self.__airGrid:
            if(i.getPlace() == (x, y)):
                return i