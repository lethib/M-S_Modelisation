import pandas as pd

nb_pneus_vehicule = pd.read_csv("db_csv/csv_data_pneus/[pneus_par_vehicule]", header=0).set_index("TU")
df_vehicules = pd.read_csv("db_csv/road_transport_stock copy.csv", header=0).set_index(["Approach","Calcul","Region","TU"])
print(df_vehicules)
liste_region = ["France", "Africa", "ASEAN", "China", "Europe\France", "India", "LatinAmerica", "MiddleEast", "NorthAmerica", "OCDEPacific", "RestOfAsia","World"]
df_pneus_tot = pd.DataFrame()


for region in liste_region:
    df_region = df_vehicules.loc[('EnergyStart','Feedback',region)]
    df_pneus = df_region.mul(nb_pneus_vehicule)
    df_pneus['Region'] = region
    df_pneus_tot = pd.concat([df_pneus_tot,df_pneus.set_index(["Region"],append=True)],axis=0)
    

print(df_pneus_tot)
df_pneus_tot.to_csv('db_csv/db_pneus')