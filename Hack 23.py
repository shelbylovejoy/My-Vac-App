# HACKATHON 2023
import tkinter as tk
from tkinter import font
from tkinter import * 
import requests 
from tkintermapview import TkinterMapView
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter.ttk import Combobox


HEIGHT = 800
WIDTH = 600

root = tk.Tk()

# setting up opening page
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH, bg = '#310A31')
canvas.pack()

homePage = tk.Frame(root, bg = '#A7CAB1', bd = 5)
homePage.place(relx = 0.5, rely = 0.5, relwidth = 0.75, relheight = 0.1, anchor = 'n')

title = Label(canvas, text = "MY VAC APP", font = ('Courier',60,"bold"),bg = '#310A31',fg = '#A7CAB1')
title.pack()
title.place(relx = 0.5, rely =0.1, anchor = 'n')

civilian = Button(homePage, text = "Civilian Access", background = "#847996", fg = "#310A31",font = 50, command = lambda: get_civPage())
civilian.pack(expand = True, fill = BOTH)

government = Button(homePage, text = "Government Access", background = "#847996", fg = "#310A31",font = 50, command = lambda: get_govPage())
government.pack(expand = True, fill = BOTH)


# currently just sample data/maps/etc. ---> want to use API's to access data in real time

def vacRecPage():   #civilian function
    vacRecPage = tk.Frame(root,bd=10, bg = "#A7CAB1")
    vacRecPage.pack()
    vacRecPage.place(relx = 0.5, rely = 0, width = 600, height = 800, anchor = 'n')
    vrp = tk.Label(vacRecPage, text = "Vaccination Record Page", font = ('Courier', 16), anchor = 'nw', justify = 'left', bd = 4)
    vrp.place(relwidth = 1, relheight = 1)

    rec1 = tk.Label(vacRecPage, text = "    USER    |    VACCINE    |    DATE    ", font = ('Courier', 14,"bold"), anchor = 'nw', justify = 'left', bd = 4)
    rec1.place(x= 50, y = 60)

    rec2 = tk.Label(vacRecPage, text = "    SALLY   |    COVID-19   |  11/22/19  ", font = ('Courier', 14,), anchor = 'nw', justify = 'left', bd = 4)
    rec2.place(x= 50, y = 120)

    rec3 = tk.Label(vacRecPage, text = "     BOB    |   INFLUENZA   |   1/22/23  ", font = ('Courier', 14,), anchor = 'nw', justify = 'left', bd = 4)
    rec3.place(x= 50, y = 150)

    rec3 = tk.Label(vacRecPage, text = "   TIMMY    |    COVID-19   |   1/22/23  ", font = ('Courier', 14,), anchor = 'nw', justify = 'left', bd = 4)
    rec3.place(x= 50, y = 180)


    #home button
    home = tk.Button(vacRecPage, text = "MENU", width = 6, font = ('Courier',12), command = lambda: get_civPage())
    home.place(x = 500, y = 4)

def heatMapPage():   #gov function
    heatMapPage = tk.Frame(root, bd = 10, bg = "#A7CAB1")
    heatMapPage.pack()
    heatMapPage.place(relx = 0.5, rely = 0, width = 600, height = 800, anchor = 'n')
    hmp = tk.Label(heatMapPage, text = "Vaccination Rate Map", font = ('Courier', 16), anchor = 'nw', justify = 'left', bd = 4)
    hmp.place(relwidth = 1, relheight = 1)

    #google maps widget
    map_widget = TkinterMapView(root, width = 550,height = 700)
    map_widget.place(x=30,y=50)

    #google url + setting starting position
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    map_widget.set_address("Dallas")

    #making polygons
    poly1 = map_widget.set_polygon([(32.808044656335774, -96.7853861301659), 
                                    (32.82319765289922, -96.78040407656113),
                                    (32.8383480649438, -96.75501932724151),
                                    (32.818811524920015, -96.7469531452147),
                                    (32.80605064862415, -96.72488976496496),
                                    (32.79368680241073, -96.74339453549702),
                                    (32.78331579928026, -96.73105802180896),
                                    (32.785509766171955, -96.74719038586257),
                                    (32.7783293096639, -96.7469531452147)], 
                                    fill_color = "red", outline_color = "red", border_width = 3)
    poly2 = map_widget.set_polygon([(32.832965978021214, -96.77043996962244), 
                                    (32.85050639423383, -96.77447306063584),
                                    (32.83037448634683, -96.82120946826167),
                                    (32.810636799656166, -96.82310739175153),
                                    (32.82598871266557, -96.78918197910943)], 
                                    fill_color = "orange", outline_color = "orange", border_width = 3)
    poly3 = map_widget.set_polygon([(32.82917838766132, -96.82073498527306), 
                                    (32.809041643590504, -96.82192118851229),
                                    (32.82698549840765, -96.78847025716587),
                                    (32.81821339995486, -96.78609785068741),
                                    (32.78750423474753, -96.82642876082137),
                                    (32.80126484778003, -96.83188529572186),
                                    (32.79508280680791, -96.84683145653622),
                                    (32.80704765824627, -96.86509898642042),
                                    (32.83017513760397, -96.8209722259209)], 
                                    fill_color = "green", outline_color = "green", border_width = 3)
    poly4 = map_widget.set_polygon([(32.809041643590504, -96.78680957263096), 
                                    (32.77952609283424, -96.84113768098788),
                                    (32.803059553356036, -96.851813510141),
                                    (32.787703679128036, -96.87221620585584),
                                    (32.75000074772744, -96.86154037670272),
                                    (32.765762116581485, -96.81338052518981),
                                    (32.7478059054969, -96.8057888244587),
                                    (32.77852877478895, -96.78348820356109)], 
                                    fill_color = "yellow", outline_color = "yellow", border_width = 3)
    poly5 = map_widget.set_polygon([(32.80664885580925, -96.78752129457449), 
                                    (32.766161102369594, -96.78206475967401),
                                    (32.764764644287865, -96.7562055290587),
                                    (32.761971662409444, -96.73888696176589),
                                    (32.79189190781144, -96.7683048020989)], 
                                    fill_color = "green", outline_color = "green", border_width = 3)

    #home button
    home = tk.Button(heatMapPage, text = "MENU", width = 6, font = ('Courier',12), command = lambda: get_govPage())
    home.place(x = 500, y = 4)

def vacMapPage():     #civilian function
    #original page
    vacMapPage = tk.Frame(root, bd = 10, bg = "#A7CAB1")
    vacMapPage.pack()
    vacMapPage.place(relx = 0.5, rely = 0, width = 600, height = 800, anchor = 'n')
    
    #title
    vmp = tk.Label(vacMapPage, text = "Vaccination Site Map", font = ('Courier', 16), anchor = 'nw', justify = 'left', bd = 4)
    vmp.place(relwidth = 1, relheight = 1)
    
    #google maps widget
    map_widget = TkinterMapView(root, width = 550,height = 500)
    map_widget.place(x=30,y=50)

    #google url + setting starting position
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

    #markers
    marker1 = map_widget.set_address("8335 Westchester Dr, Dallas, TX 75225", marker=True)
    marker1.set_text("1) CVS Pharmacy")

    marker2 = map_widget.set_address("3414 Milton Ave, Dallas, TX 75205", marker=True)
    marker2.set_text("2) Citra Urgent Care")

    marker3 = map_widget.set_address("10455 N Central Expy, Dallas, TX 75231",marker=True)
    marker3.set_text("3) Tom Thumb Pharmacy")

    ursuline = map_widget.set_address("4900 Walnut Hill Ln, Dallas, TX 75229",marker=True)
    ursuline.set_text("Ursuline Academy")

    #location titles @ bottom
    location1 = tk.Label(vacMapPage, text = "1) CVS Pharmacy", font = ('Courier', 14,"bold"), anchor = 'nw', justify = 'left', bd = 4)
    location1.place(x= 17, y = 550)
    location1address = tk.Label(vacMapPage, text = "8355 Westchester Dr, Dallas, TX 75225", font = ('Courier', 14), anchor = 'nw', justify = 'left', bd = 4)
    location1address.place(x= 17, y = 575)

    location2 = tk.Label(vacMapPage, text = "2) Citra Urgent Care", font = ('Courier', 14,"bold"), anchor = 'nw', justify = 'left', bd = 4)
    location2.place(x= 17, y = 615)
    location2address = tk.Label(vacMapPage, text = "3414 Milton Ave, Dallas, TX 75205", font = ('Courier', 14), anchor = 'nw', justify = 'left', bd = 4)
    location2address.place(x= 17, y = 640)

    location3 = tk.Label(vacMapPage, text = "3) Tom Thumb Pharmacy", font = ('Courier', 14,"bold"), anchor = 'nw', justify = 'left', bd = 4)
    location3.place(x= 17, y = 680)
    location3address = tk.Label(vacMapPage, text = "10455 N Central Expy, Dallas, TX 75231", font = ('Courier', 14), anchor = 'nw', justify = 'left', bd = 4)
    location3address.place(x= 17, y = 705)

    #home button
    home = tk.Button(vacMapPage, text = "MENU", width = 6, font = ('Courier',12), command = lambda: get_civPage())
    home.place(x = 500, y = 4)

def statsPage():    #gov function
    statsPage = tk.Frame(root, bd = 10, bg = "#A7CAB1")
    statsPage.pack()
    statsPage.place(relx = 0.5, rely = 0, width = 600, height = 800, anchor = 'n')
    sp = tk.Label(statsPage, text = "Vaccination Levels & Cases", font = ('Courier', 16), anchor = 'nw', justify = 'left', bd = 4)
    sp.place(relwidth = 1, relheight = 1)

    rec1 = tk.Label(statsPage, text = "    REGION   |    VACCINE    |   PERCENT   ", font = ('Courier', 14,"bold"), anchor = 'nw', justify = 'left', bd = 4)
    rec1.place(x= 50, y = 60)

    rec2 = tk.Label(statsPage, text = "  SOUTHWEST  |    COVID-19   |     72%     ", font = ('Courier', 14,), anchor = 'nw', justify = 'left', bd = 4)
    rec2.place(x= 50, y = 120)

    rec3 = tk.Label(statsPage, text = "  NORTHEAST  |    COVID-19   |     98%     ", font = ('Courier', 14,), anchor = 'nw', justify = 'left', bd = 4)
    rec3.place(x= 50, y = 150)

    rec3 = tk.Label(statsPage, text = "  SOUTHWEST  |   INFLUENZA   |     18%     ", font = ('Courier', 14,), anchor = 'nw', justify = 'left', bd = 4)
    rec3.place(x= 50, y = 180)

    rec4 = tk.Label(statsPage, text = "  NORTHEAST  |   INFLUENZA   |     23%     ", font = ('Courier', 14,), anchor = 'nw', justify = 'left', bd = 4)
    rec4.place(x= 50, y = 210)

    #home button
    home = tk.Button(statsPage, text = "MENU", width = 6, font = ('Courier',12), command = lambda: get_govPage())
    home.place(x = 500, y = 4)


###########################

# main page w/ 4 options
def get_civPage():
    # use frame to fill with sign picture of letter
    civPage = tk.Frame(root, bd = 10, bg = "#88B7B5")
    civPage.pack()
    civPage.place(relx = 0.5, rely = 0, width = 600, height = 800, anchor = 'n')

    title = Label(civPage, text = "Hello User!", font = ('Courier',50,"bold"),bg = '#88B7B5',fg = '#310A31')
    title.pack()
    title.place(relx = 0.5, rely =0.2, anchor = 'n')
   
    vacRecords = Button(civPage, text = "Vaccination Records", background = "#847996", fg = "#310A31",font = 20, command = lambda: vacRecPage())
    vacRecords.pack()
    vacRecords.place(relx = 0.5, rely = 0.60, width = 315, height = 70, anchor = 'n')

    vacMap = Button(civPage, text = "Vaccination Sites Nearby", background = "#847996", fg = "#310A31",font = 20, command = lambda: vacMapPage())
    vacMap.pack()
    vacMap.place(relx = 0.5, rely = 0.70, width = 315, height = 70, anchor = 'n')

def get_govPage():
    # use frame to fill with sign picture of letter
    govPage = tk.Frame(root, bd = 10, bg = "#88B7B5")
    govPage.pack()
    govPage.place(relx = 0.5, rely = 0, width = 600, height = 800, anchor = 'n')

    title = Label(govPage, text = "Welcome", font = ('Courier',50,"bold"),bg = '#88B7B5',fg = '#310A31')
    title.pack()
    title.place(relx = 0.5, rely =0.2, anchor = 'n')
   
    # gov't acct. extra
    heatMap = Button(govPage, text = "Area Vaccination Levels & Cases", background = "#847996", fg = "#310A31",font = 20, command = lambda: statsPage())
    heatMap.pack()
    heatMap.place(relx = 0.5, rely = 0.60, width = 315, height = 70, anchor = 'n')

    # gov't acct. extra
    stats = Button(govPage, text = "Area Vaccination Rates Map", background = "#847996", fg = "#310A31",font = 20, command = lambda: heatMapPage())
    stats.pack()
    stats.place(relx = 0.5, rely = 0.70, width = 315, height = 70, anchor = 'n')

    root.mainloop()



root.mainloop()


