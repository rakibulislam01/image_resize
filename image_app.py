import tkinter as tk
import tkinter
import tkinter.filedialog
from image_resize import image_location

master = tk.Tk()
e1 = tk.Entry(master)
e2 = tk.Entry(master)
tk.Label(master,
         text="First Name").grid(row=0)
tk.Label(master,
         text="Last Name").grid(row=1)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


def call_function_(f, first, second):
    image_location(f, first, second)


def print_path(first, second):
    f = tkinter.filedialog.askopenfilename(
        parent=master, initialdir='/home/rakibul/Desktop/',
        title='Choose file',
        filetypes=[('png images', '.png'),
                   ('jpag images', '.jpg'),
                   ('gif images', '.gif')]
    )
    print(f)
    image_location(f, first, second)
    return f


def button_value():
    first = e1.get()
    second = e2.get()

    print_path(first, second)
    return first, second


tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)

tk.Button(master,
          text='Value', command=button_value).grid(row=3,
                                                   column=2,
                                                   sticky=tk.W,
                                                   pady=4)

tk.mainloop()

#
# root = tk.Tk()
# def print_path():
#     f = tkinter.filedialog.askopenfilename(
#         parent=root, initialdir='/home/rakibul/',
#         title='Choose file',
#         filetypes=[('png images', '.png'),
#                    ('gif images', '.gif')]
#     )
#     # image_location(f)
#     size_input_field()
#     return f
#
#
# b1 = tkinter.Button(root, text='Print path', command=print_path)
# b1.pack(fill='x')
#
# root.mainloop()
