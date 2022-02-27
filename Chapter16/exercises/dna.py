import tkinter
class DNA:
    """Create the GUI."""
    def __init__(self, parent):
        self.parent = parent
        self.frame = tkinter.Frame(parent)
        self.frame.pack()
        
        self.result = tkinter.StringVar()
        self.result.set('Num As: 0 Num Ts: 0 Num Cs: 0 Num Gs: 0')
        
        self.text = tkinter.Text(self.frame)
        self.text.pack()
        
        self.button = tkinter.Button(self.parent, text='Count',
                                     command=self.counter)
        self.button.pack()
        self.label = tkinter.Label(self.parent, textvariable=self.result)
        self.label.pack()
        
    def onclick(self):
        print('Button click')
        
    
    def counter(self):
        data = self.text.get('0.0', tkinter.END)
        count_a, count_t, count_c, count_g = 0, 0, 0, 0
        for x in data:
            if x == 'A':
                count_a += 1
            elif x == 'T':
                count_t += 1
            elif x == 'C':
                count_c += 1
            elif x == 'G':
                count_g += 1
        return self.result.set(f'Num As: {str(count_a)} Num Ts: {str(count_t)} ' \
                               f'Num Cs: {str(count_c)} Num Gs: {str(count_g)}')
        
        
if __name__=='__main__':
    window = tkinter.Tk()
    myapp = DNA(window)
    window.mainloop()