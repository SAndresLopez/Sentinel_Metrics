#Interfaz gráfica. Se conecta a MySQL,
#Extrae la información (especialmente de la Vista SQL que creamos)
#y la transforma en algo visual


import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sentinel Metrics | Dashboard", layout="wide")
st.title("🛡️ Sentinel Metrics: Control de Retención")

def get_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="sentinel_metrics_db"
    )
    query = "SELECT * FROM customer_health_index"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

df = get_data()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Usuarios", len(df))
with col2:
    riesgo_alto = len(df[df['churn_risk'] == 'ALTO'])
    st.metric("Riesgo Alto ⚠️", riesgo_alto, delta=f"{riesgo_alto} críticos")
with col3:
    st.metric("Interacciones Totales", df['total_interactions'].sum())

st.divider()

c1, c2 = st.columns(2)

with c1:
    st.subheader("Distribución de Riesgo")
    fig, ax = plt.subplots()
    df['churn_risk'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax, colors=['red', 'yellow', 'green'])
    st.pyplot(fig)

with c2:
    st.subheader("Usuarios con Mayor Actividad")
    top_users = df.nlargest(10, 'total_interactions')
    st.bar_chart(data=top_users, x='full_name', y='total_interactions')

st.subheader("Lista de Vigilancia (Sentinel List)")
st.dataframe(df.sort_values(by="last_activity", ascending=True), use_container_width=True)