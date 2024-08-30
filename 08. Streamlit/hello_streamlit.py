import streamlit as st

st.title("Mi primera App Web")

st.header("Escritura de texto")
st.write("Hola Mundo")
st.write("Hello World")

st.header("Ingreso de texto")
nombre = st.text_input("Nombre")

st.write(nombre)


st.header("Ingreso de numeros")
num1 = st.number_input("Ingrese cualquier número")
num2 = st.number_input("Ingrese cualquier número positivo", min_value=0)


st.header("Seleccion de opciones")
opcion = st.selectbox("Seleccione 1", ["opcion 1", "opcion 2"])

d = st.date_input("When's your birthday")
st.write("Your birthday is:", d)
