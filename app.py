import pandas as pd
import streamlit as st
import plotly_express as px
vehicles = pd.read_csv('vehicles_us.csv')
st.header('Price Analysis')
st.write('Here is a look at how different variables affect vehicle prices')
list_for_hist = ['condition', 'transmission', 'type']
selected_variable = st.selectbox('Select a variable', list_for_hist)
fig1 = px.histogram(vehicles, x="price", color= selected_variable,)
fig1.update_layout(title= "<b> Visual of price by {}</b>".format(selected_variable))
st.plotly_chart(fig1)
