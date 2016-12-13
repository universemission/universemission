import pygame, pyglet, ctypes
pyglet.lib.load_library('avbin')
pyglet.have_avbin=True

window = pyglet.window.Window(fullscreen=True)
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()

def set_video(video):
    global window
    global player
    MediaLoad = pyglet.media.load(video)
    player.queue(MediaLoad)
    player.play()

@window.event
def on_draw():
    global window
    global player
    window.clear()
    if player.source and player.source.video_format:
        player.get_texture().blit(0,0)

def update(dt):
    global player
    if not player.playing:
        pyglet.app.exit()

def run():
    dt = pyglet.clock.tick()
    pyglet.clock.schedule(update)
    pyglet.app.run()
