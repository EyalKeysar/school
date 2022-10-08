from this import s
import random

class CrazyPlane:
    def __init__(self, num: int):
        self.__pos = (random.randint(1, 8), random.randint(1, 8))
        self.__velX = random.randint(0, 2)
        if(self.__velX == 0):
            self.__velY = random.randint(1, 2)
        else:
            self.__velY = random.randint(0, 2)

    def setPos(self, x: int, y: int) -> None:
        if(x <= 10 and x>= 0 and y<= 10 and y>= 0):
            self.__pos = (x, y)

    def getPos(self) -> tuple:
        return self.__pos

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
        if(self.getPos()[0] != 0 and self.getPos()[1] != 0 and self.getPos()[0] != 9 and self.getPos()[1] != 9):
            self.setPos(self.getPos()[0] + self.getVel()[0], self.getPos()[1] + self.getVel()[1])

    def getNewVel(self) -> tuple:
        self.__velX = random.randint(-1, 1)
        if(self.__velX == 0):
            self.__velY = random.randint(0, 1)
        else:
            self.__velY = random.randint(0, 2)
