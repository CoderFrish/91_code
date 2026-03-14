from turtle import *

pen = Pen()

"""
来自Frish写的神秘海龟迪克
"""

def draw():
    pen.circle(40)
    pen.teleport(x = 40)
    pen.left(90)
    pen.forward(300)
    pen.circle(-40)
    pen.teleport(x = 120)
    pen.right(180)
    pen.forward(300)
    pen.teleport(y = 40)
    pen.circle(40)
    pen.right(90)
    pen.teleport(y = 0)
    pen.forward(80)

    mainloop()

if __name__ == '__main__':
    draw()
