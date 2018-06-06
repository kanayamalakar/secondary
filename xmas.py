# code draws a christmas scenery with snowfall
# python2 

# AUTHOR : Kanaya Malakar
# COPYRIGHT : Kanaya Malakar 2018

import numpy as np
from turtle import*
bgcolor(0,0.1,0.2)

#~~~~~~~~~ XMAS TREE ~~~~~~~~~~~~~~~~
color('green','green')
up(), lt(90), fd(200), down(), lt(135)
begin_fill()
for x in range(1,4,1):
	fd(60*x), lt(135), dot(15*np.log(x+1),'red')
	fd(60*2/3.0*x*np.cos(np.pi/4.0)), rt(135)
lt(135), fd(85)
end_fill()
up(), lt(90), fd(254.56), rt(135), down()
begin_fill()
for x in range(1,4,1):
	fd(60*x), rt(135), dot(15*np.log(x+1),'red')
	fd(60*2/3.0*x*np.cos(np.pi/4.0)), lt(135)
rt(135), fd(85)
end_fill()


#~~~~~~~~~~TREE TRUNK~~~~~~~~~~~~~~~~~~~~~~~~~~~
lt(90), fd(20), width(40), color(0.6,0,0.5), fd(90)

#~~~~~~~~~~STAR~~~~~~~~~~~
seth(90), up(), fd(400), down(), width(1)
color('yellow','yellow')
begin_fill(), rt(236)
for x in range(1,6,1):
	lt(36), fd(40), lt(108)
end_fill()
up()

#~~~~~~~~~~~DECORATION~~~~~~~~~~~~~~~
def candle(x,y):
	setpos(x,y), down(), width(3), seth(90), color('white'), fd(20), dot(6,'yellow'), up()
	
def streamer(radius,extent):
	down(), width(6), circle(radius,extent), up()
	
def ball(Colour,x,y):
	setpos(x,y), down(), dot(12,Colour), up(), setpos(x+2,y+2), down(), dot(4,'white'),up()

#~~~~~~~~ Streamer Decoration ~~~~~~~~~~~~~~~~
setpos(-160,-50)
color('brown'),seth(0),streamer(400,38)
color('yellow'),seth(180),streamer(-370,28)
color('brown'),seth(0),streamer(170,48)
color('red'),seth(180),streamer(-140,27)#
setpos(160,-50)
color('maroon'),seth(180),streamer(-400,38)
color('red'),seth(0),streamer(370,28)
color('red'),seth(180),streamer(-170,48)
color('yellow'),seth(0),streamer(140,27)#

#~~~~~~~~ Ball Decoration ~~~~~~~~~~~~~~~~~~~~
ball('red',0,-40),ball('blue',70,-20),ball('maroon',30,70),ball('violet',-20,80),ball('purple',30,170),
ball('turquoise',-120,-10),ball('orange',-30,10),ball('yellow',-45,100),ball('red',40,100),ball('blue',-20,170),
ball('brown',40,30),ball('cyan',10,50),ball('pink',100,10),ball('magenta',-90,20),ball('red',-35,-10),
ball('blue',-85,-30),ball('brown',-5,150),ball('purple',125,-20),ball('violet',10,-50),ball('blue',-30,40),
ball('red',-7,130),ball('magenta',50,-20),ball('orange',-10,0),ball('red',20,80),ball('pink',-70,-20),
ball('yellow',-35,110),ball('blue',60,-30),ball('brown',115,-25),ball('yellow',-70,-30)

#~~~~~~~~ Candle Decoration ~~~~~~~~~~~~~~~~~~
candle(0,0),candle(10,0),candle(-10,0),candle(40,-50),candle(-40,-50),candle(-30,80),candle(-40,85),
candle(30,80),candle(40,85),candle(140,-40),candle(-120,-35),candle(-140,-40),candle(120,-35),
candle(100,0),candle(-100,0),candle(20,120),candle(-20,120),candle(10,160),candle(-10,160)

#~~~~~~~~~~~SNOW FALL~~~~~~~~~~~~~~~~
hideturtle()
speed('fast')
for x in range(2000):
	dice=np.random.random()
	if dice<0.9:
		setpos((np.random.random())*680-340 ,(np.random.random())*130-280 )
		dice2=np.random.random()
		if dice2<0.7:
			down(), dot((np.random.random())*30,'white'), up()
		else:
			down(), dot((np.random.random())*30,'cyan'), up()
	else:
		setpos((np.random.random())*650-325 ,(np.random.random())*570-270 )
		down(), dot((np.random.random())*15,'white'), up()
print('done')
done()
