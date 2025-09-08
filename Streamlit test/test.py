import streamlit as st
import pandas as pd
import numpy as np

# Titre de l'application
st.title("🚀 Test Streamlit - Ça marche !")

# Texte de bienvenue
st.write("Si vous voyez cette page, Streamlit fonctionne parfaitement !")

# Sidebar
st.sidebar.title("Menu de test")
option = st.sidebar.selectbox(
    "Choisissez un test :",
    ["Accueil", "Graphique", "Données", "Widgets"]
)

if option == "Accueil":
    st.subheader("✅ Installation réussie")
    st.success("Streamlit est correctement installé et configuré !")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("Version Python détectée")
    with col2:
        st.info("Streamlit fonctionne")

elif option == "Graphique":
    st.subheader("📊 Test graphique")
    
    # Données aléatoires
    data = pd.DataFrame({
        'x': range(10),
        'y': np.random.randn(10)
    })
    
    st.line_chart(data.set_index('x'))
    st.write("Données utilisées :", data)

elif option == "Données":
    st.subheader("📋 Test tableau")
    
    # Tableau de test
    df = pd.DataFrame({
        'Nom': ['Alice', 'Bob', 'Charlie'],
        'Âge': [25, 30, 35],
        'Ville': ['Paris', 'Lyon', 'Marseille']
    })
    
    st.dataframe(df)

elif option == "Widgets":
    st.subheader("🎛️ Test widgets")
    
    # Différents widgets
    nom = st.text_input("Votre nom :")
    age = st.slider("Votre âge", 0, 100, 25)
    
    if st.button("Cliquez-moi !"):
        if nom:
            st.balloons()
            st.success(f"Salut {nom}, vous avez {age} ans !")
        else:
            st.warning("Entrez votre nom d'abord !")

# Footer
st.markdown("---")
st.markdown("*Test Streamlit - Tout fonctionne parfaitement ! 🎉*")