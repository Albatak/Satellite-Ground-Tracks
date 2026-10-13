#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:08:58 2022

@author: alibatuhanakbey
"""

import numpy as np # library for scientific computing in Python
# e = 0.2
# M = 0.349 #rad 

# input=degree outpur=rad
def nu2E(nu,e):
    bruch = (e+np.cos(nu))/(1+e*np.cos(nu))
    return np.arccos(bruch)

######################################################
# AUXILIARY FUNCTION: returns equation value
######################################################
def f_VdW(E,e,M):
      VdW = E - e*np.sin(E) - M 
      return VdW
######################################################
# AUXILIARY FUNCTION: returns the derivative of the VdW equation w.r.t. V
######################################################
def f_dVdW(E,e):
      dVdW = 1 - e*np.cos(E) #the derivative of the VdW equation
      return dVdW
#################################################
# FUNCTION TO PERFORM THE NEWTON METHOD
#################################################
def newton_method(x0,tol,nmax,e,M):
    # This is the main function where most of the calculations are done.
    # Prepare for the iteration:
    x = x0                              # setting the initial values for the loop
    fx = f_VdW(x,e,M)                       # evaluating the function
    dfx= f_dVdW(x,e)                      # evaluating the function derivative
    niter = 0                           # setting iteration counter
    diff = -fx/dfx                      # calculate initial distance between points
    res = abs(fx)                            # the initial error
    # Perform the iteration as long as udonot reach the condition
    while abs(fx) > tol and niter < nmax:       ## KLAUSURRELEVANT !!!!!!
            # calculate value of new iteration           
                      
            fx = f_VdW(x,e,M)       
            dfx= f_dVdW(x,e)
            diff= -fx/dfx                  # new step size
            x = x + diff                      # guess of the result 
            niter += 1                     # count iteration
            res = np.append(res, abs(fx))  # store residual
            #print(str(niter)+". Iteration value= " + str(x))
            # exit condition
            if niter==nmax and diff>tol:
                print('Newton method stopped without convergence')
    # Returns the desired values to the main program     
    return (x,res,niter)

# tol=1e-15
# # Initial value
# x0 = 0.349
# nmax=1000

# (x,res,niter) = newton_method(x0,tol,nmax)

# print('Exzentrische Anomalie beträgt = ' + str(x) + 'rad' + ' = ' + str((180/np.pi)*x) + '°'  )
