import pandas as pd

liste_annees = [i for i in range(1900,2101)]

df_taux_collecte = pd.DataFrame()

taux_collecte_pneu_france = dict.fromkeys(liste_annees,0)

for key in taux_collecte_pneu_france.keys():
    # Source : https://fr.wikipedia.org/wiki/Recyclage_des_pneus (Dans Enjeux)
    for keys in taux_collecte_pneu_france.keys():
        if keys >= 1976 and keys <= 1995 :
            taux_collecte_pneu_france[keys] = [0.25]
        if keys >= 1996 and keys <= 2012 :
            taux_collecte_pneu_france[keys] = [0.52]
        if keys >= 2013 and keys <= 2016:
            taux_collecte_pneu_france[keys] = [0.78]
        if keys >= 2017:
            taux_collecte_pneu_france[keys] = [0.93]

df_new_row = pd.DataFrame(taux_collecte_pneu_france)
df_new_row['Region'] = 'France'
df_taux_collecte = pd.concat([df_taux_collecte,df_new_row.set_index('Region')],axis=0)


taux_collecte_pneu_world = dict.fromkeys(liste_annees,0)

for key in taux_collecte_pneu_world.keys():
    for keys in taux_collecte_pneu_world.keys():
        if keys >= 1986 and keys <= 2010 :
            taux_collecte_pneu_world[keys] = [0.25]
        if keys >= 2011 and keys <= 2015 :
            taux_collecte_pneu_world[keys] = [0.5]
        if keys >= 2016 :
            taux_collecte_pneu_world[keys] = [0.7]

df_new_row = pd.DataFrame(taux_collecte_pneu_world)
df_new_row['Region'] = 'World'
df_taux_collecte = pd.concat([df_taux_collecte,df_new_row.set_index('Region')],axis=0)
print(df_taux_collecte)

df_taux_collecte.to_csv('db_csv/taux_collecte.csv')