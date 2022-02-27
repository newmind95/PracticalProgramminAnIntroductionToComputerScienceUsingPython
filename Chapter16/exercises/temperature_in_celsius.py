import tkinter

class ConvertToCelsius:
    """Create the GUI."""
    def __init__(self, parent):
        self.parent = parent
        self.frame = tkinter.Frame(self.parent).pack()

        self.out_data = tkinter.StringVar()
        self.temp_data = tkinter.DoubleVar()

        tkinter.Label(self.frame, text='Temperature in Fahrenheit').pack()
        self.entry = tkinter.Entry(self.frame, textvar=self.temp_data)
        self.entry.pack()

        self.label = tkinter.Label(self.frame, textvar=self.out_data)
        self.label.pack()

        self.button = tkinter.Button(self.frame, text='Convert',
                                     command=lambda: 
                                         self.convert_to_fahrenheit(
                                             self.out_data, self.temp_data))
        self.button.pack()

        self.button_quit = tkinter.Button(self.frame, text='Quit',
                                          command=lambda:
                                          self.quit_button())
        self.button_quit.pack()


    def convert_to_fahrenheit(self, out_data, temp_data):
        """Convert from Celsius to Fahrenheit."""
        f = temp_data.get()
        result = out_data.set((f-32) * 5/9)
        return result


    def quit_button(self):
        """Handles quit button."""
        self.parent.destroy()

          
if __name__ == '__main__':
    window = tkinter.Tk()
    myapp = ConvertToCelsius(window)
    window.mainloop()
