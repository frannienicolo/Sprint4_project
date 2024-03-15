import pandas as pd
import streamlit as st
import plotly.express as px
vehicles = pd.read_csv('vehicles_us.csv')
st.header('Vehicles Dataset Analysis')
st.write('Filter the data below to see vehicles sorted by their condition')
condition_choice = vehicles['condition'].unique()
selected_condition = st.selectbox('Select a condition', condition_choice)
vehicles_filtered = vehicles[vehicles.condition==selected_condition]
vehicles_filtered
st.header('Price Analysis')
st.write('Here is a look at how condition, transmission, and type affect vehicle prices')
list_for_hist = ['condition', 'transmission', 'type']
check = st.checkbox('Exclude cars over $40,000')
selected_variable = st.selectbox('Select a variable', list_for_hist)
if check:
    vehicles_filtered2 = vehicles[vehicles['price'] <= 40000]
else:
    vehicles_filtered2 = vehicles
fig1 = px.histogram(vehicles, x="price", color= selected_variable)
fig1.update_layout(title= "<b> Visual of price by {}</b>".format(selected_variable))
fig1.update_xaxes(range=[0, 100000])
st.plotly_chart(fig1)
st.write('Here is a look at how the odometer, model year, and model affect the price')
list_for_scat = ['odometer', 'fuel']
selected_scat_variable = st.selectbox('Select a variable', list_for_scat)
fig2 = px.scatter(vehicles, x='price', y=selected_scat_variable, color='condition')
fig2.update_xaxes(range=[0, 80000])
st.plotly_chart(fig2)