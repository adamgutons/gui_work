#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:  Attemtping to make a GUI tool for use when transferring large amnts
#           of data across networks, specifically when moving from the
#           isilon1nmjml server to local path
#
# Author:      adam.gutonski
#
# Created:     06/02/2019
# Copyright:   (c) adam.gutonski 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Tkinter import *

import os
import subprocess
from datetime import datetime
import robo_test
import threading

"""
### This method used for initial testing ###
def print_stuff():
    start = datetime.now()
    to_print = server_path_entry.get()
    label_3.config(text="Button clicked...")
    print to_print
    print os.path.exists(to_print)
    end = datetime.now() - start
    label_3.config(text="Time taken: %s" % end)
"""
# this method gathers the user entered paths and plugs into the list of
# args that will be used in the subprocess call.  The exception catches output
# from the stdin call, which is the robocopy status output.  Redirect the output
# to the GUI label_4
def robo_this():
    label_3.config(text="Beginning file transfer...this could take a few minutes\nPlease do not close the window until transfer is complete.")
    server_path = server_path_entry.get()
    local_path = local_path_entry.get()
    try:
        args = ["robocopy", server_path, local_path, '/np', '/ns', '/nc', '/nfl', '/ndl', '/s']
        subprocess.check_output(args)
    except subprocess.CalledProcessError, e:
        for n in e.output:
            if n == '\n':
                read_out = e.output.replace(n, '')
        #print read_out
        label_3.config(text="File transfer complete!")
        label_4.config(text=read_out)

def start():
    t = threading.Thread(target=robo_this)
    t.start()


root = Tk()
#root.geometry('520x150')
root.title("Large File Transfer Tool")
label_1 = Label(root, text='Server path from where data will be pulled:')
label_1.grid(padx=10, column=0, row=0, sticky='W')
server_path_entry = Entry(root)
server_path_entry.config(width=50)
server_path_entry.grid(padx=(10,10), column=1, row=0, sticky='E')
label_2 = Label(root, text='Local path to store the data:')
label_2.grid(padx=10, column=0, row=1, sticky='W')
local_path_entry = Entry(root)
local_path_entry.config(width=50)
local_path_entry.grid(padx=(10,10), column=1, row=1, sticky='E')
move_files = Button(root, text='Move Files', command=start)
move_files.grid(padx=10, pady=5, columnspan=2, row=2, sticky='NSEW')
label_3 = Label(root, text="")
label_3.grid(columnspan=2, row=3)
label_4 = Label(root, text="")
label_4.grid(columnspan=2, row=4)
#label_1.pack()
#server_path_entry.pack()
#label_2.pack()
#local_path_entry.pack()
#move_files.pack()
#label_3.pack()
root.mainloop()



