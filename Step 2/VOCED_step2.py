import pandas as pd

csv_filepath = r'W:\Astrophysics\ML Basics\SEIP_data.csv'
csv_dataframe = pd.read_csv(csv_filepath)

print("SEIP Dataframe Head \n")
print(csv_dataframe.head())

print("\nSEIP Dataframe Info\n")
print(csv_dataframe.info())

n_matches = csv_dataframe['nmatches']

print("N Matches Max: ", end="")
print(n_matches.max())
print("N Matches Min: ", end="")
print(n_matches.min())
print("N Matches Value Counts:")
print(n_matches.value_counts())

print("N Matches For Value Count 3")
print (csv_dataframe.loc[csv_dataframe['nmatches'] == 3])