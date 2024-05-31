
from tkinter import HORIZONTAL
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

#formulas provided from class

#latitude that ice reaches when multiplied by temperature. If this formula gives a negative number, ice is down to 0
ice_latitude_slope = 1.5  # degrees latitude per kelvin
ice_latitude_intercept = -322.5 # degrees latitude

#albedo of earth as a function of temperature
albedo_temp_slope = -.01 # fraction per K
albedo_temp_intercept = 2.8 # fraction

#constants
sigma = 5.67e-8
epsilon = 1

#plotting data
L = []
T = []
J = []
t = []



def converge_albedo_temp(direction):
    
    #initial conditions
    albedo = 0.65

    #Incoming solar radiation in W/m^2, this represents the range of values for which to do the calculation 
    LRange = np.linspace(1200,1600,num=100)
    if direction == -1:
        LRange = np.flip(LRange)
        
    #loop through to find values
    for i in LRange:
        for j in range(100):
            temp = pow((i * (1 - albedo) / 4 / sigma / epsilon),0.25) # set incoming radiation to outgoing radiation and solve for T
            albedo = albedo_temp_slope * temp + albedo_temp_intercept
            albedo = min(albedo,.65) 
            albedo = max(albedo,.15)
            J.append(j)
            t.append(temp)
        L.append(i)
        T.append(temp)

converge_albedo_temp(1)
converge_albedo_temp(-1)

#plotting
plt.plot(L,T)
plt.title("Temperature as a function of Solar Radiation")
plt.figtext(0,0,"The above image has two separate lines, one with the radiation increasing in intensity and one decreasing. This demonstrates that, depending on the situation, you can have two stable temperatures at one solar radiation amount.",wrap='True',fontsize=8)
plt.xlabel("Incoming Solar Radiation W/m^2")
plt.subplots_adjust(bottom=.3)
plt.ylabel("Temperature")
plt.show()

plt.plot(J[0:len(J)//2],t[0:len(t)//2])
plt.title("Converging Albedo Temperature while Modifying Solar Insolation")
plt.show()

plt.plot(J[len(J)//2:len(J)],t[len(t)//2:len(t)],color='red')
plt.title("Converging Albedo Temperature while Modifying Solar Insolation (reversed direction)")
plt.show()



        