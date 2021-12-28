import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import numpy as np
from run import *

"""
def callback(self, inp):
    if inp.isdigit():
        return True
    # change input of (column, row)
"""


class AdjMatrix(tk.Frame):
    def __init__(self, parent, n):
        tk.Frame.__init__(self, parent)
        self.entry = {}
        self.rows = n
        self.columns = n
        self.entered_number = 0
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)

                if row == column:
                    e = tk.Entry(self, name=str(row) + ',' + str(column), justify='center', width=8)
                    e.insert(0, '0')
                    e.config(state='disabled')
                elif row > column:
                    e = tk.Entry(self, name=str(row) + ',' + str(column), justify='center', width=8)
                    e.config(state='disabled')
                else:
                    reg = self.register(self.callback)
                    e = tk.Entry(self, name=str(row) + ',' + str(column), justify='center', validate="key",
                                 validatecommand=(reg, '%P', '%W'), width=8)

                e.grid(row=row, column=column)
                self.entry[index] = e

    def get(self):
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                try:
                    val = int(self.entry[index].get())
                except ValueError:
                    # warn widget
                    val = 0
                current_row.append(val)
            result.append(current_row)
        return result

    # def set(self, num, row, col):

    def callback(self, inp, name):
        if not inp:  # the field is being cleared
            self.entered_number = 0
            return True

        if inp == '0' or inp == '1':
            inp = int(inp)
            self.entered_number = inp
            i = tuple(map(int, (name.split(".")[-1]).split(',')))
            list_i = list(i)
            list_i[0], list_i[1] = list_i[1], list_i[0]
            ir = tuple(list_i)
            self.entry[ir].config(state='normal')
            self.entry[ir].delete(0, 'end')
            self.entry[ir].insert(0, self.entered_number)
            self.entry[ir].config(state='disabled')
            return True
        else:
            # warn widget
            return False


def create_adj_matrix():
    frame2.grid_remove()
    global matrix
    n = int(e111.get())
    if -1 < n < 13:
        matrix.grid_remove()
        matrix = AdjMatrix(frame12, n)
        b121 = tk.Button(frame12, text='Planarity Test', command=lambda: convert_adj_matrix_to_np_array())
        matrix.grid(row=0, column=0, columnspan=3)
        b121.grid(row=1, column=1)
        frame12.grid(row=1, column=0)
    else:
        pass


def planar_test(adj_matrix_array):
    graph = nx.from_numpy_array(adj_matrix_array) #, parallel_edges=True, create_using=nx.MultiGraph
    print(graph)
    planar = run(graph)
    if planar:
        txt.set("Your entered graph is planar.\n")
    else:
        txt.set("Your entered graph is not planar.\n")
    msg.grid(row=0, column=0)
    frame2.grid(row=2, column=0)


def convert_adj_matrix_to_np_array():
    adj_matrix = matrix.get()
    adj_matrix_array = np.array(adj_matrix)
    planar_test(adj_matrix_array)


def show_enter_matrix():
    frame1a.grid_remove()
    frame12.grid_remove()
    frame2.grid_remove()
    frame1.grid(row=1, column=0)
    if e111.get() != '0':
        print(e111.get())
        e111.delete(0, 'end')
        e111.insert(0, '0')


def symmetric(a, rtol=1e-05, atol=1e-08):
    return np.allclose(a, a.T, rtol=rtol, atol=atol)


def check_correct_matrix_format(adj_matrix_array):
    if adj_matrix_array.shape[0] != adj_matrix_array.shape[1]:
        return False
    elif not np.all((adj_matrix_array == 0) | (adj_matrix_array == 1)):
        return False
    elif not symmetric(adj_matrix_array):
        return False
    elif not np.all(adj_matrix_array.diagonal() == 0):
        return False
    else:
        return True


def show_read_in_matrix():
    frame1.grid_remove()
    frame2.grid_remove()
    file = askopenfile(parent=frame, mode='rb', title='Choose a file', filetype=[("Csv File", "*.csv")])
    if file:
        adj_matrix_array = np.genfromtxt(file, delimiter=',')
        if check_correct_matrix_format(adj_matrix_array):
            print(adj_matrix_array.shape)
            print(type(adj_matrix_array))
            b1a1 = tk.Button(frame1a, text='Planarity Test', command=lambda: planar_test(adj_matrix_array))
            b1a1.grid(row=0, column=0)
            frame1a.grid(row=1, column=0)
        else:
            pass
            # warn signal


root = tk.Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

frame = tk.Frame(root, padx=20, bg='red')  # , pady=20,width=600, height=600,

frame01 = tk.Frame(frame, padx=20, bg='orange')  #
logo = Image.open('logo1.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(frame01, image=logo, bd=0)
logo_label.image = logo
logo_label.grid(row=0, column=0, columnspan=2)
b011 = tk.Button(frame01, text='Enter matrix', bg='#D7D7D7', command=lambda: show_enter_matrix())
b012 = tk.Button(frame01, text='Read in matrix', bg='#D7D7D7', command=lambda: show_read_in_matrix())
b011.grid(row=1, column=0)
b012.grid(row=1, column=1)
frame01.grid(row=0, column=0)
frame.grid(row=0, column=0)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
"""
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
"""

frame1 = tk.Frame(root, bg='blue')  # , bg='blue', width=600, height=600, pady=20,


frame11 = tk.Frame(frame1, padx=20, bg='grey')  # , pady=20, width=600, height=600,
l111 = tk.Label(frame11, text='Number of nodes')
e111 = tk.Entry(frame11, justify='center', width=12)
e111.insert(0, '0')
matrix = AdjMatrix(frame11, 0)
b111 = tk.Button(frame11, text='Create Matrix', bg='#D7D7D7', command=lambda: create_adj_matrix())
l111.grid(row=0, column=0)
e111.grid(row=0, column=1)
b111.grid(row=0, column=2, padx=10)
frame11.grid(row=0, column=0)

# Planarity Test Button
frame12 = tk.Frame(frame1, bg='red')
frame12.grid(row=1, column=0)

frame1a = tk.Frame(root, padx=20, bg='purple')
root.grid_rowconfigure(1, weight=1)

frame2 = tk.Frame(root, padx=20, bg='yellow')  # , pady=20, , width=600, height=100,
txt = tk.StringVar(frame2)
msg = tk.Message(frame2, textvariable=txt)

root.grid_rowconfigure(2, weight=1)

root.mainloop()

# run()
