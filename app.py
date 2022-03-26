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
                    # %P ist Input, %W ist name des Entry (z.B. .!frame2.!frame2.!adjmatrix.0,1)
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
                    val = 0
                current_row.append(val)
            result.append(current_row)
        return result

    def set(self, numpy_array):
        matrix_list = numpy_array.tolist()
        for row in range(len(matrix_list)):
            for column in range(len(matrix_list[row])):
                e = tk.Entry(self, name=str(row) + ',' + str(column), justify='center', width=8)

                self.entry[(row, column)].insert(0, int(matrix_list[row][column]))
                self.entry[(row, column)].config(state='disabled')

                e.grid(row=row, column=column)
                self.entry[(row, column)] = e

    # untere Diagonalmatrix ausfüllen (überprüfen, welche Zahlen in Ordnung sind)
    # callback functions überprüfen, ob eingegebener Wert valide ist
    def callback(self, inp, name):
        idx = tuple(map(int, (name.split(".")[-1]).split(',')))
        list_idx = list(idx)
        list_idx[0], list_idx[1] = list_idx[1], list_idx[0]
        idx_reversed = tuple(list_idx)

        if not inp:  # leeres Feld oder wenn man eine 1 wieder löscht, springt das Feld auf 0
            self.entry[idx_reversed].config(state='normal')
            self.entry[idx_reversed].delete(0, 'end')
            self.entry[idx_reversed].insert(0, 0)
            self.entry[idx_reversed].config(state='disabled')
            return True

        if inp == '0' or inp == '1':
            inp = int(inp)
            self.entry[idx_reversed].config(state='normal')
            self.entry[idx_reversed].delete(0, 'end')
            self.entry[idx_reversed].insert(0, inp)
            self.entry[idx_reversed].config(state='disabled')
            return True

        else:
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


def convert_adj_matrix_to_np_array():
    adj_matrix = matrix.get()
    print('adj_matrix app', adj_matrix)
    adj_matrix_array = np.array(adj_matrix)
    planar_test(adj_matrix_array)


def visualize_the_graph(final_adj_list, parent_edge, height, side):
    visualize(final_adj_list, parent_edge, height, side)


def planar_test(adj_matrix_array):
    graph = nx.from_numpy_array(adj_matrix_array)
    planar, parameter_list = run(graph)

    if planar:
        global b21
        b21.grid_remove()
        txt.set("Your entered graph is planar.\n")
        msg.grid(row=0, column=0, padx=10)
        b21 = tk.Button(frame2, text='Visualize Graph', bg='#D7D7D7',
                        command=lambda: visualize_the_graph(parameter_list[0], parameter_list[1], parameter_list[2],
                                                            parameter_list[
                                                                3]))  # final_adj_list, parent_edge, height, side
        b21.grid(row=0, column=1, padx=10)

    else:
        b21.grid_remove()
        txt.set("Your entered graph is not planar.\n")
        msg.grid(row=0, column=0, padx=10)

    frame2.grid(row=2, column=0)


def show_enter_matrix():
    frame1a.grid_remove()
    frame12.grid_remove()
    frame2.grid_remove()
    frame1.grid(row=1, column=0) # frame 1 ohne frame12 wird gezeigt
    if e111.get() != '0':
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
    frame1a.grid_remove()
    file = askopenfile(parent=frame0, mode='rb', title='Choose a file',
                       filetypes=[("Csv File", "*.csv")])
    if file:
        adj_matrix_array = np.genfromtxt(file, delimiter=',')
        if check_correct_matrix_format(adj_matrix_array):
            global matrixa
            n = adj_matrix_array.shape[0]
            if -1 < n < 13:
                matrixa.grid_remove()
                matrixa = AdjMatrix(frame1a, n)
                matrixa.set(adj_matrix_array)
                b1a1 = tk.Button(frame1a, text='Planarity Test', command=lambda: planar_test(adj_matrix_array))
                matrixa.grid(row=0, column=0, columnspan=3)
                b1a1.grid(row=1, column=1)
                frame1a.grid(row=1, column=0)
            else:
                pass


root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry("%dx%d" % (width, height))

# frame0: Logo + Auswahl-Button Eingabe / Einlesen
frame0 = tk.Frame(root, padx=20)

logo = Image.open('logo1.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(frame0, image=logo, bd=0)
logo_label.image = logo
logo_label.grid(row=0, column=0, columnspan=2)

b01 = tk.Button(frame0, text='Enter matrix', bg='#D7D7D7',
                command=lambda: show_enter_matrix())
b02 = tk.Button(frame0, text='Read in matrix', bg='#D7D7D7',
                command=lambda: show_read_in_matrix())
b01.grid(row=1, column=0)
b02.grid(row=1, column=1)

frame0.grid(row=0, column=0)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# frame1: Eingabebereich
frame1 = tk.Frame(root)

# frame11: Eingabe der Knotenanzahl
frame11 = tk.Frame(frame1, padx=20)
l111 = tk.Label(frame11, text='Number of nodes')
e111 = tk.Entry(frame11, justify='center', width=12)
e111.insert(0, '0')
b111 = tk.Button(frame11, text='Create Matrix', bg='#D7D7D7', command=lambda: create_adj_matrix())
l111.grid(row=0, column=0)
e111.grid(row=0, column=1)
b111.grid(row=0, column=2, padx=10)
frame11.grid(row=0, column=0)

# frame 12: Matrix + Planarity Test Button
frame12 = tk.Frame(frame1)
matrix = AdjMatrix(frame12, 0)
frame12.grid(row=1, column=0)

# frame1a ist der alternative frame1 für das Einlesen einer Matrix (2. Seite)
frame1a = tk.Frame(root, padx=20)
matrixa = AdjMatrix(frame1a, 0)

root.grid_rowconfigure(1, weight=1)

# Ausgabe, ob planar + Visualisierungsbutton
frame2 = tk.Frame(root, padx=20)  #
txt = tk.StringVar(frame2)
msg = tk.Message(frame2, textvariable=txt)
b21 = tk.Button()
root.grid_rowconfigure(2, weight=1)

root.mainloop()

