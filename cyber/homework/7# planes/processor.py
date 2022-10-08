import pygame
from AirSpace import AirSpace

def main() -> None:
    ais = AirSpace()
    pygame.init()
    display = pygame.display.set_mode((500, 500))
    while(True):
        pygame.display.update()
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()