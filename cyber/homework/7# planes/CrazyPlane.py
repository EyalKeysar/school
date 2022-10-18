import random
from typing import Tuple

class CrazyPlane:
    def __init__(self, num: int):
        self.__pos = (random.randint(1, 8), random.randint(1, 8)) # Gets random position.
        self.getNewVel()  # Gets random velocity.

    def setPos(self, x: int, y: int) -> None:
        '''
        This function set the position of a plane.
        '''
        if(x <= 10 and x>= 0 and y<= 10 and y>= 0):
            self.__pos = (x, y)

    def getPos(self) -> tuple:
        '''
        This function returns the position of a plane.
        '''
        return self.__pos

    def setVel(self, x: int, y: int) -> None:
        '''
        This function set the velocity of a plane.
        '''
        if((x in {1, -1}) and (y in {1, -1})):
            self.__velX = x
            self.__velY = y
        else:
            self.__velX = 1
            self.__velY = 1

    def getVel(self) -> tuple:
        '''
        This function returns the velocity of a plane.
        '''
        return (self.__velX, self.__velY)

    def update(self) -> None:
        '''
        This function update the plane position by its velocity.
        '''
        self.setPos(self.getPos()[0] + self.getVel()[0], self.getPos()[1] + self.getVel()[1])

    def nextMove(self) -> Tuple:
        '''
        This function returns the plane position in the next frame by its velocity.
        '''
        return (self.getPos()[0] + self.getVel()[0], self.getPos()[1] + self.getVel()[1])

    def getNewVel(self) -> tuple:
        '''
        This function return a randomly new velocity to the plane.
        '''
        self.__velX = random.randint(-1, 1)
        if(self.__velX == 0):
            self.__velY = random.randint(0, 1)
            if(self.__velY == 0):
                 self.__velY = -1
        else:
            self.__velY = random.randint(-1, 1)
