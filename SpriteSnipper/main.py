from mouse import reader
from window import main_window
import tkinter as tk

# Initialize Mouse Reader
reader.root = main_window.root
reader.image = tk.PhotoImage(file=main_window.image_path)
reader.frame = tk.Frame(reader.root, width=640, height=480)
reader.frame.pack()
reader.canvas = tk.Canvas(reader.frame, width=640, height=480, scrollregion=(0, 0, 700, 700))

reader.on_init(start=False)
reader.canvas.config(width=640, height=480)
reader.canvas.config(xscrollcommand=reader.hbar.set, yscrollcommand=reader.vbar.set)
reader.canvas.configure(scrollregion=reader.canvas.bbox("all"))
reader.canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# Substitute for root.mainloop but without blocking
while True:
    main_window.root.update_idletasks()
    main_window.root.update()
