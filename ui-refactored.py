import pygcurse, pygame, sys
from pygame.locals import *

def parser(command):
    #Going to be replaced with the actual game logic
    global imgfile
    global image
    if command == 'caccaa':
        imgfile = 'bridge-ascii-2.png'
        image = pygame.image.load(imgfile)
    elif command == 'ei caccaa':
        imgfile = 'bridge-ascii.png'
        image = pygame.image.load(imgfile)
    elif command == 'quit':
        return False
    return True

def init_ui():    
    #Making sure we can access the variables
    global gamewindow
    global imgfile
    global image
    global box
    global sidebox
    global print
    global input

    #Defining the UI
    gamewindow = pygcurse.PygcurseWindow(120, 40)
    gamewindow.font = pygame.font.Font('terminus.ttf', 14)
    print = gamewindow.pygprint
    input = gamewindow.input
    imgfile = 'bridge-ascii.png'
    image = pygame.image.load(imgfile)
    pygame.display.set_caption('Universe Mission')    
    box = pygcurse.PygcurseTextbox(gamewindow, (1, 27, 118, 12), fgcolor='black', bgcolor=(0,255,0), border='basic', wrap=True, marginleft=1, margintop=1, caption='Hello world!')
    sidebox = pygcurse.PygcurseTextbox(gamewindow, (100, 1, 19, 25), fgcolor='black', bgcolor=(255,0,0), border='basic', wrap=True, marginleft=1, margintop=1, caption='Inventory')
    box.text = 'This is the Universe Mission test text box.'
    sidebox.text = 'Tools         Mops         Other things'
    sound = pygame.mixer.Sound('spacehum.ogg')
    sound.play()

def main():
    global gamewindow
    global box
    global sidebox

    init_ui()
    running = True
    
    #The actual game loop
    while running:
        gamewindow.setscreencolors((0,255,0), 'black', clear=True)
        gamewindow.surface.blit(image,(10,10))
        box.update()
        sidebox.update()
        gamewindow.cursor = 0, gamewindow.height-1
        command = input(' >')
        box.text = str(command)
        if parser(command):
            pygame.display.update()
        else:
            running = False
            pygame.quit()

if __name__ == "__main__": main()
