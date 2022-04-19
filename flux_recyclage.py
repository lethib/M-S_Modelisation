import pandas as pd

df_pneus = pd.read_csv('db_csv/csv_data_pneus/db_pneus',header=0).set_index(["TU","Region"])
df_taux_recyclage = pd.read_csv('db_csv/taux_recyclage.csv',header=0).set_index('Region')
print(df_taux_recyclage)
df_taux_collecte = pd.read_csv('db_csv/taux_collecte.csv',header=0).set_index("Region")

liste_annees = [i for i in range (1901,2101)]
liste_regions = ["France", "World"]
liste_vehicules = ["TTWFossil","TTWElec","TTWHydrogen","PLDVFossil","PLDVElec","PLDVPlugInHybrid","PLDVHydrogen","LCVFossil","LCVElec","LCVPlugInHybrid","LCVHydrogen","BusFossil","BusElec","BusHydrogen","TruckFossil","TruckElec","TruckHydrogen"]

duree_vie_pneu = 8 #ans

df_flux_entrant = pd.DataFrame()
dic_flux = {}

for region in liste_regions:
    for vehicule in liste_vehicules:
        ligne = (vehicule,region)
        for annees in liste_annees:
            flux = (df_pneus.loc[ligne,str(annees)] - df_pneus.loc[ligne,str(int(annees)-1)])/duree_vie_pneu
            flux_recyclage = flux*df_taux_collecte.loc[region,str(annees)]*df_taux_recyclage.loc[region,str(annees)]
            dic_flux[str(int(annees-1)) + ' -> ' + str(int(annees))] = [flux_recyclage]
        df_new_row = pd.DataFrame(dic_flux)
        df_new_row['TU'] = vehicule
        df_new_row['Region'] = region
        df_flux_entrant = pd.concat([df_flux_entrant,df_new_row.set_index(["TU","Region"])],axis=0)

print(df_flux_entrant)

df_flux_entrant.to_csv('db_csv/db_flux_entrant_recyclage.csv')