import streamlit as st
import pandas as pd

def read_file(file):
    data = pd.read_csv(file, sep=",", header=None, names=["Nombre", "Edad", "Email"])
    return data

def filter_emails(data):
    filtered_data = data[data["Edad"] > 18]
    return filtered_data["Email"]

def save_emails(emails):
    with open("emails_mayores_18.txt", "w") as f:
        for email in emails:
            f.write(email + "\n")

def main():
    st.title("Filtrado de Correos Electrónicos")

    uploaded_file = st.file_uploader("Sube tu archivo de texto", type=["txt", "csv"])

    if uploaded_file is not None:
        data = read_file(uploaded_file)
        st.write("Datos cargados:")
        st.dataframe(data)

        emails = filter_emails(data)
        st.write("Correos electrónicos de personas mayores de 18 años:")
        st.write(emails)

        save_emails_button = st.button("Guardar correos en archivo")

        if save_emails_button:
            save_emails(emails)
            st.success("Archivo guardado con éxito como 'emails_mayores_18.txt'.")

if __name__ == "__main__":
    main()