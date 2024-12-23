import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset’s CSV file into a Pandas DataFrame
cars_df = pd.read_csv('vehicles_us.csv')

# Create a header
st.header('Car Sales Data Analysis')

# Create a Plotly Express histogram
fig_hist = px.histogram(cars_df, x='price', title='Price Distribution')
st.plotly_chart(fig_hist)

# Create a Plotly Express scatter plot
fig_scatter = px.scatter(cars_df, x='model_year', y='price', title='Price vs Model Year')
st.plotly_chart(fig_scatter)

# Create a checkbox that changes the behavior of the scatter plot
if st.checkbox('Show only cars with price above $10,000'):
    cars_df_filtered = cars_df[cars_df['price'] > 10000]
    fig_scatter_filtered = px.scatter(cars_df_filtered, x='model_year', y='price', title='Price vs Model Year (Filtered)')
    st.plotly_chart(fig_scatter_filtered)

