import tkinter
import tkinter.messagebox
from tkinter import filedialog
from tkinter import *
import pandas as pd

from Main import GPSVis
import os

def Open_Dataset(Menu, dropVar, index=None):
    # This function will open file explorer
    # making the filename global allows for it to be called later down the line
    global data_set
    data_set = filedialog.askopenfilename()
    global UID
    UID=pd.read_csv(data_set)
    UID=UID['iPhoneUID'].unique().tolist()
    print(type(UID))
    #for id in UID:
        #print(id)
    drop_menu = Menu["menu"]
    #drop_menu.delete(0, "end")
    for string in UID:
        drop_menu.add_command(label=string,
                              command= lambda value=string:
                                dropVar.set(string))
    print(dropVar)
    for id in dropVar:
       print(id)

        #for loop, adds value to drop menu
        #command is value = string

def Open_Map():
    global Map
    Map = filedialog.askopenfilename()
def about_us():
    tkinter.messagebox.showinfo('About Us', 'This is a program made in Python by Alex Hulme for his Final Year Project')
def help_guide():
    os.startfile(r"C:\Users\AlexT\OneDrive\Desktop\Python Project New\User_Guide.pdf")
def option_changed(*args):
    print("the user chose value {}".format(dropVar.get()))

def GPS_Visualisation(entry1,entry2,entry3,entry4):
    vis = GPSVis(data_path=data_set,  # DATASET WITH COORDINATES
                 map_path=Map,  # Map Image from Open Street Maps
                 points= (float(entry1),float(entry2),float(entry3),float(entry4)))
    # Coordinates from Open Street Maps
    # Relates to the image so it can be written out

    vis.create_image(color=(0, 0, 255), width=3)
    # Sets the colour of the visualisation on map
    vis.plot_map(output='save')

    # Starts the tkinter GUI
root = Tk()

# Creating a menu drop down bar
menubar = Menu(root)
root.config(menu=menubar)
# Creates the sub menu
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New")
subMenu.add_command(label="Exit", command=root.destroy)

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About us", command=about_us)
subMenu.add_command(label="User Guide", command=help_guide)

root.title("PERSEC Application")
# Titles the frame
root.geometry('400x400')
# Sets the Height and Width
text = Label(root, text='Welcome to the Personal Security Application')
text.pack()
dropVar = tkinter.StringVar(root)
dropVar.trace("w", option_changed)
options_list = ["select a file"]
drop_menu = tkinter.OptionMenu(root, dropVar, ())
drop_menu.pack()
btn = Button(root, text="Select Dataset File", command=lambda: Open_Dataset(drop_menu, dropVar))
btn.pack()
btn2 = Button(root, text="Select Map File", command=Open_Map)
btn2.pack()

# Allows user to input Map latitude and longitude
entry1 = tkinter.DoubleVar()
entry2 = tkinter.DoubleVar()
entry3 = tkinter.DoubleVar()
entry4 = tkinter.DoubleVar()

var1 = tkinter.Label(root, text="Top Left Latitude")
var1.pack()
entry1 = tkinter.Entry(root, textvariable=entry1)
entry1.pack()
var2 = tkinter.Label(root, text="Top Left Longitude")
var2.pack()
entry2 = tkinter.Entry(root, textvariable=entry2)
entry2.pack()
var3 = tkinter.Label(root, text="Bottom Right Latitude")
var3.pack()
entry3 = tkinter.Entry(root, textvariable=entry3)
entry3.pack()
var4 = tkinter.Label(root, text="Bottom Right Longitude")
var4.pack()
entry4 = tkinter.Entry(root, textvariable=entry4)
entry4.pack()

# Add an error check later (int check, prescence check)
# select present --- Dialog box
submit = Button(root, text="Submit",
                command=lambda: GPS_Visualisation(entry1.get(), entry2.get(), entry3.get(), entry4.get()))
submit.pack()



root.mainloop()
# Infinite loop created to keep GUI open
# Keep at the bottom or it won't appear in GUI loop

