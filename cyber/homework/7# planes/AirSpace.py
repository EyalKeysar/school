from CrazyPlane import CrazyPlane
from AirCube import AirCube
from typing import *

class AirSpace:
    def __init__(self):
        self.__airGrid = [[AirCube(x, y) for x in range(10)] for y in range(10)]  # Define 10 by 10 AirCube array.
        all_planes_good = False
        while(not all_planes_good):
            self.__crazyPlanes: List[CrazyPlane] = [CrazyPlane(0), CrazyPlane(1),CrazyPlane(2),CrazyPlane(3)]
            all_planes_good = True
            for plane in self.__crazyPlanes:
                for other_plane in self.__crazyPlanes:
                    if(not plane == other_plane):
                        if(plane.getPos() == other_plane.getPos()):
                            all_planes_good = False
                

    def mainLoop(self):
        loopBool = True
        while(loopBool):
            for plane in self.__crazyPlanes:
                plane.update()
    
    def getCube(self, x: int, y: int) -> AirCube:
        for i in self.__airGrid:
            if(i.getPlace() == (x, y)):
                return i
    
    def getPlane(self, num: int) -> CrazyPlane:
        return self.__crazyPlanes[num]