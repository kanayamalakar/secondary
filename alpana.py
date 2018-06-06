# code creates a mandala or alpana (aesthetic geometrical pattern)
# python2 

# AUTHOR : Kanaya Malakar
# COPYRIGHT : Kanaya Malakar 2018

import numpy as np
import matplotlib.pyplot as plt

Color = ['lightcoral', 'khaki', 'salmon', 'crimson', 'sandybrown', 'lightsalmon', 'gray', 'floralwhite']
#Color = ['lightseagreen', 'mediumturquoise', 'aqua', 'deepskyblue', 'silver', 'lightgray', 'gray', 'ivory']


# coordinate transformation under vector rotation
'''
X = x np.cos A - y np.sin A
Y = x np.sin A + y np.cos A
'''
def repetition(x,y, repeat=4, color='red', lw=2, skew=0):
	for q in range(repeat):
		A = q* 2*np.pi/repeat
		X = x *np.cos(A+skew) - y *np.sin(A+skew)
		Y = x *np.sin(A+skew) + y *np.cos(A+skew)
		plt.plot(X,Y, color=color, lw=lw)


theta = np.linspace(0, 2*np.pi, 200)


#Fermat's spiral r^2 = a^2 theta
phi = np.linspace(0.0, 8*np.pi, 100)
r = (0.2**2.0 * phi)**0.5
x = r*np.cos(phi)
y = r*np.sin(phi)
plt.plot(x, y, lw=2, color=Color[0])
plt.plot(-x, -y, lw=2, color=Color[1])


# Astroid  x = a cos(t)^3 ; y = a sin(t)^3
x = 0.5 * (np.cos(theta))**3.0 + 1.5
y = 0.5 * (np.sin(theta))**3.0
repetition(x,y, 12, color=Color[2])


# Double Folium r = 4a cos(theta) sin(theta)^2
r = 4*0.25* np.cos(theta)*(np.sin(theta))**2
x = r*np.cos(theta)+1.7
y = r*np.sin(theta)
repetition(x, y, repeat=12, color=Color[3], lw=2, skew= np.pi/12.0)


# Lituus  r^2 = a^2/theta
phi = np.linspace(1.0, 10*np.pi, 100)
r1 = (0.5**2.0/phi)**0.5
x = r1*np.cos(phi)
y = r1*np.sin(phi)+2.5
repetition(x, y, repeat=24, color=Color[4], lw=2)
r2 =-(0.5**2.0/phi)**0.5
x = r2*np.cos(phi)
y = r2*np.sin(phi)+2.5
repetition(x, y, repeat=24, color=Color[5], lw=2)


# sine
x = np.linspace(0, 0.3, 10)
y = 0.03*np.sin(x/0.3*2*np.pi) + 3.0
repetition(x, y, repeat=64, color=Color[6])

plt.tick_params( axis='both', which='both', bottom='off', top='off', 
                left='off', right='off', labelleft='off', labelbottom='off') 
plt.axis('equal')
plt.set_facecolor=Color[7]
plt.show()


