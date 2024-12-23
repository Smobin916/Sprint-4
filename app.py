import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset’s CSV file into a Pandas DataFrame
df = pd.read_csv('vehicles_us.csv')

# Create a header
st.header('Car Sales Data Analysis')

# Create a Plotly Express histogram
fig_hist = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_hist)

# Create a Plotly Express scatter plot
fig_scatter = px.scatter(df, x='year', y='price', title='Price vs Year')
st.plotly_chart(fig_scatter)

# Create a checkbox that changes the behavior of the scatter plot
if st.checkbox('Show only cars with price above $10,000'):
    df_filtered = df[df['price'] > 10000]
    fig_scatter_filtered = px.scatter(df_filtered, x='year', y='model_year', title='Price vs Year (Filtered)')
    st.plotly_chart(fig_scatter_filtered)
