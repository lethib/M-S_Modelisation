import pandas as pd
from sqlalchemy import null

def nb_pneu_an(nb_voiture,duree_pneu_en_km,nb_km_an):
    """Équation de l'évolution du nombre de pneu par an"""
    res = 4*nb_voiture + 4*nb_voiture*nb_km_an/duree_pneu_en_km
    return res

def select_vehicle_type(csv_file, vehicle_type, header_column_name, region):
    """Permet de choisir les lignes correspondant aux type de véhicule choisi, mettre "none" dans région pour sortir toutes les régions pour le véhicule choisi. Sinon mettre la région."""
    if region == "none":
        return csv_file[csv_file[header_column_name] == vehicle_type]
    else:
        return csv_file[(csv_file[header_column_name] == vehicle_type) & (csv_file["Region"] == region)]

def create_dict(csv_row, start_year, end_year):
    """Création du Dictionnaire donnant en clé, l'année et en valeur le nombre de voiture en stock"""
    start_row = start_year - 1896
    end_row = end_year - 1896

    dic = {}

    for i in range(start_row, end_row+1):
        dic[start_year + i - start_row] = csv_row.iloc[0,i]

    return dic

