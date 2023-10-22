# # Laboratorio 8
# ## Puesta en producción de un modelo de ML
# ### Integrantes
# * Marco Orozco  20857
# * Gabriel Vicente Lorenzo 20498

import streamlit as st
import joblib
import pandas as pd

model_filename = 'random_forest_model.pkl'
model = joblib.load(model_filename)

def obtener_numero_por_ciudad(ciudad):
    if ciudad == "Belo Horizonte":
        return 0
    elif ciudad == "Campinas":
        return 1
    elif ciudad == "Porto Alegre":
        return 2
    elif ciudad == "Rio de Janeiro":
        return 3
    elif ciudad == "São Paulo":
        return 4
    else:
        return "Ciudad no encontrada"

def predict_rent():
    st.title('Predicción de Alquiler Mensual')
    st.write('Este es un ejemplo de predicción de alquiler mensual.')

    city = st.selectbox('Ciudad', ["Belo Horizonte","Campinas","Porto Alegre","Rio de Janeiro","São Paulo"])  # Puedes proporcionar opciones de ciudad si es necesario
    area = st.number_input('Área (m²)', min_value=1)
    rooms = st.number_input('Número de habitaciones', min_value=1)
    bathroom = st.number_input('Número de baños', min_value=1)
    parking_spaces = st.number_input('Número de plazas de aparcamiento', min_value=0)
    floor = st.number_input('Número de plantas', min_value=0)
    animal = st.radio('¿Se permiten animales?', ['Sí', 'No'])
    furniture = st.radio('¿Está amueblado?', ['Sí', 'No'])
    hoa = st.number_input('Impuesto de la Asociación de Residentes (R$)', min_value=0)

    city = 1  
    animal = 1 if animal == 'Sí' else 0
    furniture = 1 if furniture == 'Sí' else 0

    user_data = pd.DataFrame({
        "city": [city-1],
        "area": [area],
        "rooms": [rooms],
        "bathroom": [bathroom],
        "parking spaces": [parking_spaces],
        "floor": [floor],
        "animal": [animal],
        "furniture": [furniture],
        "hoa (R$)": [hoa]
    })

    predicted_rent = model.predict(user_data)

    st.subheader('Resultado de la Predicción')
    st.write(f'La predicción de alquiler mensual es: R${predicted_rent[0]:.2f}')

if __name__ == '__main__':
    predict_rent()
