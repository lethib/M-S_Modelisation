import pandas as pd
import matplotlib.pyplot as plt

df_flux_entrant = pd.read_csv('db_csv/db_flux_entrant.csv',header=0).set_index(['Region','TU'])
liste_annees = [i for i in range(1901,2101)]

print(liste_annees)

somme_france = df_flux_entrant.loc['France'].sum()
somme_world = df_flux_entrant.loc['World'].sum()

dic_france = dict.fromkeys(liste_annees,0)
dic_world = dict.fromkeys(liste_annees,0)

i = 0
for keys in dic_france.keys():
    dic_france[keys] = somme_france.iloc[i]
    i += 1


i = 0
for keys in dic_world.keys():
    dic_world[keys] = somme_world.iloc[i]
    i += 1


fig, (ax1, ax2) = plt.subplots(1,2)
fig.suptitle('Flux entrant en nombre de pneus en prenant (sans recyclage)')

print(list(dic_france.values()))

ax1.plot(liste_annees, list(dic_france.values()))
ax1.set_title('France')
ax2.plot(liste_annees, list(dic_world.values()))
ax2.set_title('World')

plt.tight_layout()
plt.show()
