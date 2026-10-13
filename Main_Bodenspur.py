#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 15:26:33 2022

@author: alibatuhanakbey
"""
import numpy as np
import math
from ExzentrischeAnomalie import nu2E,f_VdW, f_dVdW, newton_method
import matplotlib.pyplot as plt
#Bahnparameter
# 01.07.2012 06:00 UTC auf GTO
i_d = 25
i_r = np.radians(i_d)

w_d = 120 
w_r = np.radians(w_d)

omega_d = 60
omega_r = np.radians(omega_d)

M_d = 60
M_r = np.radians(M_d)

e = 0.73

# Method 1: Start 0° Ende 360° wahre Anomalie
nu_d = np.linspace(0,360,13)
nu_r = np.radians(nu_d)

delta_nu = 30 # degrees

# Exzentrische Anomalie
E_r = nu2E(nu_r,e)
E_d = np.degrees(E_r)

# E_0 for M_0
(E_0_r,res,niter) = newton_method(M_r,1e-6,1000,e,M_r)

# nu_0 for M_0
nu_in_r = (np.cos(E_0_r)-e)/(1-e*np.cos(E_0_r))
nu_0_r = np.arccos(nu_in_r)
nu_0_d = np.degrees(nu_0_r)
# Methode 2 : wir beginnen mit nu_0 berechnet aus M_0 und rechnen 30° drauf bis wir nu_0 wieder erreichen
nu_m2_d = [nu_0_d] 

for i in range(1,12):
    ink = nu_0_d+i*delta_nu
    if ink <= 360:
        nu_m2_d.append(ink)
    elif ink > 360:
        nu_m2_d.append(ink-360) 

nu_m2_r = np.radians(nu_m2_d)

# Bestimmung Rektaszension alpha und Deklination delta aus wahre Anomalie nu

# Rektaszension alpha
def rektaszension(i_r,w_r,nu_r):

    # a1_korr = np.cos(i_r)*np.tan((w_r+nu_r)%np.pi/2)
    # a1 = np.cos(i_r)*np.tan((w_r+nu_r))
    # alpha1 = np.arctan(a1_korr) 
    # alpha = np.degrees(alpha1) + omega_d

    # for i in nu:
    #     a = np.arctan(np.cos(i)*np.tan(w+nu))
    #     print("for nu=" + str(nu[i]) + "°" + " Rektaszension alpha = " + str(a) + "°" ) 
    
    # Rievers: 0 bis 180 keine Korrektur. Ab 180 korrigieren tan(360-Winkel)
    # +pi/2 korrektur 
    a1 = np.cos(i_r)*np.tan((w_r+nu_r)%np.pi/2)
    #alpha = np.arctan(a1)
    alpha1 = np.arctan(a1)
    
    for i in range(2,len(alpha1)):
        alpha1[i]+=90*np.pi/180

    for i in range(8,len(alpha1)):
        alpha1[i]+=90*np.pi/180
    
    return alpha1 + omega_d

alpha_m1 = rektaszension(i_r,w_r,nu_r)

# Methode 1
alpha_d = np.degrees(rektaszension(i_r,w_r,nu_r))
alpha_r = np.radians(alpha_d)

# Rektaszension alpha
def rektaszension_2(i_r,w_r,nu):
    a1=[]
    # Rievers: 0 bis 180 keine Korrektur. Ab 180 korrigieren tan(360-Winkel)
    for i in range(len(nu)):
        # 1. Bereich
        if (w_r+nu[i]) <= np.pi/2:
            a1.append(np.cos(i_r)*np.tan(w_r+nu))
            #print("1.teyim")
        # 2. Bereich
        elif (w_r+nu[i]) > np.pi/2 and (w_r+nu[i]) <= np.pi:
            # a1.append(np.cos(i_r)*np.tan(2*np.pi-(w_r+nu_r)))
            a1.append(np.cos(i_r)*np.tan(np.pi-(w_r+nu)))
            #print("2.teyim")
        # 3. Bereich
        elif (w_r+nu[i]) > np.pi and (w_r+nu[i]) <= 3*np.pi/2:
            a1.append(np.cos(i_r)*np.tan(w_r+nu-np.pi))
            #print("3.teyim")
        # 4. Bereich
        elif (w_r+nu[i]) > 3*np.pi/2 and (w_r+nu[i]) <= 2*np.pi:
            # a1.append(np.cos(i_r)*np.tan(2*np.pi-(w_r+nu_r)))
            a1.append(np.cos(i_r)*np.tan(2*np.pi-(w_r+nu)))
            #print("4.teyim")
        # 1 Turn 1. Bereich 
        elif (w_r+nu[i]) > 2*np.pi and (w_r+nu[i]) <= 5*np.pi/2:
            a1.append(np.cos(i_r)*np.tan(w_r+nu)) 
            #print("1.teyim 2.kez")
        # 1 Turn 2. Bereich
        elif (w_r+nu[i]) > 5*np.pi/2 and (w_r+nu[i]) <= 3*np.pi:
            a1.append(np.cos(i_r)*np.tan(np.pi-(w_r+nu)))
            #print("2.teyim 2.kez")
          
    alpha_r = np.arctan(a1) + omega_r
    alpha_d = np.degrees(alpha_r)
    
    return alpha_r, alpha_d, a1


# Methode 2 mit nu_m2_r
alpha_m2_r, alpha_m2_d, a1 = rektaszension_2(i_r,w_r,nu_m2_r)

# Rektaszension Matrix
alpha_m2_r_1 = alpha_m2_r[0]
# alpha_m2_r_1[1] += 2*np.pi 
# alpha_m2_r_1[7] += 2*np.pi 
alpha_m2_d_1 = np.degrees(alpha_m2_r_1)

# Deklination delta
de = np.sin(i_r)*np.sin(w_r+nu_m2_r)
delta = np.arcsin(de)

plt.plot(nu_m2_d, np.degrees(delta))
# plt.ylim(-2,5)
plt.show()
