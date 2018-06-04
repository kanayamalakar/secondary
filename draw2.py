


from pylab import*

#-- definitions of mathematical functions --------------------------------

def plotsin(a,b,c,d,f,l,u, color):	#plot a*sin(b*(x-c))+d+x/e;  
	x=linspace(l,u,200)
	y=a*sin(b*(fabs(x)-c))+d+fabs(x)/f
	plot(x,y, color=color, lw=3)


def plothair(a,b,c,d,f,g,l,u):	#plot a*e^-b(x-c)+d+fsin(gx)
	x=linspace(l,u,200)
	y=a*e**(-b*(x-c))+d+f*sin(g*x)
	plot(x,y, 'blue', lw=3)


def plotcosh(a,b,c,l,u, color):		#plot a*(cosh(bx))+c
	x=linspace(l,u,50)
	y=a*cosh(b*x)+c
	plot(x,y, color=color, lw=3)


def plotface(a,b,c,l,u, color):	#plot a((bx)^2)+c
	x=linspace(l,u,500)
	y=a*((b*x)**2)+c
	plot(x,y, color=color, lw=4)


def circle(a,b,r,f, color):		#plot (x-a)^2+(y-b)^2=r^2
	x=linspace(a-r,a+r,200)
	y1=f*(((r**2 - (x-a)**2))**.5)+b
	y2=f*(-((r**2 - (x-a)**2))**.5)+b
	plot(x,y1, color=color, lw=4)
	plot(x,y2, color=color, lw=4)


from numpy import log

def plotlog(a,b,c,l,u):	#plot a*log(x-c)to base b;  u=upper,l=lowerlimit
	x = linspace(l,u,100)
	y=a*log(abs(x)-c) / log(b)
	plot(x,y, 'saddlebrown', lw=3)

#---- drawing facial parts with curves  --------------------------------------


plothair(30,.01,0,70,1,1/5.,0,200)	     #left half hair
plothair(30,-.01,0,70,1,-1/5.,-200,0)   #right half hair

plotface(20,1/100.,-40,-200,200, 'darkorange')	#face

plotlog(5,1.5,0,.8,200)		#right eyebrow
plotlog(5,1.5,0,-200,-.8)	#left eyebrow

circle(106.,39.,28.,.35, 'gray')	#right eye
circle(-106.,39.,28.,.35, 'gray')	#left eye

plotsin(11,1/58.,20,35,30,20,200, 'darkslategray')		#right upper eyelid
plotsin(-10,1/58.,20,35,30,20,200, 'darkslategray')		#right lower eyelid
plotsin(11,1/58.,20,35,30,-200,-20, 'darkslategray')   	#left upper eyelid
plotsin(-10,1/58.,20,35,30,-200,-20, 'darkslategray')	#left lower eyelid

plotface(25,1/100.,-20,-25,25, 'firebrick')	#mouth
plotcosh(.1,1/5.,-25,-24,24, 'maroon')		#lower lip
plotsin(1,1/5.,0,-17,1000,-25,25, 'r')  	#upper lip

circle(0.,60.,10.,.5, 'red')		#bindi
circle(30.,0.,25.,.4, 'goldenrod')	#nose ring
plotcosh(.5,.3,-5,-10,10, 'orangered')		#nose

tick_params(axis='both', which='both', labelsize = 0, 
            right='off',  top='off', left ='off', bottom='off')
axis([-207, 207, -43, 107])

show()
