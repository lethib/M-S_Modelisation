from function import *

#Variables
voiture_essence = "TTWFossil"

db_vehicles = pd.read_csv("road_transport_stock copy.csv")
db_voiture_essence = select_vehicle_type(db_vehicles, voiture_essence, "TU","France")
dic_test = create_dict(db_voiture_essence,1900,2100)
print(db_voiture_essence)
print(dic_test)
