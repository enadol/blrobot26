# -*- coding: utf-8 -*-
"""
Created on Sun May 28 10:52:15 2023

@author: enado
"""

import pandas as pd

# Datos de posición del Bayern Múnich en la tabla
posicion = [1, 2, 3, 4, 5, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
partidos_ganados = [25, 23, 20, 18, 15, 22, 24, 22, 20, 22, 23, 26, 26, 24, 26, 27, 25, 26, 25, 26, 26, 25, 25, 25, 26, 26, 27, 28, 29, 29, 30, 30, 29, 29, 29]
partidos_empatados = [4, 7, 9, 9, 12, 4, 3, 6, 7, 4, 4, 4, 4, 6, 4, 3, 5, 3, 5, 4, 4, 6, 5, 5, 4, 4, 3, 3, 2, 1, 1, 1, 2, 3, 3, 3]
partidos_perdidos = [5, 4, 5, 7, 7, 8, 10, 6, 7, 8, 10, 8, 6, 8, 4, 4, 4, 6, 4, 4, 5, 4, 5, 5, 5, 4, 3, 2, 1, 0, 0, 1, 2, 1, 2, 2]

# Crear un DataFrame con los datos
data = pd.DataFrame({
    'Posicion': posicion,
    'Partidos Ganados': partidos_ganados,
    'Partidos Empatados': partidos_empatados,
    'Partidos Perdidos': partidos_perdidos
})

# Calcular la correlación entre la posición y los partidos ganados, empatados y perdidos
correlation = data['Posicion'].corr(data['Partidos Ganados'])
print(f"Correlación entre posición y partidos ganados: {correlation}")

correlation = data['Posicion'].corr(data['Partidos Empatados'])
print(f"Correlación entre posición y partidos empatados: {correlation}")

correlation = data['Posicion'].corr(data['Partidos Perdidos'])
print(f"Correlación entre posición y partidos perdidos: {correlation}")
