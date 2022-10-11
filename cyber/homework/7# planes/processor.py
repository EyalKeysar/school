import time
import sys
import pygame
from AirSpace import AirSpace

BG_COLOR = (0, 0, 0)  # black
RED_COLOR = (255, 0, 0)  # red
BLOCK_LENGTH = 50
SCREEN_SIZE = 500
try:
    plain_img_0 = pygame.image.load('planes/0.png')
    plain_img_1 = pygame.image.load('planes/1.png')
    plain_img_2 = pygame.image.load('planes/2.png')
    plain_img_3 = pygame.image.load('planes/3.png')
    plains_images = [plain_img_0, plain_img_1, plain_img_2, plain_img_3]
except FileNotFoundError:
    print("Planes images not found.")
    sys.exit(1)


def main() -> None:
    global display
    ais = AirSpace()
    
    pygame.init()
    display = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    
    # Graphic and main loop.
    while(True):
        for event in pygame.event.get():  # Get each of the current events.
            if(event.type == pygame.KEYDOWN):  # If the event was a key pressing.
                if(event.key == pygame.K_ESCAPE):  # If that key was escape.
                    pygame.quit()  # Quit and close program window.
                    quit()
        pygame.display.update()
        
        # Draw frame.
        drawGrid()
        for num in range(4):  # For each plane.
            cur_plain =  ais.getPlane(num)  # Get current plane by his number.
            last_pos_x, last_pos_y = cur_plain.getPos()
            cur_plain.update()  # Update it's position.
            new_pos_x, new_pos_y = cur_plain.getPos()
            if(new_pos_x in {0, 9} or new_pos_y in {0,9}):
                sys.exit(1)
            drawPlain(num, cur_plain.getPos()[0], cur_plain.getPos()[1])  # Draw plane in new position.
        time.sleep(1)

    pygame.quit()
    quit()
    
def drawGrid():
    display.fill(BG_COLOR)
    for x in range(0, SCREEN_SIZE, BLOCK_LENGTH):
        for y in range(0, SCREEN_SIZE, BLOCK_LENGTH):
            rect = pygame.Rect(x, y, BLOCK_LENGTH, BLOCK_LENGTH)
            pygame.draw.rect(display, RED_COLOR, rect, 1)

def drawPlain(plain_num, x, y):
    img = pygame.transform.scale(plains_images[plain_num], (50, 50))
    display.blit(img, (x*50,y*50))

if __name__ == "__main__":
    main()