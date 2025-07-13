# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 09:56:55 2021

@author: enado
"""
import pandas as pd

matchesdf=pd.DataFrame(matches)
matchesdf.to_csv("matches22.csv", encoding="utf-8", index=False)

