# Importar las bibliotecas necesarias
import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv("static/datasets/registros_carros_electricos.csv")
    df['fecha_registro'] = pd.to_datetime(df['fecha_registro'])
    return df

df = load_data()

st.title("Análisis de Registros de Coches Eléctricos")

st.sidebar.header("Filtros")

unique_brands = df['marca_auto'].unique()
selected_brands = st.sidebar.multiselect("Marca del Auto", unique_brands, default=unique_brands)

min_year = int(df['año_modelo'].min())
max_year = int(df['año_modelo'].max())
selected_years = st.sidebar.slider("Año del Modelo", min_year, max_year, (min_year, max_year))

min_autonomy = int(df['autonomia_km'].min())
max_autonomy = int(df['autonomia_km'].max())
selected_autonomy = st.sidebar.slider("Autonomía (km)", min_autonomy, max_autonomy, (min_autonomy, max_autonomy))

unique_charge_types = df['tipo_carga'].unique()
selected_charge_types = st.sidebar.multiselect("Tipo de Carga", unique_charge_types, default=unique_charge_types)

min_date = df['fecha_registro'].min().date()
max_date = df['fecha_registro'].max().date()
selected_dates = st.sidebar.date_input("Fecha de Registro", [min_date, max_date])

selected_recycled = st.sidebar.selectbox("Baterías Recicladas", ["Todos", "Sí", "No"])

min_age = int(df['edad'].min())
max_age = int(df['edad'].max())
selected_age = st.sidebar.slider("Edad del Propietario", min_age, max_age, (min_age, max_age))

start_date = pd.to_datetime(selected_dates[0])
end_date = pd.to_datetime(selected_dates[1])

df_filtered = df[
    (df['marca_auto'].isin(selected_brands)) &
    (df['año_modelo'] >= selected_years[0]) & (df['año_modelo'] <= selected_years[1]) &
    (df['autonomia_km'] >= selected_autonomy[0]) & (df['autonomia_km'] <= selected_autonomy[1]) &
    (df['tipo_carga'].isin(selected_charge_types)) &
    (df['fecha_registro'] >= start_date) & (df['fecha_registro'] <= end_date) &
    (df['edad'] >= selected_age[0]) & (df['edad'] <= selected_age[1])
]

if selected_recycled != "Todos":
    df_filtered = df_filtered[df_filtered['baterias_recicladas'] == selected_recycled]

st.header("Datos Filtrados")
st.dataframe(df_filtered)

if not df_filtered.empty:
    with st.expander("Autos por Marca"):
        brand_counts = df_filtered['marca_auto'].value_counts().reset_index()
        brand_counts.columns = ['Marca', 'Cantidad']
        fig = px.bar(brand_counts, x='Marca', y='Cantidad', title="Número de Autos por Marca", color='Marca')
        st.plotly_chart(fig)

    with st.expander("Distribución de Autonomía"):
        fig = px.histogram(df_filtered, x='autonomia_km', title="Distribución de Autonomía (km)", nbins=20)
        st.plotly_chart(fig)

    with st.expander("Distribución de Tipos de Carga"):
        charge_counts = df_filtered['tipo_carga'].value_counts().reset_index()
        charge_counts.columns = ['Tipo de Carga', 'Cantidad']
        fig = px.pie(charge_counts, names='Tipo de Carga', values='Cantidad', title="Distribución de Tipos de Carga")
        st.plotly_chart(fig)

    with st.expander("Autonomía vs. Año del Modelo"):
        fig = px.scatter(df_filtered, x='año_modelo', y='autonomia_km', title="Autonomía vs. Año del Modelo", 
                         hover_data=['marca_auto', 'modelo_auto'])
        st.plotly_chart(fig)

    with st.expander("Baterías Recicladas"):
        recycled_counts = df_filtered['baterias_recicladas'].value_counts().reset_index()
        recycled_counts.columns = ['Recicladas', 'Cantidad']
        fig = px.bar(recycled_counts, x='Recicladas', y='Cantidad', title="Autos con Baterías Recicladas")
        st.plotly_chart(fig)
else:
    st.warning("No hay datos disponibles con los filtros seleccionados.")