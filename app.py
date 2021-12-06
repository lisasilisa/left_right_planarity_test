import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import numpy as np
from run import *


class AdjMatrix(tk.Frame):
    def __init__(self, parent, n):
        tk.Frame.__init__(self, parent)
        self.entry = {}
        self.rows = n
        self.columns = n
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = tk.Entry(self)
                e.grid(row=row, column=column)
                if row == column:
                    e.insert(0, '1')
                else:
                    e.insert(0, '0')
                self.entry[index] = e

    def get(self):
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(int(self.entry[index].get()))
            result.append(current_row)
        return result


def create_adj_matrix():
    global matrix
    n = int(e1.get())
    matrix.grid_remove()
    matrix = AdjMatrix(frame1, n)
    b2 = tk.Button(frame1, text='Planarity Test', command=lambda: planarity_test())
    matrix.grid(row=1, column=0, columnspan=3)
    b2.grid(row=2, column=1)



def planarity_test():
    adj_matrix = matrix.get()
    adj_matrix_array = np.array(adj_matrix)
    graph = nx.from_numpy_array(adj_matrix_array, parallel_edges=True, create_using=nx.MultiGraph)
    planar = run(graph)
    print('planar', planar)


def planarity_test_1(adj_matrix_array):
    graph = nx.from_numpy_array(adj_matrix_array, parallel_edges=True, create_using=nx.MultiGraph)
    planar = run(graph)
    print('planar', planar)


def show_enter_matrix():
    frame1.grid(row=1, column=0)


def show_read_in_matrix():
    frame1.grid_remove()
    file = askopenfile(parent=frame, mode='rb', title='Choose a file', filetype=[("Csv File", "*.csv")])
    if file:
        adj_matrix_array = np.genfromtxt(file, delimiter=',')
        planarity_test_1(adj_matrix_array)



root = tk.Tk()

frame = tk.Frame(root, width=600, height=600, padx=20, pady=20)
logo = Image.open('logo1.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(frame, image=logo, bd=0)
logo_label.image = logo
logo_label.grid(row=0, column=0, columnspan=2)
b1 = tk.Button(frame, text='enter matrix', bg='#D7D7D7', command=lambda: show_enter_matrix())
b2 = tk.Button(frame, text='read in matrix', bg='#D7D7D7', command=lambda: show_read_in_matrix())
b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
frame.grid(row=0, column=0)

frame1 = tk.Frame(root, width=600, height=600, padx=20, pady=20)
l1 = tk.Label(frame1, text='Number of nodes')
e1 = tk.Entry(frame1, justify='center')
e1.insert(0, '0')

matrix = AdjMatrix(frame1, 0)
b11 = tk.Button(frame1, text='Create Matrix', bg='#D7D7D7', command=lambda: create_adj_matrix())
l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
b11.grid(row=0, column=2, padx=10)

root.mainloop()

#run()
