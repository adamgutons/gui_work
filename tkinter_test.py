#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      adam.gutonski
#
# Created:     05/02/2019
# Copyright:   (c) adam.gutonski 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Tkinter import *
import os
from subprocess import call

class App():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('250x150')
        self.root.title("File transfer tool")
        self.label_1 = Label(self.root, text='Enter a pathway from where data \n will be pulled')
        self.server_path_entry = Entry(self.root)
        self.label_2 = Label(self.root, text='Enter a local path to store the data')
        self.local_path_entry = Entry(self.root)
        self.move_files = Button(self.root, text='Move Files', command=self.move_stuff)
        self.label_1.pack()
        self.server_path_entry.pack()
        self.label_2.pack()
        self.local_path_entry.pack()
        self.move_files.pack()
        self.root.mainloop()

    def print_stuff(self):
        to_print = self.server_path_entry.get()
        print to_print
        print os.path.exists(to_print)

    def move_stuff(self):
        server_path = self.server_path_entry.get()
        local_path = self.local_path_entry.get()
        call(["robocopy", server_path, local_path, '/s', '/log:C:\\Geo_Training\\logfile.txt'])

app = App()

