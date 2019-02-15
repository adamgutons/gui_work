#-------------------------------------------------------------------------------
#--------> Testing alternate subprocess calls to ROBOCOPY
# Purpose:  Attemtping to make a GUI tool for use when transferring large amnts
#           of data across networks, specifically when moving from the
#           isilon1nmjml server to local path
#
#           User can enter a local/server path source and a local/server path
#           desination to move files back and forth at discretion
# Author:      adam.gutonski
#
# Created:     February 15, 2019
# Copyright:   (c) adam.gutonski 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Tkinter import *   #----> Import tkinter module
import subprocess       #----> Import subprocess module
import threading        #----> Import threading, used to avoid GUI lockup
                        #----> when making a subprocess call
import sys
import os
# this method gathers the user entered paths and plugs into the list of
# args that will be used in the subprocess call.  The exception catches output
# from the stdin call, which is the robocopy status output.  Redirect the output
# to the GUI label_4
def robo_this():
    server_path = server_path_entry.get()
    local_path = local_path_entry.get()
    geoDB = os.path.basename(server_path)
    true_local = local_path + os.sep + geoDB
    if not os.path.exists(true_local):
        os.mkdir(true_local)
    if os.path.exists(server_path) and os.path.exists(true_local):
        try:
            label_3.config(text="Beginning file transfer, this can take several minutes.\nPlease do not close the tool until transfer is complete.")
            args = ["robocopy", server_path, true_local, '/s']
            p = subprocess.call(args)
            sys.stdout.flush()
            if p:
                label_3.config(text='File transfer complete...')
        except:
           label_3.config(text='Something went wrong...please check source and destination file paths')

def move_stuff():
    t = threading.Thread(target=robo_this)
    flag = t.start()

root = Tk()
root.title("File Transfer Tool")
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

root.mainloop()



