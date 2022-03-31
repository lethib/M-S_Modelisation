"""
Exemple d'importation d'un csv en DataFrame
"""

from numpy import append
import pandas as pd

from function import select_region

# intensite_matiere = pd.read_csv("db_csv/csv_data_pneus/intensite_matiere_pneu_[tRM_par_tPneu]", header=0).set_index(["Region", "TU", "RM"])
# print(intensite_matiere)

nb_pneus_vehicule = pd.read_csv("db_csv/csv_data_pneus/[pneus_par_vehicule]", header=0).set_index("TU")
print(nb_pneus_vehicule)

df_vehicules = pd.read_csv("db_csv/road_transport_stock copy.csv", header=0).set_index(["Approach","Calcul","Region","TU"])
print(df_vehicules)
df_region = df_vehicules.loc[('EnergyStart','Feedback','France')]
print(df_region)

df_pneus = df_region.mul(nb_pneus_vehicule)
print(df_pneus)

df_pneus['Region'] = 'France'
print(df_pneus.set_index(["Region"],append=True))

df_region_2 = df_vehicules.loc[('EnergyStart','Feedback','Africa')]
df_pneus_2 = df_region_2.mul(nb_pneus_vehicule)
df_pneus_2['Region'] = 'Africa'
print(df_pneus_2.set_index(["Region"],append=True))

df_pneus_tot = pd.concat([df_pneus_2.set_index(["Region"],append=True),df_pneus.set_index(["Region"],append=True)],axis=0)
print(df_pneus_tot)