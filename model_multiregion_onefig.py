from function import *
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random

#Variables
duree_pneu_km = 50000
duree_voiture_km = 250000
nb_km_voiture_an = 12500
liste_region = ["France", "Africa", "ASEAN", "China", "Europe\France", "India", "LatinAmerica", "MiddleEast", "NorthAmerica", "OCDEPacific", "RestOfAsia", "World"]
liste_couleurs = [color for color in mcolors.TABLEAU_COLORS]

#Création d'un dictionnaire avec en clé l'année et en valeur le nombre de voiture
db_vehicles = pd.read_csv("db_csv/road_transport_stock copy.csv")
fig, axs = plt.subplots(3, 4, sharex=True)
fig.suptitle('Evolution du stock de pneus par an pour tout type de véhicule')
i = 0

for row in range(3):
    for column in range(4):

        db_region = select_region(db_vehicles, liste_region[i], "Region", "none")
        sommes = create_sums(db_region,1900,2100)
        nb_voiture_an = create_dict(sommes,1900,2100)
        #Création d'un dictionnaire avec en clé l'année et en valeur le nombre de pneus sans prise en compte du recyclage
        nb_tire = {}


        #Convertir le stock de voiture en le stock de pneus
        for cle, valeur in nb_voiture_an.items():
            nb_tire[cle] = nb_pneu_an(valeur,duree_pneu_km,nb_km_voiture_an)

        annees = [int(i) for i in nb_tire.keys()]
        annees_tick = [i for i in range(1900,2101,20)]
        # print(list(nb_tire.values()))

        # plt.plot(annees,list(nb_tire.values()), label=region)
        axs[row, column].plot(annees, list(nb_tire.values()), c=random.choice(liste_couleurs))
        axs[row, column].set_title(liste_region[i])

        i += 1

# Set common labels
fig.text(0.5, 0.03, 'Années', ha='center', va='center')
fig.text(0.04, 0.5, 'Nombre de pneus', ha='center', va='center', rotation='vertical')

plt.tight_layout()
plt.show()
