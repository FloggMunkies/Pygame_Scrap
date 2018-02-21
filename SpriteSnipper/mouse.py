import tkinter as tk
from PIL import ImageGrab


class MouseReader:
    def __init__(self):
        self.running = False
        self.initialized = False

        # Tkinter
        self.root = None
        self.frame = None
        self.hbar = None
        self.vbar = None

        # Canvas
        self.canvas = None
        self.image = None
        self.rect = [0, 0, 0, 0]
        self.coords = 0

    def motion(self, event):
        x, y = self.root.winfo_pointerx(), self.root.winfo_pointery()
        # print('{}, {}'.format(x, y))

    def get_image(self, rect):
        self.image = ImageGrab.grab(bbox=(rect[0], rect[1], rect[2], rect[3]))
        self.image.save("most_recent.png")

    def on_init(self, start=True):
        self.root.bind("<Motion>", self.motion)
        self.root.bind("<Button-1>", self.get_coord)

        self.hbar = tk.Scrollbar(self.frame, orient=tk.HORIZONTAL)
        self.hbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.hbar.config(command=self.canvas.xview)
        self.vbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.vbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.vbar.config(command=self.canvas.yview)
        self.canvas.create_image(0, 0, anchor="nw", image=self.image)

        self.running, self.initialized = start, True

    def get_coord(self, event):
        # x, y = self.root.winfo_pointerx(), self.root.winfo_pointery()
        # # print("{}, {}".format(x, y))
        # if self.coords is 0:
        #     self.coords = 1
        #     self.rect[0], self.rect[1] = x, y
        #     return
        # if self.coords is 1:
        #     self.coords = 2
        #     self.rect[2], self.rect[3] = x, y
        #     self.get_image(self.rect)
        #     self.canvas.create_rectangle(self.rect[0], self.rect[1], self.rect[2], self.rect[3])
        #     return
        pass

    def on_execute(self):
        if not self.initialized:
            self.on_init()

        if self.running:
            self.root.mainloop()


reader = MouseReader()

if __name__ == "__main__":
    reader.on_execute()
