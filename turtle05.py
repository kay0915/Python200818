import turtle
tur = turtle.Turtle()
cir = int(input('數字:'))
for i in range(cir):
    tur.forward(30)
    tur.left(360/cir)
turtle.done()