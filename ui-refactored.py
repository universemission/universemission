import pygcurse, pygame, sys
from pygame.locals import *

global print
global input

win = pygcurse.PygcurseWindow(120, 40)
win.font = pygame.font.Font('terminus.ttf', 14)
image = pygame.image.load('bridge-ascii.png')
pygame.display.set_caption('Universe Mission')
print = win.pygprint
input = win.input
box = pygcurse.PygcurseTextbox(win, (1, 27, 118, 12), fgcolor='black', bgcolor='green', border='basic', wrap=True, marginleft=1, margintop=1, caption='Hello world!')
inventory = pygcurse.PygcurseTextbox(win, (100, 1, 19, 25), fgcolor='black', bgcolor='red', border='basic', wrap=True, marginleft=1, margintop=1, caption='Inventory')
box.text = 'This is the Universe Mission test text box.'
inventory.text = 'Tools         Mops         Other things'

while True:
    win.setscreencolors('green', 'black', clear=True)
    win.surface.blit(image,(10,10))
    box.update()
    inventory.update()
    win.cursor = 0, win.height-1
    letter = input(' >')
    box.text = str(letter)

