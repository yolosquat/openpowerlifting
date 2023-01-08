# Importer les librairies
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

# Lire le fichier CSV et le stocker dans un dataframe
filename = "C:\\Users\\Adrien\\openpwr\\data.csv"
#data = pd.read_csv(filename, low_memory=False)

# Supprimer certaines colonnes inutiles
data.drop(['Event', 'Equipment', 'AgeClass', 'Division', 'BodyweightKg', 'Squat1Kg', 'Squat2Kg', 'Squat3Kg', 'Squat4Kg', 'Best3SquatKg',
           'Bench1Kg', 'Bench2Kg', 'Bench3Kg', 'Bench4Kg', 'Best3BenchKg',
           'Deadlift1Kg', 'Deadlift2Kg', 'Deadlift3Kg', 'Deadlift4Kg',
           'Best3DeadliftKg', 'TotalKg', 'Place', 'Dots', 'Wilks', 'Glossbrenner', 'Goodlift', 'Tested', 'State', 'Federation',
           'ParentFederation', 'Date', 'MeetCountry', 'MeetState', 'MeetTown','BirthYearClass',
           'MeetName'], axis=1, inplace=True)

# Supprimer les lignes contenant des valeurs nulles
data.dropna(inplace=True)

# Sélectionner les lignes de la colonne 'WeightClassKg' contenant le caractère '+'
ind = data[data['WeightClassKg'].str.contains('+')].index

# Supprimer ces lignes du dataframe
data.drop(ind, axis=0, inplace=True)

# Définir le format des colonnes
data['Name'] = data['Name'].astype(str)
data['Age'] = data['Age'].astype(float)
data['WeightClassKg'] = data['WeightClassKg'].astype(float)
data['Country'] = data['Country'].astype(str)

# Créer un nouveau dataframe avec uniquement les colonnes 'Name', 'Age', 'WeightClassKg' et 'Country'
datasimple = data[['Name', 'Age', 'WeightClassKg', 'Country']]

print(data['Name'].dtypes)

#quand print(data.dtypes) pourquoi il y a que age qui a float 
#print(data.dtypes)
