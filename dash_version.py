import Tkinter as Tk
import timer 
import random

fr=Tk.Tk()

cw = 500
ch = 500
x = cw/2
y = ch/2
x2 = x
y2 = y

c=Tk.Canvas(fr, width=cw, height=ch)
c.pack()


def draw():
    global c, x, y, x2, y2

    d = random.randint(1,4) #direction
    if d == 1: # move y + 1
        x2 = x
        y2 = y+10
    if d == 2: # move x + 1
        x2=x+10
        y2=y
    if d == 3: # move y -1
        x2=x
        y2=y-10
    if d == 4: # move x - 1
        x2=x-10
        y2=y

    l = c.create_line(x, y, x2, y2, width=2, fill='red')
    
    x = x2
    y = y2

t=timer.SimpleTimer(draw, 0.1)


fr.mainloop()
