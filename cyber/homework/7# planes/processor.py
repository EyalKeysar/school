import pygame
from AirSpace import AirSpace

BG_COLOR = (0, 0, 0)  # black
RED_COLOR = (255, 0, 0)  # red
BLOCK_LENGTH = 50
SCREEN_SIZE = 500

def main() -> None:
    global display
    ais = AirSpace()
    
    pygame.init()
    display = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    display.fill(BG_COLOR)
    drawGrid()
    while(True):
        pygame.display.update()
    pygame.quit()
    quit()
    
def drawGrid():
    for x in range(0, SCREEN_SIZE, BLOCK_LENGTH):
        for y in range(0, SCREEN_SIZE, BLOCK_LENGTH):
            rect = pygame.Rect(x, y, BLOCK_LENGTH, BLOCK_LENGTH)
            pygame.draw.rect(display, RED_COLOR, rect, 1)

if __name__ == "__main__":
    main()