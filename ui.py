import pygcurse, pygame, sys, engine, mysql.connector, videoplayer
from pygame.locals import *

response = ""

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
    sound = pygame.mixer.Sound('spacehum.ogg')
    sound.play(-1)

def main():
    global db
    global cur
    global gamewindow
    global sidebox
    global response
    videoplayer.run()
    init_ui()
    running = True

    #The actual game loop
    while running:
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
        #box.text = str(command)
        if parser(command):
            pygame.display.update()
        else:
            running = False
            engine.db.close()
            pygame.quit()

if __name__ == "__main__": main()
