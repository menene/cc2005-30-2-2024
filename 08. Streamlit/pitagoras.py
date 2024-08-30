# =======================================
# Universidad del Valle de Guatemala
# Algoritmos y programacion basica
# Seccion 30
#
# Erick Marroquin
# 123456
#
# Pitagoras web
# 23/08/24
# =======================================

import streamlit as st
import math

def hipotenusa(cateto_a, cateto_b):
    a2 = cateto_a * cateto_a
    b2 = cateto_b * cateto_b
    
    c = math.sqrt(a2 + b2)

    return c

def cateto(hipotenusa, cateto_b):
    c2 = hipotenusa ** 2
    b2 = cateto_b ** 2
    
    a = math.sqrt(c2 - b2)
    
    return a


st.title("Teorema de Pitágoras")

modo = st.sidebar.selectbox(
    "Seleccione un modo de solución",
    ["Hipotenusa Conocida", "Hipotenusa Desconocida"]
)

if modo == "Hipotenusa Conocida":
    st.header("Hipotenusa Conocida")
    st.write("Ingresa los valores de los catetos para determinar el valor de la hipotenusa")
    
    a = st.number_input("Ingrese el valor de A", min_value=0)
    b = st.number_input("Ingrese el valor de B", min_value=0)
    
    procesar = st.button("Calcular")
    
    if procesar:
        r = hipotenusa(a, b)
        
        st.write("El resultado es:")
        st.write(r)
    
elif modo == "Hipotenusa Desconocida":
    st.header("Hipotenusa Desconocida")
    st.write("Ingresa los valores de la hipotenusa y un cateto para determinar el valor del cateto restante")
    
    c = st.number_input("Ingrese el valor de C", min_value=0)
    b = st.number_input("Ingrese el valor de B", min_value=0)
    
    procesar = st.button("Calcular")
    
    if procesar:
        r = cateto(c, b)
        
        st.write("El resultado es:")
        st.write(r)






