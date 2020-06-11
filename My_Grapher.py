# Importing Modules

import matplotlib.pyplot as plt
import numpy as np
from tkinter import *

# Making Window
win = Tk()
win.title('Grapher')
win.geometry('500x330+400+100')
win.resizable(0, 0)
var = IntVar()


# Making plotter function
def plotter():
    function = eqEnter.get()

    '''replacing trigonometric ratios, power, log, inverse-trigonometric ratios'''
    rep = {'^': '**', 'cos(': 'np.cos(', 'sin(': 'np.sin(', 'tan(': 'np.tan(',
           'sec(': '1/np.cos(', 'cosecant(': '1/np.sin(', 'cot(': '1/np.tan(', 'log': 'np.log',
           'sin-1': 'np.arcsin', 'cos-1': 'np.arccos', 'tan-1': 'np.arctan'}
    for key in rep.keys():
        if key in function:
            function = function.replace(key, rep[key])

    '''making domain'''
    domain = entryDomain.get()
    upper_l = float(domain.split(',')[1])
    lower_l = float(domain.split(',')[0])

    print(function, upper_l, lower_l)

    '''plotting graph'''
    x = np.arange(lower_l, upper_l, step=0.1)
    y = eval(function)

    '''marker on/off'''
    if var.get():
        plt.plot(x, y, color='blue', linestyle='dashed', linewidth=2,
                 marker='^', markersize='7', markerfacecolor='yellow')
    else:
        plt.plot(x, y, color='blue', linestyle='dashed', linewidth=2)

    x1 = 0
    y1 = 0
    plt.plot(x1, y1, "ro")
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    plt.axhline(-1, color='green')
    plt.axhline(1, color='green')
    plt.axvline(1, color='green')
    plt.axvline(-1, color='green')
    plt.show()


# Equation Label

eqFrame = Frame(master=win)
eqFrame.pack(side='top', fill=X)
eqLabel = Label(master=eqFrame, text='Enter f(x) : '
                , anchor=W, font=('verdana', 10, 'bold'), pady=10)
eqLabel.pack(side='left')
eqEnter = Entry(master=eqFrame, width=55)
eqEnter.pack(side='left')

# Instruction Label

insFrame = Frame(master=win, height=150, width=100)
insFrame.pack(side='top', fill=X)
insLabel = Label(master=insFrame, text="Instructions :\n ",
                 anchor=W, font=('verdana', 10, 'italic'))
insLabel.pack(side='top', fill=X)
insLabel = Label(master=insFrame, text=" - y= f(x), so, enter only f(x). ",
                 anchor=W, font=('verdana', 10, 'italic'))
insLabel.pack(side='top', fill=X)
insLabel = Label(master=insFrame, text=" - While using exponential use '^'. ",
                 anchor=W, font=('verdana', 10, 'italic'))
insLabel.pack(side='top', fill=X)
insLabel = Label(master=insFrame,
                 text=" - Always use trigonometric ratios in lower case eg: cos(x) \nand inverse ratios as cos-1(x) ",
                 anchor=W, font=('verdana', 10, 'italic'))
insLabel.pack(side='top', fill=X)
insLabel = Label(master=insFrame, text="- Inverse Trigonometric ratios sec-1(), cosec-1(), \ncot-1() are not "
                                       "supported ",
                 anchor=W, font=('verdana', 10, 'italic'))
insLabel.pack(side='top', fill=X)
insLabel = Label(master=insFrame, text=" - please enter cosec(x) as cosecant(x)",
                 anchor=W, font=('verdana', 10, 'italic'))
insLabel.pack(side='top', fill=X)
insLabel = Label(master=insFrame, text=" - If desired graph is not obtained check if equation is "
                                       "entered correctly",
                 anchor=W, font=('verdana', 10, 'italic'))
insLabel.pack(side='top', fill=X)

# Plot button
plotButton = Button(master=insFrame, text='Plot', height=1, width=8,
                    bg='light green', command=plotter)
plotButton.pack(side='right', padx=20, pady=20)

markerShow = Checkbutton(master=insFrame, text='Show Markers', variable=var, anchor=W, pady=10, padx=20)
markerShow.pack(side='bottom', fill=X)

noteLabel = Label(master=insFrame, text=" -Note: Enter Domain in format of lower-limit, upper-limit"
                  , anchor=NW)
noteLabel.pack(side='bottom', fill=X)

domainLabel = Label(master=insFrame, text="Enter Domain : ", anchor=W, pady=10,
                    font=('verdana', 10, 'bold'))
domainLabel.pack(side='left')

entryDomain = Entry(master=insFrame, width=50)
entryDomain.pack(side='left')


# Main Loop
win.mainloop()
