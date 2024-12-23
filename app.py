import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset’s CSV file into a Pandas DataFrame
cars_df = pd.read_csv('vehicles_us.csv')

# Remove missing values
cars_df.dropna(inplace=True)

# Separate company name and car model if they are combined
cars_df[['manufacturer', 'model']] = cars_df['model'].str.split(' ', 1, expand=True)

# Convert model_year to integer
cars_df['model_year'] = cars_df['model_year'].astype(int)

# Create a header
st.header('Car Sales Data Analysis')

# Create columns for layout
col1, col2 = st.columns([3, 1])

with col2:
    # Create dropdown menus
    car_type = st.selectbox('Select Car Type', cars_df['type'].unique())
    car_year_range = st.select_slider('Select Car Year Range', options=sorted(cars_df['model_year'].unique()), value=(cars_df['model_year'].min(), cars_df['model_year'].max()))
    company_name = st.selectbox('Select Company Name', cars_df['manufacturer'].unique())

# Filter the DataFrame based on selections
filtered_df = cars_df[(cars_df['type'] == car_type) & (cars_df['model_year'] >= car_year_range[0]) & (cars_df['model_year'] <= car_year_range[1]) & (cars_df['manufacturer'] == company_name)]

# Create a Plotly Express scatter plot
fig_scatter = px.scatter(filtered_df, x='model_year', y='price', title='Price vs Model Year')
st.plotly_chart(fig_scatter)

# Create a Plotly Express histogram
fig_hist = px.histogram(filtered_df, x='price', title='Price Distribution')
st.plotly_chart(fig_hist)




