# HACKATHON 2023


import tkinter as tk
from tkinter import font
from tkinter import * 
import requests 
from PIL import ImageTk, Image

HEIGHT = 800
WIDTH = 600

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH, bg = '#304C89')
canvas.pack()

homePage = tk.Frame(root, bg = '#80c1ff', bd = 5)
homePage.place(relx = 0.5, rely = 0.5, relwidth = 0.75, relheight = 0.1, anchor = 'n')

title = Label(canvas, text = "MY VAC APP", font = ('Courier',40))
title.pack()
title.place(relx = 0.5, rely =0.1, anchor = 'n')

profile = Button(homePage, text = "Get Started", command = lambda: get_profilePage())
profile.pack(expand = True, fill = BOTH)


# currently just sample data/maps/etc. ---> want to use API's to access data in real time

def vacRecPage():
    vacRecPage = tk.Frame(root,bd=10, bg = "pink")
    vacRecPage.pack()
    vacRecPage.place(relx = 0.5, rely = 0, width = 600, height = 800, anchor = 'n')
    vrp = tk.Label(vacRecPage, text = "Vaccination Record Page", font = ('Courier', 16), anchor = 'nw', justify = 'left', bd = 4)
    vrp.place(relwidth = 1, relheight = 1)

def heatMapPage():
    heatMapPage = tk.Frame(root, bd = 10, bg = "violet")
    heatMapPage.pack()
    heatMapPage.place(relx = 0.5, rely = 0, width = 600, height = 800, anchor = 'n')
    hmp = tk.Label(heatMapPage, text = "Vaccination Access Level Map", font = ('Courier', 16), anchor = 'nw', justify = 'left', bd = 4)
    hmp.place(relwidth = 1, relheight = 1)

def vacMapPage():
    vacMapPage = tk.Frame(root, bd = 10, bg = "black")
    vacMapPage.pack()
    vacMapPage.place(relx = 0.5, rely = 0, width = 600, height = 800, anchor = 'n')
    vmp = tk.Label(vacMapPage, text = "Vaccination Site Map", font = ('Courier', 16), anchor = 'nw', justify = 'left', bd = 4)
    vmp.place(relwidth = 1, relheight = 1)

def statsPage():
    statsPage = tk.Frame(root, bd = 10, bg = "orange")
    statsPage.pack()
    statsPage.place(relx = 0.5, rely = 0, width = 600, height = 800, anchor = 'n')
    sp = tk.Label(statsPage, text = "Vaccination Levels & Cases", font = ('Courier', 16), anchor = 'nw', justify = 'left', bd = 4)
    sp.place(relwidth = 1, relheight = 1)
#################
def get_profilePage():
    # use frame to fill with sign picture of letter
    profilePage = tk.Frame(root, bd = 10, bg = "yellow")
    profilePage.pack()
    profilePage.place(relx = 0.5, rely = 0, width = 600, height = 800, anchor = 'n')

    # BACK/HOME BUTTON? to get home without closing
   
    vacRecords = Button(profilePage, text = "Vaccination Records", background = "blue", fg = "white", command = lambda: vacRecPage())
    vacRecords.pack()
    vacRecords.place(relx = 0.5, rely = 0.5, width = 200, height = 50, anchor = 'n')

    # gov't acct. extra
    heatMap = Button(profilePage, text = "Area Vaccination Access Levels", background = "blue", fg = "white", command = lambda: heatMapPage())
    heatMap.pack()
    heatMap.place(relx = 0.5, rely = 0.58, width = 200, height = 50, anchor = 'n')

    vacMap = Button(profilePage, text = "Vaccination Sites Nearby", background = "blue", fg = "white", command = lambda: vacMapPage())
    vacMap.pack()
    vacMap.place(relx = 0.5, rely = 0.66, width = 200, height = 50, anchor = 'n')

    # gov't acct. extra
    stats = Button(profilePage, text = "Area Vaccination Rates and Cases", background = "blue", fg = "white", command = lambda: statsPage())
    stats.pack()
    stats.place(relx = 0.5, rely = 0.74, width = 200, height = 50, anchor = 'n')

    root.mainloop()



root.mainloop()


