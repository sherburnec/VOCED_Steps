import pandas as pd
from scipy.optimize import curve_fit as cf
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 1. Define fundamental physical constants
h = 6.62607015e-34  # Planck constant (J*s)
c = 299792458       # Speed of light (m/s)
k = 1.380649e-23    # Boltzmann constant (J/K)

def line(x, m, b):
    return m * x + b

def parabolic(x, a, b, c):
    return a * x**2 + b * x + c

def planck_law(wavelength_um, T):
    # Convert micrometers to meters for internal SI unit calculation
    wavelength_m = wavelength_um * 1e-6
    nu = c / wavelength_m

    # B_nu = 2 h nu^3 / c^2 / (exp(h nu / kT) - 1), in W / (m^2 * Hz * sr)
    radiance_nu = (2 * h * nu**3 / c**2) / np.expm1(h * nu / (k * T))

    # 1 Jy = 1e-26 W / (m^2 * Hz)
    return radiance_nu / 1e-26

#Read in csv data
csv_filepath = r'W:\Astrophysics\ML Basics\SEIP_data.csv'
seip_data = pd.read_csv(csv_filepath)

#star_data = seip_data.loc[seip_data['objid'] == 'SSTSL2 J012412.12-741735.2', ['j','h','k','i1_f_ap2','i2_f_ap2','i3_f_ap2','i4_f_ap2','m1_f_psf']]
#x_cords = [1.235, 1.662, 2.159, 3.6, 4.5, 5.8, 8.0, 24]

star_name = 'SSTSL2 J012412.12-741735.2'

#Get scatter plot data
cols = ['j', 'h', 'k', 'i1_f_ap2', 'i2_f_ap2', 'i3_f_ap2', 'i4_f_ap2', 'm1_f_psf']
star_data = seip_data.loc[seip_data['objid'] == star_name, cols]
x = np.array([1.235, 1.662, 2.159, 3.6, 4.5, 5.8, 8.0, 24])
y = star_data.to_numpy().flatten() * 1e-6   # µJy -> Jy

#Step 2 get linear function
lopt, lcov = cf(line, x, y)
x_plots = np.linspace(x.min(), x.max(), 400)
y_linear = line(x_plots, *lopt)

#Step 3 get the quadratic
popt, pcov = cf(parabolic, x, y)
y_quad = parabolic(x_plots, *popt)


#Step 4 get plank's law
star_temp = seip_data.loc[seip_data['objid'] == star_name, 'Teff'].values[0]
print(star_temp)
# Temperature is fixed; only the overall scale (star's solid angle) is fit
scale_opt, _ = cf(lambda wl, s: s * planck_law(wl, star_temp), x, y, p0=[1e-20])
p_plots = np.geomspace(1, 30, 400)
y_plank = scale_opt[0] * planck_law(x_plots, star_temp)

#Plot Everything with labels
plt.scatter(x, y, label='Data Points')
plt.plot(x_plots, y_linear, label='Line fit')
plt.plot(x_plots, y_quad, label='Quadratic Fit')
plt.plot(x_plots, y_plank, label='Plank law')
plt.title('Fitting of SSTSL2 J012412.12-741735.2', fontsize = 19)
plt.xlabel('Wavelength (μm)', fontsize = 15)
plt.ylabel('Flux Density (Jy)', fontsize=15)
plt.ylim(.0004, .1)
plt.legend()
plt.loglog()
plt.show()