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

def select_region(csv_file, region, header_column_name, vehicle_type):
    """Permet de choisir les lignes correspondant à la région du monde choisie, mettre "none" dans vehicle_type pour sortir tous les véhicules pour la région choisie. Sinon mettre la région"""

    if vehicle_type == "none":
        return csv_file[csv_file[header_column_name] == region]
    else:
        return csv_file[(csv_file[header_column_name] == region) & (csv_file["TU"] == vehicle_type)]

def create_dict(csv_row, start_year, end_year):
    """Création du Dictionnaire donnant en clé, l'année et en valeur le nombre de voiture en stock"""
    start_column = start_year - 1899
    end_column = end_year - 1899

    dic = {}

    for i in range(start_column, end_column+1):
        dic[start_year + i - start_column] = csv_row.iloc[i] #Ne pas mettre de iloc[i,0] quand il n'y a qu'une seule colonne

    return dic

def create_list_dic(nb_ligne, csv_file, start_year, end_year):
    """Création d'une liste de dictionnaire"""
    list = []

    for j in range(nb_ligne):
        selected_row = csv_file.iloc[j,:] #Retourne la ligne sous la forme d'une colonne
        dic = create_dict(selected_row, start_year, end_year)
        list.append(dic)

    return list

def create_sums(csv_file, start_year, end_year):
    start_column = start_year - 1896
    end_column = end_year - 1896

    only_numbers = csv_file.iloc[:, (start_column-1):(end_column+1)]

    return only_numbers.sum()

