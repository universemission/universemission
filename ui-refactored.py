import pygcurse, pygame, sys
from pygame.locals import *

global print
global input

def parser(command):
    global imgfile
    global image
    if command == 'caccaa':
        imgfile = 'bridge-ascii-2.png'
        image = pygame.image.load(imgfile)
    elif command == 'ei caccaa':
        imgfile = 'bridge-ascii.png'
        image = pygame.image.load(imgfile)    
        
win = pygcurse.PygcurseWindow(120, 40)
win.font = pygame.font.Font('terminus.ttf', 14)
imgfile = 'bridge-ascii.png'
image = pygame.image.load(imgfile)
pygame.display.set_caption('Universe Mission')
print = win.pygprint
input = win.input
box = pygcurse.PygcurseTextbox(win, (1, 27, 118, 12), fgcolor='black', bgcolor='green', border='basic', wrap=True, marginleft=1, margintop=1, caption='Hello world!')
sidebox = pygcurse.PygcurseTextbox(win, (100, 1, 19, 25), fgcolor='black', bgcolor='red', border='basic', wrap=True, marginleft=1, margintop=1, caption='Inventory')
box.text = 'This is the Universe Mission test text box.'
sidebox.text = 'Tools         Mops         Other things'
sound = pygame.mixer.Sound('spacehum.ogg')
sound.play()

while True:
    win.setscreencolors('green', 'black', clear=True)
    win.surface.blit(image,(10,10))
    box.update()
    sidebox.update()
    win.cursor = 0, win.height-1
    command = input(' >')
    box.text = str(command)
    parser(command)
    pygame.display.update()
