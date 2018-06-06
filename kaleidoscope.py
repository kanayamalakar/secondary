# code simulates a rotating kaleidoscope 
# python2 

# AUTHOR : Kanaya Malakar
# COPYRIGHT : Kanaya Malakar 2018

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')
from cycler import cycler

cmap1 = [plt.cm.plasma, plt.cm.inferno, plt.cm.magma, plt.cm.seismic, plt.cm.RdYlGn , 
         plt.cm.viridis, plt.cm.ocean, plt.cm.bone]

plt.rcParams["axes.facecolor"]='black'

no_of_beads = 30
a = 1.0
Time=48
shift = Time / len(cmap1) + 1

# Defining reflection --------------------------------------------------

def kaleidoscope(x2, y2, figname):

    # Reflection in region 1 -----------------------------------------------
    plt.plot(0,0 , 'white', marker='o', ms=430)
    
    x1 = x2 - (3**0.5)/2.0 * (x2*(3**0.5) - y2*1)
    y1 = y2 + 1/2.0 * (x2*(3**0.5) - y2*1)
    
    # Reflection in region 3 -----------------------------------------------
    
    x3 = x2 - (3**0.5)/2.0 * (x2*(3**0.5) + y2*1)
    y3 = y2 - 1/2.0 * (x2*(3**0.5) + y2*1)
    
    # Stacking all reflections
    
    X = np.stack((x1, x2, x3, x1, x2, x3))
    Y = np.stack((y1, y2, y3, -y1, -y2, -y3))
    
    plt.plot(X,Y, 'o', ms=7)
    
    # ---First layer---------------------------------------------
    
    for m in a*np.array( [[0, 2*(3**0.5)], [0, -2*(3**0.5)], [3, (3**0.5)],
                       [3, -(3**0.5)], [-3, (3**0.5)], [-3, -(3**0.5)]] ):
    	plt.plot(X +m[0], Y +m[1], 'o', ms=7)
    
    #---Second layer---------------------------------------------
    
    for m in a*np.array([ [0, 4*(3**0.5)], [0,-4*(3**0.5)], [3, 3*(3**0.5)], 
       [3,-3*(3**0.5)], [-3,3*(3**0.5)], [-3,-3*(3**0.5)], [6, 2*(3**0.5)], 
       [6, 0], [6,-2*(3**0.5)], [-6, 2*(3**0.5)], [-6, 0], [-6,-2*(3**0.5)] ]):
    	plt.plot(X +m[0], Y +m[1], 'o', ms=7)
    
    #------------------------------------------------------------
    
    rx = np.linspace(-8.2, 8.2, 100)
    ry1 = (8.2**2 - rx**2)**0.5
    ry2 =-(8.2**2 - rx**2)**0.5
    plt.plot(rx, ry1,'black', lw=30)
    plt.plot(rx, ry2,'black', lw=30)
    
    plt.tick_params(axis='both', which='both', labelsize = 0, 
                    right='off',  top='off', left ='off', bottom='off')
    plt.axis('equal')
    plt.savefig(figname)
    plt.close()
# -------------------------------------------------------------------

#---- Populate region 2 -----(notations consistent with my notes)-------------------
x2 = []
y2 = []

count=0
while count < no_of_beads:
    x = np.random.random() * (np.random.randint(0,2)*2-1)
    y = np.random.random() * (3**0.5)
    if np.pi/3 < np.arctan2(y, x) < 2*np.pi/3 :
        x2.append(x)
        y2.append(y)
        count = count +1

x2 = np.array(x2)
y2 = np.array(y2)

#--- Time evolution ---------------------------------------------

for time in range(Time):
    cmap=cmap1[time/shift]
    c = cycler('color', cmap(np.linspace(0,1,no_of_beads)) )
    plt.rcParams["axes.prop_cycle"] = c
    for i in range(len(x2)):
        x2[i] = x2[i] + 0.1
        if  np.arctan2(y2[i], x2[i]) < np.pi/3 :
            x2[i] = - np.random.random()
            y2[i] = - (3**0.5) * x2[i]
    figname = 'Fig'+str(time)+'.png'
    kaleidoscope(x2, y2, figname)



