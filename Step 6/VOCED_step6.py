from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
import astropy.units as u
from astropy.visualization import simple_norm


import matplotlib.pyplot as plt
import numpy as np

FITS = "SPITZER_I1_22839808_0000_6_E8143254_maic.fits"

# Open the file using "fits.open"
fits_file = fits.open(FITS)
# The image data
fits_data = fits_file[0].data
# The header information
fits_header = fits_file[0].header

w = WCS(fits_file[0].header)

# Define the coordinates using SkyCoord
sky = SkyCoord(ra=21.050533, dec=-74.293111, unit=(u.deg, u.deg))
x, y = w.world_to_pixel(sky)
print(f"Pixel coordinates: x={x}, y={y}")

 # Define the half-width size for the initial broad crop
crop_distance = 15

# Round coordinates to find the nearest central pixel index
y_rounded = int(np.round(y, 0))
x_rounded = int(np.round(x, 0))

# Perform the initial broad crop around the target coordinate
cropped_fits_data = fits_data[
    y_rounded - crop_distance : y_rounded + crop_distance,
    x_rounded - crop_distance : x_rounded + crop_distance
]

# Find the pixel coordinates of the maximum intensity within this crop (centroiding)
max_y, max_x = np.where(cropped_fits_data == np.nanmax(cropped_fits_data))

# Map the local maximum back to the global coordinates of the full image
coord_max_y = y_rounded - crop_distance + max_y[0]
coord_max_x = x_rounded - crop_distance + max_x[0]

# Perform a precise 11x11 crop centered on our detected peak
recropped = fits_data[
    coord_max_y - 5 : coord_max_y + 5 + 1,
    coord_max_x - 5 : coord_max_x + 5 + 1
]

# Display the results side-by-side
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Broad Crop with Peak Centroid Location
axes[0].imshow(cropped_fits_data, origin='lower', cmap='viridis')
axes[0].scatter(max_x, max_y, color='red', marker='x', s=100, label='Peak Emission')
axes[0].set_title('Broad Crop (30x30 px)')
axes[0].legend()

# Plot 2: Centered tight crop
axes[1].imshow(recropped, origin='lower', cmap='viridis')
axes[1].set_title('Centroided Crop (11x11 px)')

plt.tight_layout()
plt.show()
