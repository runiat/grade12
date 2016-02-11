# from http://sebsauvage.net/python/gui/#import
#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import tkinter

# SimpleApp_tk is a tkinter.Tk. ( parent-child relationship)
class SimpleApp_tk(tkinter.Tk):

    #constructor
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent

        # I think this is bad form
        self.initialize()

    # initialize here. create any buttons, windows, ect
    def initialize(self):
        # use tkinter's grid manager
        self.grid()

        # create the widget, then add it.
        # This creates a text field where you can type in some information
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        # add event handlers
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set("Enter text here.")

        # add a button and an event handler for it
        button = tkinter.Button(self,text="Click Button !",command=self.OnButtonClick)
        button.grid(column=1,row=0)

      # create a label, and change the label when an event happens
        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.labelVariable, anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set("Hello !")

        # resize the window if it is resized. ( no fixed by pixels)
        self.grid_columnconfigure(0,weight=1)
        # only rezise horizontally. not vertically
        self.resizable(True,False)

    def OnButtonClick(self):
        self.labelVariable.set( self.entryVariable.get()+" (You clicked the button)")

    def OnPressEnter(self,event):
        self.labelVariable.set(self.entryVariable.get()+"You pressed enter !")


# create a main method if it is run from command line
if __name__ == "__main__":
    app = SimpleApp_tk(None)
    app.title('my application')
    app.mainloop()
