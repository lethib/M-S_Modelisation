import pandas as pd
import numpy as np

df_pneus = pd.read_csv('db_csv/csv_data_pneus/db_pneus',header=0).set_index(["TU","Region"])
liste_annees = [i for i in range(1901,2101)]
liste_regions = ["France", "Africa", "ASEAN", "China", "Europe\France", "India", "LatinAmerica", "MiddleEast", "NorthAmerica", "OCDEPacific", "RestOfAsia","World"]
liste_vehicules = ["TTWFossil","TTWElec","TTWHydrogen","PLDVFossil","PLDVElec","PLDVPlugInHybrid","PLDVHydrogen","LCVFossil","LCVElec","LCVPlugInHybrid","LCVHydrogen","BusFossil","BusElec","BusHydrogen","TruckFossil","TruckElec","TruckHydrogen"]
duree_vie_pneu = 8 #ans
print(len(liste_regions))
print(len(liste_vehicules))

df_flux_entrant = pd.DataFrame()
print(df_flux_entrant)

dic_flux = {}
for region in liste_regions:
    for vehicule in liste_vehicules:
        ligne = (vehicule,region)
        for annees in liste_annees:
            flux = (df_pneus.loc[ligne,str(annees)] - df_pneus.loc[ligne,str(int(annees)-1)])/duree_vie_pneu
            dic_flux[str(int(annees-1)) + ' -> ' + str(int(annees))] = [flux]
        df_new_row = pd.DataFrame(dic_flux)
        df_new_row['TU'] = vehicule
        df_new_row['Region'] = region
        df_flux_entrant = pd.concat([df_flux_entrant,df_new_row.set_index(["TU","Region"])],axis=0)

print(df_pneus)
print(df_flux_entrant)
df_flux_entrant.to_csv('db_csv/db_flux_entrant.csv')