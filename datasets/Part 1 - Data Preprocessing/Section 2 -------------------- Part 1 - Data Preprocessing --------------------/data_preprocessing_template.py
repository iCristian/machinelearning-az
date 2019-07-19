#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 19:43:11 2019

@author: juangabriel
"""

# Plantilla de Pre Procesado

# Cómo importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Data.csv')
# iloc = index location [filas, columnas] -1 no considera la ultima columna
X = dataset.iloc[:, :-1].values

# En python un indice comienza siempre de 0 y no toma el ultimo elemento por lo que al indicar 3 selecciona columnas 0, 1 y 2
y = dataset.iloc[:, 3].values


# Dividir el data set en conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Escalado de variables importante cuando las columnas difieren mucho entre sus vALORES
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)