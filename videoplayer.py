import pygame, pyglet, ctypes
pyglet.lib.load_library('avbin')
pyglet.have_avbin=True

vidPath="intro.mp4"
window = pyglet.window.Window(fullscreen=True)
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
MediaLoad = pyglet.media.load(vidPath)

player.queue(MediaLoad)
player.play()

@window.event
def on_draw():
    window.clear()
    if player.source and player.source.video_format:
        player.get_texture().blit(0,0)

def on_key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        return True

def run():
    pyglet.app.run()

