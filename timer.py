from threading import Timer

class MyTimer:
    def __init__(self, c, f, t):
        self.c = c
        self.f = f
        self.t = t
        self.start()

    def start(self):
        timer = Timer(self.t, self.callback)
        timer.start()

    def callback(self):
        self.f(self.c)
        self.start()
