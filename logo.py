import pygame, sys, math, time
from pygame.locals import *

delay = float(sys.argv[4])

def draw(window, depth, angle):
    window.fill((0, 0, 0))
    r = min(window.get_size())//2
    centre = (window.get_size()[0]//2, window.get_size()[1]//2)
    color = (255, 255, 255)
    m = r / depth
    while r > 0:
        pygame.draw.circle(window, color, centre, r, 1)
        time.sleep(delay)
        pygame.display.update()
        coords = []
        for i in range(0, 360, angle):
            coords.append([centre[0]+r*math.cos(i*11/630), centre[1]+r*math.sin(i*11/630)])
        for index, coord in enumerate(coords):
            for i in range(index+1, len(coords)):
                pygame.draw.line(window, color, coord, coords[i], 1)
                time.sleep(delay)
                pygame.display.update()
        r -= m

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((int(sys.argv[1]), int(sys.argv[1])))
    draw(window, int(sys.argv[2]), int(sys.argv[3]))
    pygame.display.update()
    pygame.image.save(window, sys.argv[5])
    pygame.quit()