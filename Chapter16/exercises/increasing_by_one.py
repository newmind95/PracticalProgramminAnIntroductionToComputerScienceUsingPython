import tkinter
"""Write a GUI application with a single button.
Initially the button is labeled
0, but each time it is clicked, the value on the button increases by 1."""
class Increase:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tkinter.Frame(parent)
        self.frame.pack()
        
        # Create the Model.
        self.counter = tkinter.IntVar()
        self.counter.set(0)
        
        # Label displaying current state.
        self.label = tkinter.Label(self.frame, textvariable=self.counter)
        self.label.pack()
        
        # Button to control the application
        self.up = tkinter.Button(self.frame, text='Up',
                                 command=self.up_click)
        self.up.pack()
        
        
    def up_click(self):
        """Handle click on 'up' button."""
        self.counter.set(self.counter.get()+1)
        
        
if __name__=='__main__':
    window = tkinter.Tk()
    myapp = Increase(window)
    window.mainloop()