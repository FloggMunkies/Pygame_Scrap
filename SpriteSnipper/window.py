import tkinter as tk
from PIL import Image, ImageTk
import os


# ----- Needs Updated -----
PACKAGE_PATH = "C:/Users/Matthew/PycharmProjects/Pygame_Scrap"


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.running = False
        self.initialized = False

        self.image_path = os.path.join(PACKAGE_PATH, "Mario_Sheet.png")
        self.image = ImageTk.PhotoImage(Image.open(os.path.abspath(self.image_path)))
        # self.image_label = tk.Label(self.root, image=self.image)
        # self.image_label.pack()

    def on_init(self, start=True):
        self.running, self.initialized = start, True

    def on_execute(self):
        if not self.initialized:
            self.on_init()

        if self.running:
            self.root.mainloop()


main_window = Window()

if __name__ == "__main__":
    main_window.on_execute()
