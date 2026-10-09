import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

#Read in csv data
csv_filepath = r'W:\Astrophysics\ML Basics\SEIP_data.csv'
seip_data = pd.read_csv(csv_filepath)

print(len(seip_data))
seip_data = seip_data[seip_data['Teff'].notna()]
print(seip_data['Teff'].max())

seip_data_mips = seip_data[seip_data['mips_obstype'] == 0]
print(seip_data_mips['Teff'].max())
seip_data_temp = seip_data_mips[(seip_data_mips['Teff'] > 3930) & (seip_data_mips['Teff'] < 5380)]
seip_data_log = seip_data_temp[seip_data_temp['logg'] > 3.8]

seip_data_sets = (seip_data['Teff'], seip_data_mips['Teff'], seip_data_temp['Teff'], seip_data_log['Teff'])

seip_labels = [len(seip_data), len(seip_data_mips), len(seip_data_temp), len(seip_data_log)]

fig, ax = plt.subplots()
VP = ax.boxplot(seip_data_sets, positions=[2, 4, 6, 8], widths=1.5, patch_artist=True,
                tick_labels=seip_labels,
                showmeans=False, showfliers=False,
                medianprops={"color": "red", "linewidth": 0.8},
                boxprops={"facecolor": "C0", "edgecolor": "white",
                          "linewidth": 0.5},
                whiskerprops={"color": "C0", "linewidth": 1.5},
                capprops={"color": "C0", "linewidth": 1.5})

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()