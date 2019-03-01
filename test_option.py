from Tkinter import *

def do_stuff():
	text = selected.get()
	label.config(text=text)

root = Tk()

root.title("Option menu")
label = Label(root, text='')
but = Button(root, text='click', command=do_stuff)


l = ["option1", "option2", "option3"]


selected = StringVar()
selected.set(l[0])

menu = OptionMenu(root, selected, "option1", "option2", "option3")

label.config(width=50)
menu.config(width=50)

menu.grid()
label.grid(column=0, row=2, sticky='NSEW')
but.grid(column=0, row=3, sticky='NSEW')

root.mainloop()