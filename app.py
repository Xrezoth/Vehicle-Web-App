import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') #Leer los datos

st.header('Autos en Estados Unidos')# Mostrar encabezado

hist_button = st.button('Construir histograma') #Construir un botón para histograma
scatter_button = st.button('Gráfico de dispersión') #Construir un botón para un gráfico de dispersión

if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

if scatter_button: #Al hacer clic en el botón
        # escribir un mensaje
        st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

        # Crear un gráfico de dispersión
        fig = px.scatter(car_data, x="odometer", y="price")

        # Mostrar un gráfico interactivo
        st.plotly_chart(fig, use_container_width=True)


