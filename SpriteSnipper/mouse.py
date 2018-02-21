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
        # print("ROOT: " + "{}, {}".format(self.root.winfo_rootx(), self.root.winfo_rooty()))
        # print("POINTER: " + "{}, {}".format(x, y))
        # print("WINFO: " + "{}, {}".format(self.root.winfo_x(), self.root.winfo_y()))

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

    def is_inside(self, x, y):
        # print("----- IS INSIDE CHECK -----")
        # print("{}, {}, {}".format(self.root.winfo_rootx(), x, self.root.winfo_rootx()+self.root.winfo_width()))
        # print("{}, {}, {}".format(self.root.winfo_rooty(), y, self.root.winfo_rooty() + self.root.winfo_height()))

        SCROLLBAR_W = 16
        SCROLLBAR_H = 16
        if self.root.winfo_rootx() < x < self.root.winfo_rootx()+self.root.winfo_width()-SCROLLBAR_W:
            if self.root.winfo_rooty() < y < self.root.winfo_rooty() + self.root.winfo_height()- SCROLLBAR_H:
                print("Is inside? True")
                return True
        print("Is inside? False")
        return False

    def get_coord(self, event):
        x, y = self.root.winfo_pointerx(), self.root.winfo_pointery()
        print("{}, {}".format(x, y))
        if not self.is_inside(x, y):
            return
        if self.coords is 0:
            self.coords = 1
            self.rect[0], self.rect[1] = x, y
            return
        if self.coords is 1:
            self.coords = 2
            self.rect[2], self.rect[3] = x, y
            self.get_image(self.rect)
            # TODO Need an absolute rect and a relative rect for image collection and rectangle drawing respectivley.
            self.canvas.create_rectangle(self.rect[0], self.rect[1], self.rect[2], self.rect[3])
            return
        # pass

    def on_execute(self):
        if not self.initialized:
            self.on_init()

        if self.running:
            self.root.mainloop()


reader = MouseReader()

if __name__ == "__main__":
    reader.on_execute()
