from CrazyPlane import CrazyPlane
import sys
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
                

    def updateAirSpace(self) -> None:
        '''
        This function update each object in the airspace to the next values
        and checks is planes will collide next frame and if so it will change
        their direction.
        '''
        for i in range(4):
            # Cheack each plane if it will colide with another and if it is it will change direction.
            curPlane = self.getPlane(i)
            if(curPlane.getVel() == (0,0)):
                curPlane.getNewVel()
            curNextx, curNexty = curPlane.nextMove()  # Get next move.
            for r in range(4):
                if(i != r):
                    otherPlane = self.getPlane(r)
                    otherNextx, otherNexty = otherPlane.nextMove()
                    planesNextMovGood = False
                    while(not planesNextMovGood):
                        # Check if next move the planes will be out of the grid and if so
                        # change their direction.
                        if(curNextx in {10, -1} or curNexty in {10, -1}):
                            curPlane.setVel(-1 * curPlane.getVel()[0], -1 * curPlane.getVel()[1])
                            curNextx, curNexty = curPlane.nextMove()
                        # Checks for each plane if it will collide next move and if so
                        # change its direction.
                        if(curNextx == otherNextx and curNexty == otherNexty):
                            curPlane.setVel(-1 * curPlane.getVel()[0], -1 * curPlane.getVel()[1])
                            curNextx, curNexty = curPlane.nextMove()
                            if(curNextx in {10, -1} or curNexty in {10, -1}):
                                curPlane.setVel(curPlane.getVel()[0], -1 * curPlane.getVel()[1])
                                curNextx, curNexty = curPlane.nextMove()
                                if(curNextx in {10, -1} or curNexty in {10, -1}):
                                    curPlane.setVel(-1 * curPlane.getVel()[0], curPlane.getVel()[1])
                                    curNextx, curNexty = curPlane.nextMove()
                                    if(curNextx in {10, -1} or curNexty in {10, -1}):
                                        print("Plane is blocked by all sides.")
                                        sys.exit(1)
                                
                        else:
                            planesNextMovGood = True
            curPlane.update()  # Update current plane to its new position by its velocities.
                
                
    def getCube(self, x: int, y: int) -> AirCube:
        for i in self.__airGrid:
            if(i.getPlace() == (x, y)):
                return i
    
    def getPlane(self, num: int) -> CrazyPlane:
        return self.__crazyPlanes[num]