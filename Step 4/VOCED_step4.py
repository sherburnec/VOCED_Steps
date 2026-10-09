import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Read in csv data
csv_filepath = r'W:\Astrophysics\ML Basics\SEIP_data.csv'
seip_data = pd.read_csv(csv_filepath)

seip_data = seip_data[seip_data['Teff'].notna()]

seip_data_mips = seip_data[seip_data['mips_obstype'] == 0]
seip_data_temp = seip_data_mips[(seip_data_mips['Teff'] > 3930) & (seip_data_mips['Teff'] < 5380)]
seip_data_log = seip_data_temp[seip_data_temp['logg'] > 3.8]

seip_data_sets = (seip_data['Teff'], seip_data_mips['Teff'], seip_data_temp['Teff'], seip_data_log['Teff'])

#seip_labels = [len(seip_data), len(seip_data_mips), len(seip_data_temp), len(seip_data_log)]
seip_labels = [f'Non 0 Data\n{len(seip_data)}',
               f'Mips filtered\n{len(seip_data_mips)}',
               f'Teff filter\n{len(seip_data_temp)}',
               f'logg filter\n{len(seip_data_log)}']

fig, ax = plt.subplots()
vp = ax.boxplot(seip_data_sets, positions=[2, 4, 6, 8], widths=1.5, patch_artist=True,
                tick_labels=seip_labels,
                showmeans=False, showfliers=False,
                whis=[10.0,90.0],
                medianprops={"color": "red", "linewidth": 0.8},
                boxprops={"facecolor": "C0", "edgecolor": "white",
                          "linewidth": 0.5},
                whiskerprops={"color": "C0", "linewidth": 1.5},
                capprops={"color": "C0", "linewidth": 1.5})

for median in vp['medians']:
    x = median.get_xdata()
    y = median.get_ydata()
    x_center = np.mean(x)
    y_val = y[0]

    ax.text(
        x_center, y_val, f'{y_val:.2f}',
        horizontalalignment='center',
        verticalalignment='bottom',
        fontsize='10',
        color='white',
        bbox=dict(facecolor='C0',alpha=0.1,edgecolor='none',pad=1),
    )

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))

plt.suptitle('Temperature ranges through filtered data sets', fontsize = 20)
plt.title('Representing 10th to 90th percentile', fontsize = 15)
plt.ylabel('Temperature', fontsize = 15)
plt.xlabel('Data sets', fontsize=15)
plt.show()