import streamlit as st
import pandas as pd

st.title("Winery Inc. Welcome")
st.header("Data Visualization Board for Winery Inc Chemical Components")
wine = pd.read_csv("wine_data.csv")

selected_columns = st.multiselect('Select desired Columns', wine.columns.to_list(), default=['acidity','pH'])
st.dataframe(wine[selected_columns])

st.line_chart(wine[selected_columns].rename(columns={'date':'index'}).set_index('index'))
