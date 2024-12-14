#===========================================================
# Importation des librairies
#===========================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import cufflinks as cf
import streamlit as st
import random
random.seed(123)

#===========================================================
# Chargement des données
#===========================================================

#Chargement de métadonnées1 sur les variables d'origine
metadonnees1 = pd.read_csv('metadonnees1.csv')

#Chargement de métadonnées1 sur les variables d'origine
metadonnees2 = pd.read_csv('metadonnees2.csv')

#Chargement de financial
financial = pd.read_csv('financial_clean.csv')

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

  st.markdown("""<h2 style="text-align: left; color: darkblue;
                text-decoration: underline;">About Us</h2>""",
              unsafe_allow_html=True)
  
  st.markdown("<br>", unsafe_allow_html=True) #saut de ligne

  col1, col2 = st.columns([3, 2])
  col2.image("logo.png")

  text1 = """Créé le 1er Octobre 2021, SDA est spécialisé dans la fourniture 
             de services Cloud, d'IA générative, de Machine Learning et 
             de construction d'infrastructures de données. Nous possédons 
             des experts et spécialistes métiers dans: la Banque-finance, 
             l'Agriculture, la Santé et l'économie. Notre modèle business
             innovant s'appuie principalement sur la capitalisation de l'expérience
             client, ce qui nous permet d'améliorer continuellement nos services et 
             produits fournis."""
  
  col1.markdown(f"""<div style="text-align: justify; color: darkblue; font-size: 20px;"
                    >{text1}</div>""", unsafe_allow_html=True
                  )
  
  st.markdown("<br>", unsafe_allow_html=True)  # Saut de ligne 
  
  st.markdown("""<h2 style="text-align: center; 
                  color: darkblue;
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

  st.markdown("""<h2 style="text-align: center; color: darkblue;
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
  st.markdown("""<h1 style="color: darkblue; text-decoration: underline;
              ">Credit Card Transactions Dataset</h1>""", unsafe_allow_html=True
              )
  st.markdown("<br>", unsafe_allow_html=True) #saut de ligne
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
  
  st.markdown("<br>", unsafe_allow_html=True) #saut de ligne
  st.subheader("Tableau de synthèse sur les variables d'origine:")
  st.dataframe(data=metadonnees1, hide_index=True,
               use_container_width = True)
  st.subheader("Tableau de synthèse sur les nouvelles variables calculées:")
  st.dataframe(data=metadonnees2, hide_index=True,
               use_container_width = True)

def Statistiques():

  import fonction as fc

  st.markdown("""<h1 style="color: darkblue; text-decoration: underline;"
              >Tableau statistiques croisées</h1>""", unsafe_allow_html=True)

  col1,col2 = st.columns(2)
  data_dic = {'financial_data':financial,
              'individual_data':individual}
  
  data_list = list(name for name in data_dic.keys())
  data_name = col1.selectbox("Choisir un Dataframe dans la liste:",
                            data_list, index=0, #dataframe par défaut
                            placeholder="select data...")

  data = data_dic[data_name]
  data['date'] = pd.to_datetime(data["date"]).dt.date
  date_min = data['date'].min()
  date_max = data['date'].max()

  # liste des variables
  num_list = data.select_dtypes(include=['number']).columns.tolist()
  cat_list = data.select_dtypes(include=['object', 'category']).columns.tolist()

  # Variables catégorielles sélectionnées
  catvars = col1.multiselect("Choisir une ou plusieurs variables catégorielles:",
                                cat_list, default = ['group_age'])
    
  # variable sélectionnée dans num_list
  var = col1.selectbox("Choisir une variable numerique:", num_list,
                       index=num_list.index('daily_amount$'),
                       placeholder="select data...")
  # Filtres sur les dates
  debut = col2.date_input("selectionner date debut", date_min,
                          min_value = date_min, max_value = date_max)
  fin = col2.date_input("selectionner date fin", date_max,
                          min_value = date_min, max_value = date_max)
  try:

    # Filtrer les données sur les plages de dates
    data_filtre = (data[(data['date'] >= debut) & 
                          (data['date'] <= fin)]
                    )
    table = fc.cross_stat(data_filtre, catvars,var) 
    st.write("Statistiques par catégories sur:",var)
    st.dataframe(table, use_container_width = True)

  except Exception as e:

    st.markdown("*Entrer des valeurs dans les champs* 😊")

def Tableau_Bord():
  
  # Informations sur les détenteurs
  st.markdown("""<h2 style="color: darkblue; text-decoration: underline;
              ">Identification du Détenteur de Carte de Crédits</h1>""",
              unsafe_allow_html=True
              )
  identifiants = individual['personid'].unique().tolist()

  id = st.selectbox("Selectionner ou saisir identifiant",
                        identifiants,  index=0)
  
  persondata = individual[individual['personid']==id]

  nomcomplet = persondata['fullname'].unique()[0]
  profession = persondata['job'].unique()[0]
  naissance = persondata['dob'].unique()[0]
  age = persondata['age'].unique()[0]
  sexe = persondata['gender'].unique()[0]
  ville = persondata['city'].unique()[0]
  carte = persondata['cc_num'].unique()[0]
  emetteur = persondata['iin_group'].unique()[0]
  adresse = persondata['street'].unique()[0]
  card_dict = {'American Express':'americancard.png',
               'Visa':'visacard.png', 
               'JCB':'jcbcard.png',
               'Discover Financial Services':'discovercard.png',
               'Mastercard Group':'mastercard.png',
               'GPN':'gpncard.png',
               'UATP':'uatpcard.png',
               'Laser':'lasercard.png',
               'InstaPayment':'instapaymentcard.png'}
  carteimage = card_dict[emetteur]

  col1, col2, col3= st.columns(3)
  space ='&nbsp;'

  col1.subheader(f"{space*6}{nomcomplet}")
  col1.image('cartebank.png')

  col2.subheader(f"Infos")
  col2.write(f"Nom: {nomcomplet}")
  col2.write(f"Date de Naissance: {naissance}")
  col2.write(f"Age: {age}{space*14}Sexe: {'Masculin' if sexe == 'M' else 'Feminin'}",
             unsafe_allow_html=True)
  col2.write(f"Ville d'habitation: {ville}")
  col2.write(f"Adresse: {adresse}")
  
  #col3.subheader(f"{emetteur}")
  col3.markdown(f"<h3 style='font-size:20px;'>{emetteur}</h3>", unsafe_allow_html=True)
  col3.image(carteimage)
  col3.write(f"Carte: {carte}")

def Geodata():
  st.title("Bienvenue chez SDA Analytics Group")
  st.image(logo, width=400)

def GeoStatistiques():
  st.title("Bienvenue chez SDA Analytics Group")
  st.image(logo, width=400)

def Macroanalyse():
  st.title("Bienvenue chez SDA Analytics Group")
  st.image(logo, width=400)

def WordClouds():
  st.title("Bienvenue chez SDA Analytics Group")
  st.image(logo, width=400)

  
#==========================================================
# Execution des pages
#==========================================================

# Structure des pages de l'application web
pages = [
    st.Page(About_Us, title="Home"),
    st.Page(MétaDonnees, title="MétaDonnées"),
    st.Page(Statistiques, title="Statistiques Descriptives"),
    st.Page(Tableau_Bord, title="Suivi des KPIs de transactions individuelles"),
    st.Page(Geodata, title="Géolocalisation des transactions individuelles"),
    st.Page(Macroanalyse, title="MacroAnalyse Financière"),
    st.Page(WordClouds, title="WordClouds"),
]

pg = st.navigation(pages)
pg.run()

