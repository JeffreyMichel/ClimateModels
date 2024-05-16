import numpy as np
import matplotlib.pyplot as plt

# Constants
solar_constant = 1361  # Solar constant (W/m^2)
albedo = 0.31  # Earth's albedo
sigma = 5.67e-8  # Stefan-Boltzmann constant (W/m^2/K^4)
emissitivity = 1

# Model parameters
time_step = 1  # Time step in years
num_years = 100  # Number of years to simulate

# Initial conditions
global_temperature = 0  # Initial global average temperature (K)
#from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2007JD008746
heat_capacity = 17  # Effective heat capacity of the Earth's surface and atmosphere (Wam^-2K^-1)


# Arrays to store results
time = np.arange(0, num_years, time_step)
temperature = np.zeros(len(time))

#constants that estimate the amount of earth that is being hit by the sun and the amount of radiation given off by the sun
earth_radius = 6.371e6 #radius of earth in m
earth_surface_area = 4 * np.pi * earth_radius**2
area_earth_sun = np.pi * earth_radius**2 #approximate the sunny part of the earth as a disc getting hit by the sun

# Calculate incoming solar radiation
solar_radiation = solar_constant * (1 - albedo) * area_earth_sun

# Run the model
for i in range(len(time)):
    # Store temperature
    temperature[i] = global_temperature
    # This is because the atmosphere emits in 2 directions (up and down) but it is still a blackbody, so we need to do 2^1/4
    atomosphere_temperature = global_temperature / 2**(0.25)
    
    # Account for temperature of incoming radiation from the atmosphere
    total_incoming = solar_radiation + sigma * atomosphere_temperature**4 * earth_surface_area
    
    # Calculate outgoing thermal radiation
    thermal_radiation = sigma * global_temperature**4 * earth_surface_area * emissitivity
    
    
    # Calculate net energy imbalance
    energy_imbalance = total_incoming - thermal_radiation
    
    # Update temperature using energy balance equation (dU/dt = Q - W)
    d_temperature = energy_imbalance * time_step / heat_capacity / earth_surface_area 
    
    # Update global temperature
    global_temperature += d_temperature
    


# Plot results
plt.figure(figsize=(10, 6))
plt.plot(time, temperature - 273.15, label="Global Average Temperature (C)")
plt.xlabel("Time (years)")
plt.ylabel("Temperature (C)")
plt.title("Simple Climate Model")
plt.grid(True)
plt.legend()
plt.show()

print(f"Equilibrium temp: {global_temperature}")
