import pygcurse, pygame, sys, engine, mysql.connector
from pygame.locals import *

response = ""
running = True
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
sound = pygame.mixer.Sound('song2.ogg')

def parser(command):
    #Going to be replaced with the actual game logic
    global imgfile
    global image
    engine.command(command)
    if command == 'quit':
        return False
    return True

def parseprint(text):
    global response
    global gamewindow
    response = str(text)

def init_ui():    
    #Making sure we can access the variables
    global gamewindow
    global imgfile
    global image
    global box
    global sidebox
    global print
    global input
    global sound

    #Defining the UI
    gamewindow = pygcurse.PygcurseWindow(120, 40)
    gamewindow.font = pygame.font.Font('terminus.ttf', 14)
    print = gamewindow.pygprint
    input = gamewindow.input
    imgfile = 'bridge.png'
    image = pygame.image.load(imgfile)
    pygame.display.set_caption('Universe Mission')    
    box = pygcurse.PygcurseTextbox(gamewindow, (1, 27, 118, 12), fgcolor='black', bgcolor=(148,148,148), border='basic', wrap=True, marginleft=1, marginright=1, margintop=1, caption='Universe Mission')
    sidebox = pygcurse.PygcurseTextbox(gamewindow, (100, 1, 19, 25), fgcolor='white', bgcolor=(65,65,65), border='basic', wrap=True, marginleft=1, marginright=1, margintop=1, caption='Inventory')
    box.text = 'This is the Universe Mission test text box.'
    sidebox.text = 'Tools         Mops         Other things'
    sound.play(-1)

def stop_running():
    global running
    global sound
    sound.set_volume(0)
    sound = pygame.mixer.Sound('gameover.ogg')
    sound.set_volume(100)
    sound.play(1)
    running = False

def main():
    global db
    global cur
    global gamewindow
    global sidebox
    global response
    global running
    #Remnants from previous version
    #videoplayer.set_video("intro.mp4")
    #videoplayer.run()
    init_ui()
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    #The actual game loop
    while running:
        engine.isitover()
        image = pygame.image.load(engine.roomimage())
        gamewindow.setscreencolors((148,148,148), 'black', clear=True)
        gamewindow.surface.blit(image,(10,10))
        sidebox.text = str(engine.itemsavailablelist())
        box.text = engine.returnConsoletext()
        box.caption = engine.database("roomname")
        box.update()
        sidebox.update()
        gamewindow.cursor = 0, gamewindow.height-1
        command = input(' >')
        if parser(command):
            pygame.display.update()
        else:
            stop_running()
    engine.db.close()
    pygame.quit()

if __name__ == "__main__": main()
