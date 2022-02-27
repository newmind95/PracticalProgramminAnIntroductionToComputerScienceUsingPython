import tkinter
"""Write a GUI application with a button labeled “Goodbye.” When the button
    is clicked, the window closes."""
class GoodBye:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tkinter.Frame(parent)
        self.frame.pack()
        
        self.button = tkinter.Button(self.frame, text='Goodbye',
                                     command=self.goodbye_click)
        self.button.pack()
        
    def goodbye_click(self):
        """Handle click on 'Goodbye' button."""
        self.parent.destroy()
        
if __name__=='__main__':
    window = tkinter.Tk()
    myapp = GoodBye(window)
    window.mainloop()