# code draws a house with fence and tree
# python2 

# AUTHOR : Kanaya Malakar
# COPYRIGHT : Kanaya Malakar 2018

from turtle import*

#~~~~~~~HOME ROOF~~~~~~~~~~~~~~~~~~~~~~~
color('red','red')
begin_fill() 
fd(300)				# 300 x ; 0 y
lt(135),fd(212)		# 150 x ; 150 y
lt(90),fd(212)		# 0 x ; 0 y
end_fill()

#~~~~~~~~WALLS ~~~~~~~~~~~~~~~~~~~~~~~~~~
home()
color('brown','yellow')
begin_fill()
fd(275)				# 275 x ; 0 y
rt(90),fd(200)		# 275 x; -200 y
rt(90),fd(250)		# 25 x ; -200 y
rt(90),fd(200)		# 25 x ; 0 y
end_fill()

#~~~~~~~~~ WINDOW AND DOORS ~~~~~~~~~~~~~~~~
up()
rt(90),fd(75)		# 100 x ; 0 y
rt(90),fd(50)		# 100 x ; -50 y
down()
def window():
	color('brown','black')
	width(10)		# window pane 10 units
	begin_fill()
	for x in range(4):
		fd(50)		# window width 50 units
		rt(90)
	end_fill()
window()	# 100 x ; -50 y
lt(90)
up()
fd(150),rt(90)
down()
window()	# 250 x ; -50 y
up(),fd(150),rt(90),fd(130),rt(90)
down()
color('black','brown')
width(10)
begin_fill()
fd(125),rt(90),fd(60),rt(90),fd(125)
end_fill()

#~~~~~~~~ FENCE ~~~~~~~~~~~~~~~~~~
up()
rt(90),fd(500),rt(90),fd(70)
down()
rt(90)
def fence_hor():
	width(5)
	color('black')
	fd(340)
	up()
	fd(260)
	down()
	fd(75)
fence_hor()
up()
lt(180),fd(675),rt(90),fd(50),rt(90)
down()
fence_hor()

#~~~~~~~~~~~ TREE ~~~~~~~~~~~~~~~~~~~~~~~~
up()
rt(90),fd(120),rt(90),fd(500),rt(90)
down()
width(30)
color('brown')
fd(150)
lt(180)
width(2)
color('blue','green')
begin_fill()
for x in range(12):
	circle(30,extent=210)
	lt(180)
end_fill()

#~~~~~~~~~~~~~TEXT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
up()
fd(200)
write('\tHome Sweet Home!',True,align='center',font=('Arial',30,'bold'))
done()
