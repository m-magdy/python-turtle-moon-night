import turtle
from turtle import *

x=Turtle()

title("Fatma Farjallah.")

x.speed(0)

x.hideturtle()

#ciel 

x.color("#0e0e3f")
x.begin_fill()
x.goto(-1000,1000)
x.goto(1000,1000)
x.goto(1000,-1000)
x.goto(-1000,-1000)
x.goto(-1000,1000)
x.end_fill()

#moon
x.up()
x.goto(30,-120)
x.down()
x.color("#ffff00")
x.width(20)
x.begin_fill()
x.circle(150)
x.end_fill()
x.goto(-35,-100)
x.color("#0e0e3f")
x.begin_fill()
x.circle(136)
x.end_fill()

x.up()
x.goto(110,25)
x.down()
x.color("black","white")
x.width(3)
x.begin_fill()
x.circle(25)
x.end_fill()
x.up()
x.goto(118,40)
x.down()
x.color("black")
x.width(3)
x.begin_fill()
x.circle(11)
x.end_fill()
x.up()
x.goto(111,45)
x.down()
x.color("white")
x.width(3)
x.begin_fill()
x.circle(5)
x.end_fill()


x.up()
x.goto(180,25)
x.down()
x.color("black","white")
x.width(3)
x.begin_fill()
x.circle(30)
x.end_fill()
x.up()
x.goto(185,40)
x.down()
x.color("black")
x.width(3)
x.begin_fill()
x.circle(15)
x.end_fill()
x.up()
x.goto(175,48)
x.down()
x.color("white")
x.width(3)
x.begin_fill()
x.circle(6)
x.end_fill()

#mouth
x.up()
x.goto(140,-20)
x.down()
x.color("black")
x.width(3)
x.begin_fill()
x.circle(19)
x.end_fill()
x.up()
x.goto(140,-10)
x.down()
x.color("#ffff00")
x.width(3)
x.begin_fill()
x.circle(20)
x.end_fill()


#stars

x.up()
x.goto(280,230)
x.width(5)
x.down()
x.begin_fill()
x.color("#4d4dff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(200,200)
x.width(5)
x.down()
x.begin_fill()
x.color("#ff99ff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(120,260)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffb3d9")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(30,230)
x.width(5)
x.down()
x.begin_fill()
x.color("#99ff99")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(-50,260)
x.width(5)
x.down()
x.begin_fill()
x.color("#4d4dff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(-110,270)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffffff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(-190,230)
x.width(5)
x.down()
x.begin_fill()
x.color("#ff99ff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(-270,270)
x.width(5)
x.down()
x.begin_fill()
x.color("#99ff99")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(-310,220)
x.width(5)
x.down()
x.begin_fill()
x.color("#ff99ff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(280,150)
x.width(5)
x.down()
x.begin_fill()
x.color("#99ff99")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
#
x.up()
x.goto(200,100)
x.width(5)
x.down()
x.begin_fill()
x.color("#99ff99")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
'''
x.up()
x.goto(120,150)
x.width(5)
x.down()
x.begin_fill()
x.color("#ff0000")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
'''
x.up()
x.goto(30,100)
x.width(5)
x.down()
x.begin_fill()
x.color("#99ff99")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(-50,150)
x.width(5)
x.down()
x.begin_fill()
x.color("#4d4dff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(-110,160)
x.width(5)
x.down()
x.begin_fill()
x.color("#99ff99")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(-190,120)
x.width(5)
x.down()
x.begin_fill()
x.color("#bf80ff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(-250,180)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffb3ff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(-310,150)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffffff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(280,50)
x.width(5)
x.down()
x.begin_fill()
x.color("#4d4dff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(200,100)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffffff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
'''
x.up()
x.goto(120,50)
x.width(5)
x.down()
x.begin_fill()
x.color("#ff0000")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
'''
x.up()
x.goto(30,100)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffb3ff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(-50,50)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffffff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(-110,100)
x.width(5)
x.down()
x.begin_fill()
x.color("#4d4dff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(-190,40)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffb3ff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(-270,50)
x.width(5)
x.down()
x.begin_fill()
x.color("#4d4dff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(-310,100)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffffff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()



x.up()
x.goto(280,0)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffffff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(200,-50)
x.width(5)
x.down()
x.begin_fill()
x.color("#4d4dff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
'''
x.up()
x.goto(120,0)
x.width(5)
x.down()
x.begin_fill()
x.color("#ff0000")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
'''
x.up()
x.goto(30,5)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffffff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(-50,0)
x.width(5)
x.down()
x.begin_fill()
x.color("#4d4dff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(-110,10)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffffff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(-190,-70)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffffff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(-270,0)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffb3ff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(-310,-50)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffffff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()




x.up()
x.goto(280,-100)
x.width(5)
x.down()
x.begin_fill()
x.color("#b3ffb3")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(200,-150)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffb3ff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
'''
x.up()
x.goto(120,-80)
x.width(5)
x.down()
x.begin_fill()
x.color("#ff0000")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
'''
x.up()
x.goto(30,-150)
x.width(5)
x.down()
x.begin_fill()
x.color("#4d4dff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
'''
x.up()
x.goto(-50,-100)
x.width(5)
x.down()
x.begin_fill()
x.color("#ff0000")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
'''
x.up()
x.goto(-110,-150)
x.width(5)
x.down()
x.begin_fill()
x.color("#99ff99")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(-190,-140)
x.width(5)
x.down()
x.begin_fill()
x.color("#b3ffb3")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(-270,-100)
x.width(5)
x.down()
x.begin_fill()
x.color("#4d4dff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(-310,-150)
x.width(5)
x.down()
x.begin_fill()
x.color("#99ff99")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()



x.up()
x.goto(280,-150)
x.width(5)
x.down()
x.begin_fill()
x.color("#b3ffb3")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(200,-200)
x.width(5)
x.down()
x.begin_fill()
x.color("#4d4dff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(120,-150)
x.width(5)
x.down()
x.begin_fill()
x.color("#99ff99")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(30,-50)
x.width(5)
x.down()
x.begin_fill()
x.color("#4d4dff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(-50,-150)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffb3d9")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(-110,-50)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffb3d9")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(-190,-140)
x.width(5)
x.down()
x.begin_fill()
x.color("#99ff99")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(-270,-200)
x.width(5)
x.down()
x.begin_fill()
x.color("#4d4dff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(-310,-150)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffb3d9")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()




x.up()
x.goto(280,-250)
x.width(5)
x.down()
x.begin_fill()
x.color("#99ff99")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(200,-270)
x.width(5)
x.down()
x.begin_fill()
x.color("#4d4dff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(120,-250)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffb3d9")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(30,-300)
x.width(5)
x.down()
x.begin_fill()
x.color("#99ff99")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(-50,-250)
x.width(5)
x.down()
x.begin_fill()
x.color("#4d4dff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(-110,-300)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffffff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(-190,-250)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffb3d9")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(-270,-300)
x.width(5)
x.down()
x.begin_fill()
x.color("#99ff99")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(-310,-250)
x.width(5)
x.down()
x.begin_fill()
x.color("#4d4dff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

'''
x.up()
x.goto(30,-200)
x.width(5)
x.down()
x.begin_fill()
x.color("#ff0000")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
'''
x.up()
x.goto(30,-270)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffb3d9")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()
x.up()
x.goto(120,-250)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffffff")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()

x.up()
x.goto(-150,-200)
x.width(5)
x.down()
x.begin_fill()
x.color("#ffb3d9")
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.forward(15)
x.right(144)
x.end_fill()


#good luck
x.up()
x.goto(0,-200)
x.down()
x.color("white")
x.width(5)
x.forward(80)
x.up()
x.goto(18,-220)
x.down()
x.color("white")
x.width(5)
x.forward(25)
x.left(90)
x.forward(35)
x.left(45)
x.forward(4)
x.up()
x.goto(40,-220)
x.down()
x.color("white")
x.width(5)
x.right(135)
x.forward(27)
x.up()
x.goto(30,-230)
x.down()
x.color("white")
x.width(5)
x.forward(25)
x.right(90)
x.forward(20)
x.right(90)
x.forward(20)
x.left(90)
x.forward(1)
x.left(90)
x.forward(20)
x.right(90)
x.forward(5)
x.up()
x.goto(30,-230)
x.down()
x.color("white")
x.width(5)
x.left(1)
x.forward(27)



done()