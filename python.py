from turtle import*
import colorsys
bgcolor('black')
tracer(500)

def draw():
    h=0
    for i in range(500):
        c = colorsys.hsv_to_rgb(h,1,1)
        h +=0.5
        up()
        goto(0,0)
        down()
        color('black')
        fillcolor (c)
        begin_fill()
        rt (70)
        circle(i,10)
        fd (180)
        fd(i)
        lt(19)
        for j in range(109):
            fd(i)
            circle(j,180,steps=2)
        end_fill()
draw()
don()
