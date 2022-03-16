from cProfile import label
from function import *
import matplotlib.pyplot as plt

#Variables
duree_pneu_km = 50000
duree_voiture_km = 250000
nb_km_voiture_an = 12500


#Création d'un dictionnaire avec en clé l'année et en valeur le nombre de voiture
db_vehicles = pd.read_csv("road_transport_stock copy.csv")
db_region = select_region(db_vehicles, "France","Region","none")
sommes = create_sums(db_region,1900,2100)
nb_voiture_an = create_dict(sommes,1900,2100)
#Création d'un dictionnaire avec en clé l'année et en valeur le nombre de pneus sans prise en compte du recyclage
nb_tire = {}

print(db_region)
print(sommes)

#Convertir le stock de voiture en le stock de pneus
for cle, valeur in nb_voiture_an.items():
    nb_tire[cle] = nb_pneu_an(valeur,duree_pneu_km,nb_km_voiture_an)

annees = [int(i) for i in nb_tire.keys()]
annees_tick = [i for i in range(1900,2101,20)]
print(list(nb_tire.values()))

plt.plot(annees,list(nb_tire.values()),label='Recyclage non compris')
plt.xlabel('Années')
plt.xticks(annees_tick)
plt.ylabel('Nombre de pneus')
plt.title("Évolution du stock de pneu par an en France pour tout type de véhicule")
plt.legend()
plt.show()