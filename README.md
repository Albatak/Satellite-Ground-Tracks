# Orbital Mechanics & Satellite Ground Track Toolkit

> A Python-based astrodynamics framework designed for Keplerian orbit propagation, transcendental equation root-finding, celestial coordinate transformations, and satellite ground track visualization.

---

## Overview

Accurate orbit propagation and coordinate conversions are fundamental to space mission planning, satellite constellation design, and ground station visibility analysis. This repository provides modular numerical tools to compute spacecraft states, solve Kepler's equation for eccentric orbits, and model ground track trajectories over planetary bodies.

---

## Core Modules & Methodology

### 1. Kepler's Equation & Anomaly Solver (`eccentric_anomaly.py`)
Converting mean anomaly ($M$) to eccentric anomaly ($E$) for eccentric orbits requires solving Kepler's transcendental equation:
$$E - e \sin(E) = M$$

* **Newton-Raphson Algorithm:** Implements an iterative root-finding method with customizable error tolerance ($tol$) and maximum iteration caps ($n_{max}$) to ensure rapid convergence.
* **Residual Monitoring:** Tracks error reduction across iterations.
* **Anomaly Conversion:** Computes true anomaly ($\nu$) to eccentric anomaly ($E$) mappings via:
  $$\cos(E) = \frac{e + \cos(\nu)}{1 + e \cos(\nu)}$$

### 2. GTO Propagation & Ground Track Analysis (`Main_Groundtracks.py`)
Models a high-eccentricity Geostationary Transfer Orbit (**GTO**) with typical mission parameters ($e = 0.73$, inclination $i = 25^\circ$).
* **Celestial Coordinate Transformations:** Converts true anomaly ($\nu$) into equatorial celestial coordinates—specifically **Right Ascension ($\alpha$)** and **Declination ($\delta$)**:
  $$\sin(\delta) = \sin(i) \sin(\omega + \nu)$$
* **Quadrant Boundary Handling:** Incorporates robust conditional logic to manage arctangent periodic boundary discontinuities across all four orbital quadrants.
* **Trajectory Visualization:** Utilizes `matplotlib` to plot temporal and spatial orbital behavior.

---

## Tech Stack & Requirements

* **Language:** Python 3.x
* **Libraries:** `numpy`, `matplotlib`

### Quick Start Example
To solve Kepler's equation for a given mean anomaly and eccentricity using the built-in Newton solver:

```python
import numpy as np
from eccentric_anomaly import newton_method

# Define orbital parameters
e = 0.2
M = 0.349  # radians (Mean anomaly)
x0 = 0.349 # Initial guess for eccentric anomaly
tol = 1e-15
nmax = 1000

# Execute Newton-Raphson solver
E, residuals, iterations = newton_method(x0, tol, nmax, e, M)
print(f"Eccentric Anomaly: {E:.6f} rad ({np.rad2deg(E):.2f}°)")
