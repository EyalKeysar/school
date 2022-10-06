class AirCube:
    __place: tuple
    def __init__(self, x, y) -> None:
        if(x >= 0 and y >= 0 and x<=10 and y<=10):
            self.__place = (x, y)
        else:
            self.__place = (0,0)
    def getPlace(self) -> tuple:
        return self.__place
    def update(self, x, y) -> None:
        if(x >= 0 and y >= 0 and x<=10 and y<=10):
            self.__place = (x, y)
        else:
            self.__place = (0,0)