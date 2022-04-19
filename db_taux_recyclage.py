import pandas as pd

liste_annees = [i for i in range(1900,2101)]

df_taux_recyclage = pd.DataFrame()

taux_recyclage_pneu_france = dict.fromkeys(liste_annees,0)

for key in taux_recyclage_pneu_france.keys():
    # Source : https://fr.wikipedia.org/wiki/Recyclage_des_pneus (Dans Enjeux)
    for keys in taux_recyclage_pneu_france.keys():
        if keys >= 1981 and keys <= 2001 :
            taux_recyclage_pneu_france[keys] = [0.25]
        if keys >= 2002 and keys <= 2007 :
            taux_recyclage_pneu_france[keys] = [0.50]
        if keys >= 2008 and keys <= 2018:
            taux_recyclage_pneu_france[keys] = [0.75]
        if keys >= 2019:
            taux_recyclage_pneu_france[keys] = [0.78]

df_new_row = pd.DataFrame(taux_recyclage_pneu_france)
df_new_row['Region'] = 'France'
df_taux_recyclage = pd.concat([df_taux_recyclage,df_new_row.set_index('Region')],axis=0)


taux_recyclage_pneu_world = dict.fromkeys(liste_annees,0)

for key in taux_recyclage_pneu_world.keys():
    for keys in taux_recyclage_pneu_world.keys():
        if keys >= 1986 and keys <= 1996 :
            taux_recyclage_pneu_world[keys] = [0.15]
        if keys >= 1997 and keys <= 2010 :
            taux_recyclage_pneu_world[keys] = [0.25]
        if keys >= 2011 :
            taux_recyclage_pneu_world[keys] = [0.5]

df_new_row = pd.DataFrame(taux_recyclage_pneu_world)
df_new_row['Region'] = 'World'
df_taux_recyclage = pd.concat([df_taux_recyclage,df_new_row.set_index('Region')],axis=0)
print(df_taux_recyclage)

df_taux_recyclage.to_csv('db_csv/taux_recyclage.csv')