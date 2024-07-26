# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 22:30:11 2024

@author: owner
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define global variables
nu = 0.5e-11
mumax = 1.4
Km = 12
Ki = 3
Kc = 3e-11
kinetics = 'contois'

def bacteria_odes(t, x):
    global nu, mumax, Km, Ki, Kc, kinetics
    
    # Extract the dependent variables
    X = x[0]  # Biomass concentration
    S = x[1]  # Substrate concentration
    
    # Initialize the growth rate
    mu = 0
    
    # Determine the growth rate based on the selected kinetics
    if kinetics == 'monod':
        mu = mumax * S / (Km + S)
    elif kinetics == 'haldane':
        mu = mumax * S / (Km + S + (S**2 / Ki))
    elif kinetics == 'contois':
        mu = mumax * S / (Kc * X + S)
    
    # Define the ODEs
    dXdt = mu * X
    dSdt = -nu * mu * X
    
    return [dXdt, dSdt]

# Initial, final time, plot interval
t0 = 0
tf = 20
Dtplot = 0.1

# Initial conditions
ICs = 'case_2'
if ICs == 'case_1':
    X = 1.4e11
    S = 9
elif ICs == 'case_2':
    X = 1.4e11
    S = 12

x0 = [X, S]  # Initial conditions

# Define the events function (optional)
def events(t, x):
    return 1  # Placeholder: no event detection

events.terminal = True
events.direction = 0

# Call to ODE solver
method = 'RK45'  # Default method, equivalent to MATLAB's ode45

# Uncomment the method you want to use
# method = 'RK23'   # Equivalent to MATLAB's ode23
# method = 'Radau'  # Suitable for stiff problems
# method = 'BDF'    # Suitable for stiff problems
method = 'LSODA'  # Automatically switches between stiff and non-stiff methods

sol = solve_ivp(bacteria_odes, [t0, tf], x0, method=method, t_eval=np.arange(t0, tf, Dtplot), rtol=1e-3, atol=1e-3, events=events)

# Plot results
plt.figure(1)
plt.plot(sol.t, sol.y[0])
plt.xlabel('t')
plt.ylabel('X(t)')
plt.title('Biomass concentration')
plt.grid(True)

plt.figure(2)
plt.plot(sol.t, sol.y[1])
plt.xlabel('t')
plt.ylabel('S(t)')
plt.title('Substrate concentration')
plt.grid(True)

plt.show()
