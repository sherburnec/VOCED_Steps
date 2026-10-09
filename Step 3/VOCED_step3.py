import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

#Read in csv data
csv_filepath = r'W:\Astrophysics\ML Basics\SEIP_data.csv'
seip_data = pd.read_csv(csv_filepath)

seip_data = seip_data[seip_data['Teff'].notna()]

#Create temperature ranges
spectral_temps = [
    (seip_data['Teff'] > 31900),
    (seip_data['Teff'] <= 31900) & (seip_data['Teff'] > 10400 ),
    (seip_data['Teff'] <= 10400) & (seip_data['Teff'] > 7400 ),
    (seip_data['Teff'] <= 7400) & (seip_data['Teff'] > 5990 ),
    (seip_data['Teff'] <= 5999) & (seip_data['Teff'] > 5380 ),
    (seip_data['Teff'] <= 5380) & (seip_data['Teff'] > 3930 ),
    (seip_data['Teff'] <= 3930) & (seip_data['Teff'] > 2350 )
]
colors = [ '#8B00FF', '#4B0082', '#0000FF', '#00FF00', '#FFFF00', '#FF7F00', '#FF0000']
labels = ["O", "B", "A", "F", "G", "K", "M"]
spectral_colors = np.select(spectral_temps, colors, default='gray')

print("Testing")
# Setup Scatter plot and show
# plt.scatter(seip_data['ra'], seip_data['dec'], c=spectral_colors, label="Temperatures")
# plt.grid(True)
# plt.xlabel('Right Ascension')
# plt.ylabel('Declination')

ax = plt.subplot(projection ='mollweide')
ax.scatter(np.deg2rad((seip_data['ra']) - 180), np.deg2rad(seip_data['dec']), c=spectral_colors)
ax.grid(True)

try:
    handles = [plt.plot([], [], marker='o', ls='', color=c)[0] for c in colors]
    plt.legend(handles, labels, bbox_to_anchor=(1.02, 1), loc = "upper left")
    plt.show(block = True)
except Exception as e:
    print(f"An error occurred: {e}")

# plt.show()