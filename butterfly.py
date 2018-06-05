# this code generates a picture of flying butterflies.
# python2 and python3

#AUTHOR : Kanaya Malakar
#COPYRIGHT : 2018 Kanaya Malakar

#Sample output file : butterfly.eps

from turtle import*
import numpy as np

up()

# define butterfly -------------------------------------------------------
def butterFly(x,y, angle=90, size=40, fill='cyan', border='yellow'):
	color(border, fill)
	setpos(x, y)
	begin_fill()
	seth(angle)
	down()
	width(0.1)
	fd(size), rt(30)
	circle(-0.6*size, extent=90)
	rt(40)
	circle(-0.5*size, extent=120)
	lt(180)
	circle(-0.3*size, extent=210)
	setpos(x,y)
	seth(angle)
	fd(size), lt(30)
	circle(0.6*size, extent=90)
	lt(40)
	circle(0.5*size, extent=120)
	lt(180)
	circle(0.3*size, extent=210)
	end_fill()
	up()


# color schemes - choose fillings ----------------------------------------------------------------------------

dot(900, 'mediumturquoise')

fillings= ['red', 'magenta', 'crimson', 'darkviolet', 'blueviolet', 'tomato', 'orangered', 'sandybrown']
#fillings= ['green', 'darkgoldenrod', 'olive', 'lime', 'forestgreen', 'olivedrab', 'darkgreen', 'khaki']
#fillings = ['lightyellow', 'yellow', 'greenyellow', 'goldenrod', 'khaki', 'orange', 'darkgoldenrod', 'gold']
#fillings = ['navy', 'darkblue', 'mediumblue', 'midnightblue', 'indigo', 'darkmagenta', 'purple']

bg = ['palegreen', 'paleturquoise', 'skyblue', 'aquamarine', 'powderblue', 'lightskyblue']


# background - light dots on pale blue sky---------------------------------------------------------------------

for l in range(50):
	setpos(np.random.randint(-300,300), np.random.randint(-250,250))
	down()
	dot(np.random.randint(50, 80), bg[np.random.randint(0, len(bg))] )
	up()

# overlapping butterflies---------------------------------------------------------------------------------------

for i in range(30):
	butterFly(x = np.random.randint(-250,250), y = np.random.randint(-250,250), angle = np.random.randint(60,120), size = np.random.randint(20, 50), fill = fillings[np.random.randint(0, len(fillings))])


# non-overlapping butterflies-----------------------------------------------------------------------------------
'''
xhist = [0] # x history
yhist = [0] # y history
shist = [0] # size history
count = 0
while count < 30:
	x = np.random.randint(-250,250)
	y = np.random.randint(-250,250)
	size = np.random.randint(20,50)
	Range = (( np.array(xhist) -x)**2.0 + ( np.array(yhist) -y)**2.0 )**0.5	# 1D array , dist of the present point from all other centres
	
	test =  Range - (np.array(shist) + size) 
	for i in test:
		if i<0:
			Flag = 0
			break
		else:
			Flag = 1
	
	if Flag == 1:
		butterFly( x, y, angle = np.random.randint(45,135), size= size, fill = fillings[np.random.randint(0, len(fillings))] )
		count = count + 1 
		xhist.append(x)
		yhist.append(y)
		shist.append(size)
	else: 
		count = count
'''	
#------------------------------------------------------------------------------------------------------

hideturtle()

ts = getscreen()
ts.getcanvas().postscript(file="butterfly.eps")




