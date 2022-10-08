from this import s
from AirCube import AirCube
import AirSpace
import random

class CrazyPlane:
    def __init__(self, num: int):
        airSpace = AirSpace()
        tempX = random.randint(1, 8)
        tempY = random.randint(1, 8)
        self.__pos = AirSpace.getCube(tempX, tempY)
        self.__velX = random.randint(0, 2)
        if(self.__velX == 0):
            self.__velY = random.randint(1, 2)
        else:
            self.__velY = random.randint(0, 2)

    def setPos(self, x: int, y: int) -> None:
        self.__pos = AirSpace.getCube(x, y)

    def getPos(self) -> tuple:
        return self.__pos.getPlace()

    def setVel(self, x: int, y: int) -> None:
        if((x in {1, -1}) and (y in {1, -1})):
            self.__velX = x
            self.__velY = y
        else:
            self.__velX = 1
            self.__velY = 1
    def getVel(self) -> tuple:
        return (self.__velX, self.__velY)

    def update(self) -> None:
        if(self.getPos[0] != 0 and self.getPos[1] != 0 and self.getPos[0] != 9 and self.getPos[1] != 9):
            self.setPos(self.getPos[0] + self.getVel[0], self.getPos[1] + self.getVel[1])

    def getNewVel(self) -> tuple:
        self.__velX = random.randint(-1, 1)
        if(self.__velX == 0):
            self.__velY = random.randint(0, 1)
        else:
            self.__velY = random.randint(0, 2)
