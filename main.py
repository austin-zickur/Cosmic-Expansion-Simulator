import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import astropy as ap
from flask import Flask, request, render_template_string

'''
Developer: Austin Zickur

Date: 02/26/2025

Goal:
Use Friedmann equations to give a plot of the Hubble Constant
with respect to time with sliders for the Omega values (density parameters) of k (curvature),
m (mass), r (radiation), and Λ (cosmological lambda (expansion)).

Equations:
H^2/H0^2 = Omega0,R a^-4 + Omega0,M a^-3 + Omega0,k a^-2 + Omega0,Lambda

Variables:
H - Hubble constant
H0 - Hubble constant at concurrent space-time
t - time
t0 - age of the universe
Ω₀ - Density parameter
R - Radiation
M - Mass
k - Curvature
Λ - Cosmological Constant (dark energy)


Assumptions:
The universe is homogenous and isotropic, meaning all properties are identical
along every path as well as equally dependent interactions in every direction.
The universe is also 13.8 billion years old using Hubble's law: 
t0 = 2/3 * 1/H0
'''

CES = Flask(__name__)

Omegak = st.slider("Ω₀k", 0,1) #Density parameter of effect of curvature
Omegalambda = st.slider("Ω₀Λ") #Density parameter of observed effect of cosmic expansion
Omegam = st.slider("Ω₀m") #Density parameter of mass
Omegar = st.slider("Ω₀r") #Density parameter of radiation
t0 = 13.8*10**9 #yr
H0 = 69.8 #km/s/Mpc
H0 = H0*60*60*24*365.25 #km/yr/Mpc
t = np.linspace(0,t0,10**7) #Universal time array [yr]
a = (t/t0)**(2/3) #Dimensionless scale factor for expansion

H = np.sqrt((Omegar*(a**-4)+Omegam*(a**-3)+Omegak*(a**-2)+Omegalambda)/(H0)**2) #Hubble constant 

simulation = {
    "time (years)": t,
    "expansion rate of the universe (km/s/Mpc)": H
}
df = pd.DataFrame(simulation)

st.line_chart(df)