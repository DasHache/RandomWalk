import Tkinter as Tk
from timer import MyTimer 
from random import randint

dt = 0.1
canvas_h = 700.
canvas_w = 700.

x = canvas_h /2
y = canvas_w /2
x2 = x
y2 = y
root = Tk.Tk()
c = Tk.Canvas(root, width=canvas_w, height=canvas_h)

vertical = c.create_line(x, 0, x, canvas_h, width=1, fill='gray')
horizontal = c.create_line(0, y, canvas_w, y, width=1, fill='gray')
c.pack()

l = None

def draw(c):
    global x,y,x2,y2,l,l_last
    dx = randint(-10,10)
    dy = randint(-10,10)
    x2 = x + dx
    y2 = y + dy

    if l:
        c.itemconfig(l, fill='blue')
        c.itemconfig(l, width=1)
        
    l = c.create_line(x, y, x2, y2, width=2, fill='red')
    x = x2
    y = y2



t = MyTimer(c, draw, dt)

root.mainloop()
