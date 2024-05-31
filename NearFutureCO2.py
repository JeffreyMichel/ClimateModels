
from tkinter import LAST
import numpy as np
import matplotlib.pyplot as plt

#parameters
timestep = 1
start_year = 1900
end_year = 2100

#initial conditions
initial_carbon = 291 # ppm during year 1900
natural_carbon = 280 # ppm pre industrial revolution
last_carbon_amount = initial_carbon
current_masking_effect = -0.75 # (W/m^2) masking of co2 emissions from atmosphere cooling chemicals like sulfur 
current_co2_change = 2.5 # in ppm/year, the current amount of co2 added per year to the atmosphere
temp_sensitivity = 3 # degrees increase per doubling of co2
reaction_time = 20 # amount of years it takes to reach equlibrium temperature
run = 0 #to see if we have already run the inner loop
initial_T = 0 # starting temp so we see relative differences instead of overall T
T_BAU = initial_T
stop_amount = 400 #co_2 ppm where we stop emitting
ocean_uptake_time = 100 # years


A = 0.0225 #A is a tunable growth rate parameter equal to a value of 0.0225 / year, gives an atmospheric rise rate of 2.5 ppm when the pCO2 value is 400 ppm; a reasonable fit to the current pCO2 value and rate of rise. 
B = current_masking_effect / current_co2_change # a constant that estimates the masking chemicals based on the amount of industrial gas release. This assumes that co2 and other chemicals are released in tandem

# set up an array of years
timeframe = np.linspace(start_year,end_year,num=int((end_year-start_year)/timestep))
                        
# set up listss for plotting
temp_list = []
co2ppmBAU_list = []
co2ppm_noHumans_list = []
T_NH_list = []

# loop to adjust CO2 over time per year and determine impact
for i in timeframe:
    
    #business as usual carbon dioxide release (equation from class)
    co2ppmBAU = natural_carbon + (last_carbon_amount - natural_carbon) * (1 + A/timestep) 
    
    # radiative forcing for the Co2 from BAU (equation from class). Second term represents the number of doublings over natural co2
    rf_from_co2_BAU = 4 * np.log(co2ppmBAU/natural_carbon)/np.log(2) # the 4 is in W/m^2
    #calculate the masking of the RF from sulfur and the heat added from methane
    RF_masking_BAU = B * (co2ppmBAU - last_carbon_amount) / timestep
    
    # total RF
    RF_BAU = rf_from_co2_BAU + RF_masking_BAU
    
    # temperature equilibrium 
    T_eql_BAU = temp_sensitivity * RF_BAU / 4 # 4 W/m^2 is the amount of increase that corresponds to a co2_doubling
    
    #calculate current temp assuming temp reaches equlibrium after some reaction time of the atmosphere in years
    delta_T = (T_eql_BAU - T_BAU) / (reaction_time * timestep)
    T_BAU = T_BAU + delta_T
    # maintain list for plotting
    co2ppmBAU_list.append(co2ppmBAU)
    temp_list.append(T_BAU)
    

    #to calculate a future where humans teleport away, make humans disappear as soon as we hit 400 ppm
    if run==0 and co2ppmBAU >= stop_amount:
        run = 1 #make suire this isn't run twice
        last_carbon_amount_NH = co2ppmBAU # amount of carbon ppm once humans have gone away
        # calculate different co2 change per year
        delta_co2 = (340 - co2ppmBAU) * timestep / ocean_uptake_time
        T_NH = T_BAU # starting temp is the same
        T_NH_list = temp_list.copy()
        co2ppm_noHumans_list = co2ppmBAU_list.copy()

        #continue with a new loop to continue time marching forward
        for j in range(int(i)+1,int(max(timeframe)),int(timestep)):
            #no human radiative forcing. No masking because those gases decay quickly
            RF_NH = 4 * np.log(last_carbon_amount_NH / natural_carbon) / np.log(2)
            # calculate new amount of co2 change
            delta_co2 = (340 - last_carbon_amount_NH) * 0.01 * timestep 
            # equlibrium temp in this weird world
            T_eql_NH = temp_sensitivity * RF_NH / 4
            # calc new temp
            delta_T_NH = (T_eql_NH - T_NH) / (reaction_time * timestep)
            T_NH = T_NH + delta_T_NH
            #list for plotting
            co2ppm_noHumans_list.append(last_carbon_amount_NH + delta_co2)
            T_NH_list.append(T_NH)
            # save last carbon amount
            last_carbon_amount_NH = last_carbon_amount_NH + delta_co2
    # maintain last value for new calculations
    last_carbon_amount = co2ppmBAU
    


plt.plot(timeframe,temp_list,label='Business as usual')
plt.plot(timeframe,T_NH_list,label='Humans cease all emissions')
plt.title('Temperature over time')
plt.xlabel('Years')
plt.ylabel('$\Delta T$ (degrees C) from pre-industrial')
plt.legend()
plt.show()

plt.plot(timeframe,co2ppmBAU_list,label='Business as usual')
plt.plot(timeframe,co2ppm_noHumans_list,label='Humans cease all emissions')
plt.title('$CO_2$ concentration over time')
plt.xlabel('Years')
plt.ylabel('$CO_2$ concentration (ppm)')
plt.legend()
plt.show()