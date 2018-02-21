import pygame as pg


class App:
    def __init__(self):
        self._running = False
        self._display_surf = None
        self._initialized = False
        self.size = self.width, self.height = 640, 400

    def on_init(self, start=True):
        pg.init()
        self._display_surf = pg.display.set_mode(self.size, pg.HWSURFACE | pg.DOUBLEBUF)
        self._running, self._initialized = start, True

    def on_event(self, event):
        if event.type == pg.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

    @staticmethod
    def on_cleanup():
        pg.quit()

    def on_execute(self):
        if not self._initialized:
            self.on_init()

        while self._running:
            for event in pg.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


# Main game loop


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()

