#!/usr/bin/env python3
import tkinter as tk
import random

class GuessHex:
    def __init__(self, parent):
        self.parent = parent
        parent.title("GuessHex")
        parent.minsize(660, 250)
        parent.resizable(False, False)
        self.color_label = tk.Label(parent, text="Which colour matches the Hex code below?")
        self.color_label.place(x=190,y=135)
        self.hex_label = tk.Label(parent, text="")
        self.hex_label.place(x=285,y=170)
        self.winlose = tk.Label(parent, text="")
        self.winlose.place(x=220, y=200)
        self.canvas = tk.Canvas(parent, width=600,height=80)
        self.canvas.place(x=30,y=30)
        self.col = {}
        self.color = {}
        for i in range(0,6):
            self.color['col'+str(i)] = self.randomhex()
            self.col['col'+str(i)] = self.canvas.create_oval((15+(i*100)), 20, (75+(i*100)), 80, width=0, fill=self.color['col'+str(i)], tags="col"+str(i))
            self.canvas.tag_bind("col"+str(i), "<Button-1>", self.checkwin)
        self.rwin = random.randint(0,5)
        self.hex_label.configure(text=self.color['col'+str(self.rwin)])

    def checkwin(self, event):
        self.canvas.config(state = 'disabled')
        if self.color["col"+str((event.widget.find_closest(event.x, event.y)[0]-1))] == self.hex_label.cget("text"):
            self.winlose.configure(text="Congratulations. You got it right!")
        else:
            self.winlose.configure(text="Sorry. Better luck next time!")
            self.canvas.itemconfig(self.col['col'+str(self.rwin)], width=2, outline='red')
        self.parent.after(2000, self.regenerate)

    def regenerate(self):
        for i in range(0,6):
                self.color['col'+str(i)] = self.randomhex()
                self.canvas.itemconfig(self.col['col'+str(i)],fill=self.color['col'+str(i)],width=0)
        self.rwin = random.randint(0,5)
        self.hex_label.configure(text=self.color['col'+str(self.rwin)])
        self.winlose.configure(text="")
        self.canvas.config(state = 'normal')

    def randomhex(self):
        r = lambda: random.randint(0,255)
        return '#%02X%02X%02X' % (r(),r(),r())


def main():
    root = tk.Tk()
    thegui = GuessHex(root)
    root.mainloop()

if __name__ == "__main__":
    main()
