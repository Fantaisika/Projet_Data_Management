#===========================================================
# Importation des librairies
#===========================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
import random
random.seed(123)

#===========================================================
# Chargement des données
#===========================================================

#Chargement des métadonnées
metadonnees = pd.read_csv('metadonnees.csv')

#Chargement de financial
financial = pd.read_csv('financial_clean.csv', chunksize = 10**5)

#chargement des des données individuelles
individual = pd.read_csv('individual_data.csv')

#==========================================================
# Configuration de la page streamlit 
#==========================================================

st.set_page_config(page_title="SDA ANALYTICS GROUP",
                  layout="wide"
                  )

#==========================================================
# Construction des elements de la page
#==========================================================

def About_Us():

  st.markdown("""<h1 style="color: steelblue;">Bienvenue!</h1>""",
                   unsafe_allow_html=True
              )
  
  st.markdown("<br>", unsafe_allow_html=True) #saut de ligne

  col1, col2 = st.columns([2, 2])
  col1.image("logo.png")

  text1 = """Créé le 1er Octobre 2021, SDA est spécialisé dans la fourniture 
             de services Cloud, d'IA générative, de Machine Learning et 
             de construction d'infrastructures de données. Nous possédons 
             des experts et spécialistes métiers dans: la Banque-finance, 
             l'Agriculture, la Santé et l'économie. Notre modèle business
             innovant s'appuie principalement sur la capitalisation de l'expérience
             client, ce qui nous permet d'améliorer continuellement nos services et 
             produits fournis."""
  
  col2.markdown(f"""<div style="text-align: justify; font-size: 20px;"
                    >{text1}</div>""", unsafe_allow_html=True
                  )
  
  st.markdown("<br>", unsafe_allow_html=True)  # Saut de ligne 
  
  st.markdown("""<h2 style="text-align: center; 
                  color: DodgerBlue;
                  ">Expertises Métiers</h2>""", 
                  unsafe_allow_html=True
                  )
  
  col1, col2, col3, col4 = st.columns(4)
  col1.image("bank.jpg")
  col1.markdown(f"""<div style="text-align: justify;color: darkblue;
                ">BANQUES</div>""",unsafe_allow_html=True)
  col2.image("economie.jpg")
  col2.markdown(f"""<div style="text-align: justify;color: blue;
                ">ECONOMIE</div>""",unsafe_allow_html=True)
  col3.image("sante.jpg")
  col3.markdown(f"""<div style="text-align: justify;color: steelblue;
                ">SANTE</div>""",unsafe_allow_html=True)
  col4.image("agriculture.jpg")
  col4.markdown(f"""<div style="text-align: justify;color: green;
                ">AGRICULTURE</div>""",unsafe_allow_html=True)

  st.markdown("<br>", unsafe_allow_html=True)  # Saut de ligne 

  st.markdown("""<h2 style="text-align: center; 
                  color: DodgerBlue;
                  ">Présentation de l'équipe</h2>""", 
                  unsafe_allow_html=True
                  )
  
  col1, col2, col3, col4 = st.columns(4)
  with col1:

    st.header("Atji Cheick")
    st.image("cheick.jpg")
    st.write("""Junior Statistician and Data Analyst, Atji
             travaille chez SDA en qualité de Consultant en
             risques de crédits depuis 3 ans.""")


  with col2:

    st.header("Atji Cheick")
    st.image("cheick.jpg")
    text = """Junior Statistician and Data Analyst, Atji
             travaille chez SDA en qualité de Consultant en
             risques de crédits depuis 3 ans."""
    st.markdown(f"""<div style="text-align: justify;">{text}</div>""",
                   unsafe_allow_html=True
                  )
 
  with col3:
    
    st.header("Atji Cheick")
    st.image("cheick.jpg")
    st.write("""Junior Statistician and Data Analyst, Atji
             travaille chez SDA en qualité de Consultant en
             risques de crédits depuis 3 ans.""")

  with col4:
    
    st.header("Atji Cheick")
    st.image("cheick.jpg")
    st.write("""Junior Statistician and Data Analyst, Atji
             travaille chez SDA en qualité de Consultant en
             risques de crédits depuis 3 ans.""")


def MétaDonnees():

  lien = "https://www.kaggle.com/datasets/priyamchoksi/credit-card-transactions-dataset"
  
  description = """Jeux de données sur les transactions horaires de cartes 
                   de crédits et fraudes aux USA de 2019 à 2020.
                """
  st.markdown("""<h1 style="color: darkblue;
              ">Credit Card Transactions Dataset</h1>""", unsafe_allow_html=True
              )
  col1,col2,col3, col4 = st.columns([2,1,1,2])
  
  col1.subheader("Description", divider = True)
  col1.markdown(f"""<div style="text-align: justify; color: darkblue;
                    font-size: 20px;">{description}</div>""", unsafe_allow_html=True              
                  )
  
  col2.subheader("Taille", divider = True)
  col2.markdown(f"""<div style="text-align: center; color: darkblue;
                    font-size: 30px;">1.296.675</div>""", unsafe_allow_html=True              
                  )
  col3.subheader("Variables", divider = True)
  col3.markdown(f"""<div style="text-align: center; color: darkblue;
                    font-size: 30px;">23</div>""", unsafe_allow_html=True              
                  )
  col4.subheader("Source données", divider = True)
  col4.page_link(lien, label="Kaggle Dataset", icon="🌎")
  
  st.header("Tableau de synthèse:")
  st.dataframe(data=metadonnees, hide_index=True,
               use_container_width = True)


def Tableau_Bord_Individuel():
  st.title("Bienvenue chez SDA Analytics Group")
  st.image(logo, width=400)


def GeoStatistiques():
  st.title("Bienvenue chez SDA Analytics Group")
  st.image(logo, width=400)

def WordClouds():
  st.title("Bienvenue chez SDA Analytics Group")
  st.image(logo, width=400)

  
#==========================================================
# Execution
#==========================================================
pg = st.navigation([st.Page(About_Us),
                    st.Page(MétaDonnees),
                    st.Page(Tableau_Bord_Individuel),
                    st.Page(GeoStatistiques),
                    st.Page(WordClouds)])
pg.run()