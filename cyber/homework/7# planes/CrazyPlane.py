from AirCube import AirCube
import random

class CrazyPlane:
    def __init__(self):
        tempX = random.randint(1, 8)
        tempY = random.randint(1, 8)
        self.__pos = AirCube(tempX, tempY)
        self.__velX = random.randint(0, 2)
        if(self.__velX == 0):
            self.__velY = random.randint(1, 2)
        else:
            self.__velY = random.randint(0, 2)

    def update(self) -> None:
        print()
    
    def getNewVel(self) -> tuple:
        self.__velX = random.randint(-1, 1)
        if(self.__velX == 0):
            self.__velY = random.randint(0, 1)
        else:
            self.__velY = random.randint(0, 2)
