import matplotlib
matplotlib.use('TkAgg')
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import os.path
from tkinter import messagebox
from backend import Backend


class PlotWindow(tk.Toplevel):
    '''
    this class plots the price trend or bar chart depending on the user choice
    '''

    def __init__(self, master, fct):
        self.master = master
        super().__init__(master)
        fig = plt.figure(figsize=(8, 7))
        fct()
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().grid()
        canvas.draw()


class MainWindow(tk.Tk):
    '''
    this class create main window from tk class and catches errors with the opening of the files
    '''

    def __init__(self, *infilenames):
        self.backend = Backend()
        super().__init__()
        self.canvas = tk.Canvas(self, height=700, width=1200)
        self.canvas.pack()

        frame = tk.Frame(self.canvas, background='#2C5881', border=5)
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        button = tk.Button(frame, text='XY Plot', background='#CBD7D5', border=5, command=self.displayXYPlot)
        button.place(relx=0.03, rely=0.6, relwidth=0.2, relheight=0.2)
        button.config(font=("Palatino Linotype", 20, 'bold'))

        button2 = tk.Button(frame, text='Bar Chart', background='#CBD7D5', border=5,
                            command=self.displayBar)
        button2.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.2)
        button2.config(font=("Palatino Linotype", 20, 'bold'))

        button3 = tk.Button(frame, text='Linear Regression', background='#CBD7D5', border=5,
                            command=self.displayLinearRegression)
        button3.place(relx=0.8, rely=0.6, relwidth=0.2, relheight=0.2)
        button3.config(font=("Palatino Linotype", 20, 'bold'))

        label = tk.Label(frame, text='Temperature Graphs', background='#2C5881')
        label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.2)
        label.config(font=("Palatino Linotype", 40, 'bold'))

        for file in infilenames:
            if os.path.exists(file) == False or os.path.isfile(file) == False:
                tk.messagebox.showwarning("Error", "Cannot open this file\n(%s)" % file)

    def displayXYPlot(self):
        '''
        opens a DialogWindow for the temperatures
        '''
        PlotWindow(self, self.backend.xyPlot)

    def displayLinearRegression(self):
        '''
        creates a linear regression graph
        '''
        PlotWindow(self, self.backend.linearRegression)

    def displayBar(self):
        '''
        creates a plotWindow graphing the bar chart
        '''
        PlotWindow(self, self.backend.barChart)


infileNames = ["temperature.html"]

mainWin = MainWindow(*infileNames)
mainWin.mainloop()
