import time
import sys
import pygame
from AirSpace import AirSpace

# Set constants.
BG_COLOR = (10, 10, 100)  # Black
RED_COLOR = (255, 0, 0)  # Red
BLOCK_LENGTH = 50 # In pixels.
SCREEN_SIZE = 500 # In pixels.
try:
    # Load all planes images.
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
    display = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE)) # Initialize the pygame window.

    # Graphic and main loop.
    while(True):
        for event in pygame.event.get():  # Get each of the current events.
            if(event.type == pygame.KEYDOWN):  # If the event was a key pressing.
                if(event.key == pygame.K_ESCAPE):  # If that key was escape.
                    pygame.quit()  # Quit and close program window.
                    quit()

        pygame.display.update()

        # Draw objects in the frame.
        drawGrid()
        ais.updateAirSpace()  # Update the values of air space to next frame values.
        for num in range(4):  # For each plane.
            cur_plain =  ais.getPlane(num)  # Get current plane by his number.
            drawPlane(num, cur_plain.getPos()[0], cur_plain.getPos()[1])  # Draw plane in new position.
        time.sleep(1)

def drawGrid() -> None: 
    '''
    This function draws screen_size by screen_size background with a grid in density of block_size.
    '''
    display.fill(BG_COLOR)  # Fill the background color.
    for x in range(0, SCREEN_SIZE, BLOCK_LENGTH):  # Draw each rectangle.
        for y in range(0, SCREEN_SIZE, BLOCK_LENGTH):
            rect = pygame.Rect(x, y, BLOCK_LENGTH, BLOCK_LENGTH)
            pygame.draw.rect(display, RED_COLOR, rect, 1)

def drawPlane(plain_num, x, y):
    '''
    This function gets a plane number and position and draws it.
    '''
    img = pygame.transform.scale(plains_images[plain_num], (50, 50))
    display.blit(img, (x*50,y*50))

if __name__ == "__main__":
    main()