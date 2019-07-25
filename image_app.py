# For creating desktop app.
import tkinter as tk
import tkinter
import tkinter.filedialog
from tkinter import *
from image_resize import image_location

master = tk.Tk()
master.title("Image Resizing App")
w = 660  # width for the Tk root
h = 400  # height for the Tk root

# get screen width and height
ws = master.winfo_screenwidth()  # width of the screen
hs = master.winfo_screenheight()  # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

# set the dimensions of the screen
# and where it is placed
master.geometry('%dx%d+%d+%d' % (w, h, x, y))
master.resizable(0, 0)

lbl1 = Label(master, text="Enter image Height in PX", bg="orange red", fg="white", font="none 12 bold")
lbl1.grid(row=0, column=1, padx=30, pady=20)

lbl1 = Label(master, text="Enter image Weight in PX", bg="orange red", fg="white", font="none 12 bold")
lbl1.grid(row=0, column=3, padx=30, pady=20)

l_c = 15
g_c = 1
px = 75
py = 5

e1 = tk.Entry(master)
e2 = tk.Entry(master)
tk.Label(master, text="Height").grid(row=3, column=g_c)
tk.Label(master, text="Weight").grid(row=3, column=g_c + 2)
e1.grid(row=5, column=g_c, pady=5)
e2.grid(row=5, column=g_c + 2, pady=5)

e3 = tk.Entry(master)
e4 = tk.Entry(master)
e3.grid(row=6, column=g_c, pady=5)
e4.grid(row=6, column=g_c + 2, pady=5)

e5 = tk.Entry(master)
e6 = tk.Entry(master)
e5.grid(row=7, column=g_c, pady=5)
e6.grid(row=7, column=g_c + 2, pady=5)

e7 = tk.Entry(master)
e8 = tk.Entry(master)
e7.grid(row=8, column=g_c, pady=5)
e8.grid(row=8, column=g_c + 2, pady=5)

e9 = tk.Entry(master)
e10 = tk.Entry(master)
e9.grid(row=9, column=g_c, pady=5)
e10.grid(row=9, column=g_c + 2, pady=5)


def call_function_(f, first, second):
    image_location(f, first, second)


def print_path(first):
    f = tkinter.filedialog.askopenfilename(
        parent=master, initialdir='/',
        title='Choose file',
        filetypes=[('png images', '.png'),
                   ('jpag images', '.jpg'),
                   ('gif images', '.gif')]
    )
    image_location(f, first)
    return f


def button_value():
    height1 = e1.get()
    weight1 = e2.get()

    height2 = e3.get()
    weight2 = e4.get()

    height3 = e5.get()
    weight3 = e6.get()

    height4 = e7.get()
    weight4 = e8.get()

    height5 = e9.get()
    weight5 = e10.get()

    total_h_w = [height1, weight1, height2, weight2, height3, weight3, height4, weight4, height5, weight5]
    print_path(total_h_w)
    return height1, weight1


# tk.Button(master, text='Quit', command=master.quit).grid(row=8,  sticky=tk.W, padx=50, pady=4)

tk.Button(master, text='Value', command=button_value).grid(row=12, column=2, sticky=tk.W, pady=6)

tk.mainloop()
