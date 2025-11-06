from turtle import *
screensize(3000, 4000)
tracer(0)
m = 10
down()
for i in range(4):
    fd(30*m)
    rt(90)
    fd(48*m)
    rt(90)

up()

fd(27*m)
rt(90)
fd(24*m)
lt(90)

down()

for i in range(4):
    fd(29*m)
    rt(90)
    bk(18*m)
    rt(90)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(3, "red")


update()
done()
