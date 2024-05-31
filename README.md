# Climate Models

Welcome to the Climate Models repository! This collection of climate models was developed as part of a course on Coursera. These models aim to simulate various aspects of Earth's climate system and provide insights into the complexities of climate dynamics.

## Table of Contents

1. [Introduction](#introduction)
2. [Usage](#usage)
3. [Models](#models)
4. [Contributing](#contributing)

## Introduction

Climate models are essential tools for understanding the Earth's climate system and predicting future changes. This repository contains a set of climate models developed using various techniques taught in the Coursera course. The models cover a range of topics including atmospheric circulation, ocean dynamics, greenhouse gas concentrations, and climate feedback mechanisms.

## Usage

To use the climate models in this repository, follow these steps:

1. Clone the repository to your local machine (git clone https://github.com/yourusername/climate-models.git)
2. Navigate to the directory containing the desired model.
3. Follow the instructions provided in the model's README file to run the simulation and analyze the results.

## Models

### 1. Pane of Glass model

- **Description:** This model simulates the global atmospheric temperature assuming that the atmosphere is the same as a pane of glass, emitting in two directions: up and down.
- **Features:** Produces a graph to demostrate equilibrium time frame as well as outputting the equlibrium temperature.
- **Dependencies:** Requires Python 3 and Matplotlib library.

### 2. Ice Temperature Feedback

- **Description:** This project simulates the Earth's climate response to varying levels of solar radiation by modeling the relationship between albedo and temperature. The simulation utilizes a simple energy balance model to demonstrate how albedo, the reflectivity of the Earth's surface, changes with temperature and how these changes affect the equilibrium temperature of the Earth.
- **Features:**
  - Energy Balance Model: Calculates equilibrium temperature based on incoming solar radiation and albedo.
  - Dynamic Albedo Adjustment: Albedo is dynamically adjusted based on temperature using linear regression coefficients.
  - Bi-Stability Demonstration: Shows how two stable temperature states can exist for a given solar radiation level by simulating the system with increasing and then decreasing solar radiation.
- **Dependencies:** Requires Python 3 and Matplotlib library.

### 3. A Look Into the Future
- **Description:** This project simulates the impact of human activities on climate change using a simple carbon dioxide (CO2) emission model. It explores the effects of continued CO2 emissions versus a scenario where human emissions cease abruptly. The simulation considers various factors such as radiative forcing, temperature sensitivity, and the masking effect of cooling chemicals on CO2 emissions.
- **Features:**
  - CO2 Emission Model: Calculates CO2 concentrations over time based on historical trends and projected future emissions.
  - Radiative Forcing Calculation: Estimates the radiative forcing from CO2 emissions and masking effects from cooling chemicals. An assumption is made that all other gases are released with a direct correlation to the amount of ppm change in CO2 per year. 
  - Temperature Equilibrium: Computes equilibrium temperature changes based on radiative forcing and sensitivity parameters.
  - Human Intervention Scenario: Analyzes a hypothetical scenario where human emissions suddenly cease.
 
- **Dependencies:** Requires Python 3 and Matplotlib library.
- **Conclusions:** By modifying the cooling chemical coeffcient (which was done by modifying that amount of sulfur dioxide that ships were allowed to release), you can change the speed of climate change. 

## Contributing

We welcome contributions from the community to enhance the functionality and accuracy of these climate models. If you would like to contribute, please follow these guidelines:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and ensure that the code passes all tests.
- Submit a pull request detailing your changes and the problem they solve.
