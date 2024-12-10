#===========================================================
# Importation des librairies
#===========================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import random
import warnings 
warnings.filterwarnings("ignore")
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",100)
random.seed(123)

#===========================================================
# Chargement des données
#===========================================================

#Chargement des métadonnées
metadonnees = pd.read_csv('metadonnees.csv')

#Chargement de financial
financial = pd.read_csv('financial_clean.csv', chunksize = 10**5)

#chargement des des données individuelles
individual = pd.read_csv('individual.csv')

#==========================================================
#
#==========================================================


