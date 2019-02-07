#-------------------------------------------------------------------------------
#--------> Testing alternate subprocess calls to ROBOCOPY
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
import tkMessageBox
import threading

# this method gathers the user entered paths and plugs into the list of
# args that will be used in the subprocess call.  The exception catches output
# from the stdin call, which is the robocopy status output.  Redirect the output
# to the GUI label_4
def robo_this():
    start = datetime.now()
    server_path = server_path_entry.get()
    local_path = local_path_entry.get()
    try:
        args = ["robocopy", server_path, local_path, '/s']
        p = subprocess.call(args)
        if p:
            end = datetime.now() - start
            label_3.config(text="File transfer complete.\nTime taken: %s" % end)
    except:
        label_4.config(text="Something went wrong, please check paths and try again")

def move_stuff():
    label_3.config(text="Beginning file transfer, this can take several minutes.\nPlease do not close the tool until transfer is complete.")
    t = threading.Thread(target=robo_this)
    flag = t.start()
    #print flag
    #if not flag:
    #    label_3.config(text="Time taken: %s" % end)
    #    label_4.config(text="File transfer complete!")

root = Tk()
#root.geometry('520x150')
root.title("TKINTER_TEST_3")
label_1 = Label(root, text='Enter a file source path:')
label_1.grid(padx=(10,5), column=0, row=0, sticky='W')
server_path_entry = Entry(root)
server_path_entry.config(width=50)
server_path_entry.grid(padx=(10,10), column=1, row=0, sticky='E')
label_2 = Label(root, text='Enter a file destination path:')
label_2.grid(padx=(10,5), column=0, row=1, sticky='W')
local_path_entry = Entry(root)
local_path_entry.config(width=50)
local_path_entry.grid(padx=(10,10), column=1, row=1, sticky='E')
move_files = Button(root, text='Move Files', command=move_stuff)
move_files.grid(padx=10, pady=5, columnspan=2, row=2, sticky='NSEW')
label_3 = Label(root, text="")
label_3.grid(columnspan=2, row=3)
label_4 = Label(root, text="")
label_4.grid(columnspan=2, row=4)

root.mainloop()



