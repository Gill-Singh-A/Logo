import pygame, math, random
from optparse import OptionParser
from pygame.locals import *
from datetime import date
from colorama import Fore, Style
from time import strftime, localtime, time, sleep

delay = 0.1
side = 800
draw_circles = True


status_color = {
    '+': Fore.GREEN,
    '-': Fore.RED,
    '*': Fore.YELLOW,
    ':': Fore.CYAN,
    ' ': Fore.WHITE
}

def display(status, data, start='', end='\n'):
    print(f"{start}{status_color[status]}[{status}] {Fore.BLUE}[{date.today()} {strftime('%H:%M:%S', localtime())}] {status_color[status]}{Style.BRIGHT}{data}{Fore.RESET}{Style.RESET_ALL}", end=end)

def get_arguments(*args):
    parser = OptionParser()
    for arg in args:
        parser.add_option(arg[0], arg[1], dest=arg[2], help=arg[3])
    return parser.parse_args()[0]

def draw(window, depth, angle, delay, draw_circles, random_draw):
    window.fill((0, 0, 0))
    r = min(window.get_size())//2
    centre = (window.get_size()[0]//2, window.get_size()[1]//2)
    color = (255, 255, 255)
    m = r / depth
    while r > 0:
        draw = True
        if random_draw != None:
            drawTruthValue = random.uniform(0, 1)
            if drawTruthValue < random_draw:
                draw = False
        if draw == True and draw_circles == True:
            pygame.draw.circle(window, color, centre, r, 1)
        sleep(delay)
        pygame.display.update()
        coords = []
        for i in range(0, 360, angle):
            coords.append([centre[0]+r*math.cos(i*11/630), centre[1]+r*math.sin(i*11/630)])
        for index, coord in enumerate(coords):
            for i in range(index+1, len(coords)):
                draw = True
                if random_draw != None:
                    drawTruthValue = random.uniform(0, 1)
                    if drawTruthValue < random_draw:
                        draw = False
                if draw == True:
                    pygame.draw.line(window, color, coord, coords[i], 1)
                sleep(delay)
                pygame.display.update()
        r -= m

if __name__ == "__main__":
    data = get_arguments(('-r', "--resolution", "resolution", f"Side of the Sqaure (in pixels, Default={side})"),
                         ('-c', "--circles", "circles", "Number of Circles to Draw"),
                         ('-a', "--angle", "angle", "Angle of Sector (in degrees)"),
                         ('-d', "--delay", "delay", "Delay between drawing 2 consecutive Lines"),
                         ('-s', "--save", "save", "Name of the File in which the Image has to be stored (Default=current date and time)"),
                         ('-C', "--draw-circles", "draw_circles", f"Draw Circles (True/False, Default={draw_circles})"),
                         ('-R', "--random", "random", "Draw an object with a probability (Between [0, 1])"))
    if not data.resolution:
        data.resolution = side
    else:
        data.resolution = int(data.resolution)
    if data.draw_circles == "False":
        data.draw_circles = False
    else:
        data.draw_circles = draw_circles
    if not data.circles and draw_circles == True:
        display('-', "Please provide the Number of Circles to Draw")
        exit(0)
    else:
        data.circles = int(data.circles)
    if not data.angle:
        display('-', "Please provide the Angle of the Sector")
        exit(0)
    else:
        data.angle = int(data.angle)
    if not data.delay:
        data.delay = delay
    else:
        data.delay = float(data.delay)
    if not data.save:
        data.save = f"{date.today()} {strftime('%H_%M_%S', localtime())}.jpg"
    if not data.random:
        data.random = None
    else:
        data.random = 1-float(data.random)
    pygame.init()
    window = pygame.display.set_mode((data.resolution, data.resolution))
    draw(window, data.circles, data.angle, data.delay, data.draw_circles, data.random)
    pygame.display.update()
    pygame.image.save(window, data.save)
    pygame.quit()