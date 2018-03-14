import Tkinter as Tk
from timer import SimpleTimer 
from random import randint
import sys

dt = 0.001
v = 1
canvas_h = 700.
canvas_w = 700.

if len(sys.argv) > 1:
    dt = float(int(sys.argv[1]) /10.)
    v = int(sys.argv[2])
else:
    print "Try with arguments: 'python random_walk.py 10 10' for dt = 1.0, len = 10"

    
print dt, v    
n = 0 # number of steps
sx = 0. # sum of dx
sy = 0. # sum of dy

x = x0 = canvas_h /2
y = y0 = canvas_w /2
x2 = x
y2 = y
root = Tk.Tk()
c = Tk.Canvas(root, width=canvas_w, height=canvas_h)

vertical = c.create_line(x, 0, x, canvas_h, width=1, fill='gray')
horizontal = c.create_line(0, y, canvas_w, y, width=1, fill='gray')
c.pack()
l = None
axis = 'x'

# labels

sv = Tk.StringVar()
label = Tk.Label(root, textvariable=sv, anchor='w', width=60, font=("Consolas", 16))
label.pack()


def draw():
    global c,x,y,l,ld,sv,n,v,axis

    # random value
    
    r = randint(0, 1)
    if r == 0:
        d = -v
    else:
        d = v

    # previous step line
    
    if l:
        c.itemconfig(l, fill='blue')
        c.itemconfig(l, width=1)
        c.delete(ld)

    # draw the step
    
    if axis == 'x':
        l = c.create_line(x, y, x + d, y    , width=2, fill='red')
        x += d
        axis = 'y'
    else:
        l = c.create_line(x, y, x    , y + d, width=2, fill='red')
        y += d
        axis = 'x'
        
    ld = c.create_oval(x-2, y-2, x+2, y+2, fill='yellow') 

    # calculate the average
    n += 1
    sv.set(str(n) + ': ' + "{:6.4f}".format((x-x0)/n) + ' / ' + "{:6.4f}".format((y-y0)/n) + ',   x = ' + "{:3.0f}".format(x-x0) + ', y = ' + "{:3.0f}".format(y-y0)) 


t = SimpleTimer(draw, dt)

root.mainloop()
