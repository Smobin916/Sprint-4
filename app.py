import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset’s CSV file into a Pandas DataFrame
cars_df = pd.read_csv('vehicles_us.csv')

# Create a header
st.header('Car Sales Data Analysis')

# Create a Plotly Express scatter plot
fig_scatter = px.scatter(cars_df, x='model_year', y='price', title='Price vs Model Year')
st.plotly_chart(fig_scatter)

# Create columns for layout
col1, col2 = st.columns([3, 1])

with col2:
    # Create dropdown menus
    car_type = st.selectbox('Select Car Type', cars_df['type'].unique())
    car_year = st.selectbox('Select Car Year', cars_df['model_year'].unique())

# Filter the DataFrame based on selections
filtered_df = cars_df[(cars_df['type'] == car_type) & (cars_df['model_year'] == car_year)]

# Update the scatter plot based on selections
fig_scatter_filtered = px.scatter(filtered_df, x='model_year', y='price', title='Price vs Model Year (Filtered)')
st.plotly_chart(fig_scatter_filtered)

# Create a slider below the scatter plot
price_range = st.slider('Select Price Range', int(cars_df['price'].min()), int(cars_df['price'].max()), (int(cars_df['price'].min()), int(cars_df['price'].max())))

# Filter the DataFrame based on price range
filtered_df_price = filtered_df[(filtered_df['price'] >= price_range[0]) & (filtered_df['price'] <= price_range[1])]

# Update the scatter plot based on price range
fig_scatter_price_filtered = px.scatter(filtered_df_price, x='model_year', y='price', title='Price vs Model Year (Filtered by Price)')
st.plotly_chart(fig_scatter_price_filtered)

