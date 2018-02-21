# Imports
import pygame as pg
from pygame.locals import *
import os, sys

# Functions


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    try:
        image = pg.image.load(fullname)
    except pg.error:
        print("Cannot load image:", name)
        raise SystemExit

    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()



# Classes


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 640, 400

    def on_init(self):
        pg.init()
        self._display_surf = pg.display.set_mode(self.size, pg.HWSURFACE | pg.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pg.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pg.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pg.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


class Foo(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)  # call Sprite Initializer

# Main Loop


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
