import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import classification_report

# Charger les données directement
financial = pd.read_csv('data/financial_clean.csv')

# Préparer les données pour clustering et régression
def prepare_data(financial, features, target, n_clusters=3):
    
    encoder = LabelEncoder()
    financial_encoded = financial.copy()  # Créer une copie pour encoder

    for col in features:
        financial_encoded[col] = encoder.fit_transform(financial_encoded[col])

    # Clustering avec KMeans
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(financial_encoded[features])
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(scaled_data)
    financial['cluster'] = clusters

    # PCA pour réduction des dimensions
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(scaled_data)
    financial['X'] = pca_result[:, 0]
    financial['Y'] = pca_result[:, 1]

    return financial, kmeans

# Visualiser les clusters
def visualize_clusters(financial):
    
    fig = px.scatter(
        financial, x='X', y='Y', color='cluster',
        title="Répartition des clusters (PCA)",
         labels={'X': 'Axe X (80% variance)', 'Y': 'Axe Y (20% variance)', 'cluster': 'Cluster'},
        hover_data=['gender', 'group_age', 'category']
    )
    return fig



# Analyser les proportions de genres, groupes d'âge et catégories
def analyze_proportions(financial_data):
    
    # Proportions de genre
    gender_counts = financial_data['gender'].value_counts(normalize=True) * 100

    # Proportions de groupes d'âge
    age_counts = financial_data['group_age'].value_counts(normalize=True) * 100

    # Proportions de catégories
    category_counts = financial_data['category'].value_counts(normalize=True) * 100

    # Création des graphiques
    fig_gender = px.pie(
        names=gender_counts.index, values=gender_counts.values,
        title="Répartition des Genres"
    )

    fig_age = px.pie(
        names=age_counts.index, values=age_counts.values,
        title="Répartition des Groupes d'Âge"
    )

    fig_category = px.pie(
        names=category_counts.index, values=category_counts.values,
        title="Répartition des Catégories"
    )

    return fig_gender, fig_age, fig_category



# Régression logistique et visualisation des coefficients
from sklearn.preprocessing import OneHotEncoder

def train_and_visualize_logistic_regression(financial, features, target):
   
    # Encoder les colonnes catégoriques
    encoder = OneHotEncoder(sparse_output=False, drop='first')  # OneHotEncoder pour les variables catégoriques
    X_encoded = encoder.fit_transform(financial[features])
    encoded_feature_names = encoder.get_feature_names_out(features)

    # Séparer les données d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, financial[target], test_size=0.3, random_state=42)

    # Entraîner le modèle
    model = LogisticRegression(class_weight='balanced', random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Affichons  le rapport de classification
    st.text("Rapport de Classification :")
    st.text(classification_report(y_test, y_pred))

    # Visualisons  les coefficients
    coefficients = pd.DataFrame({
        'Feature': encoded_feature_names,
        'Coefficient': model.coef_[0]
    }).sort_values(by='Coefficient', ascending=False)

    fig = px.bar(
        coefficients, x='Coefficient', y='Feature', orientation='h',
        title="Importance des Variables (Coefficients)",
        labels={'Coefficient': 'Coefficient', 'Feature': 'Variable'}
    )
    return fig


# Interface Streamlit
st.title("Analyse et Recommandations")


# Définir les colonnes explicatives et la cible
features = ['group_age', 'gender', 'category']
target = 'is_fraud'

# Étape 1 : Préparer les données
financial, kmeans = prepare_data(financial, features, target)

# Ligne 1 : Clusters et Proportions des Genres
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(visualize_clusters(financial), use_container_width=True)
with col2:
    fig_gender, fig_age, fig_category = analyze_proportions(financial)
    st.plotly_chart(fig_gender, use_container_width=True)

# Ligne 2 : Proportions des Groupes d'Âge et Catégories
col3, col4 = st.columns(2)
with col3:
    st.plotly_chart(fig_age, use_container_width=True)
with col4:
    st.plotly_chart(fig_category, use_container_width=True)

# Ligne 3 : Rapport de Classification et Importance des Variables
col5, col6 = st.columns(2)
with col5:
    st.subheader("Rapport de Classification")
    train_and_visualize_logistic_regression(financial, features, target)
with col6:
    st.plotly_chart(train_and_visualize_logistic_regression(financial, features, target), use_container_width=True)

#####================================================

import streamlit as st
##streamlit 1.40.02

import time

#Progress bar
my_bar = st.progress(0)
for p in range(10):
    time.sleep(1)
    my_bar.progress(p+1)

# #Spinner
with st.spinner('Waiting...'):
    time.sleep(5)

st.success('Finished')