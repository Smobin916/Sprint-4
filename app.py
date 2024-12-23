import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset’s CSV file into a Pandas DataFrame
cars_df = pd.read_csv('vehicles_us.csv')

# Create a header
st.header('Car Sales Data Analysis')

# Create columns for layout
col1, col2 = st.columns([3, 1])

with col2:
    # Create dropdown menus
    car_type = st.selectbox('Select Car Type', cars_df['type'].unique())
    car_year = st.selectbox('Select Car Year', cars_df['model_year'].unique())

# Filter the DataFrame based on selections
filtered_df = cars_df[(cars_df['type'] == car_type) & (cars_df['model_year'] == car_year)]

# Create a Plotly Express histogram
fig_hist = px.histogram(filtered_df, x='price', title='Price Distribution')
st.plotly_chart(fig_hist)

# Create a slider below the histogram
price_range = st.slider('Select Price Range', 0, 50000, (0, 50000))

# Filter the DataFrame based on price range
filtered_df_price = filtered_df[(filtered_df['price'] >= price_range[0]) & (filtered_df['price'] <= price_range[1])]

# Update the histogram based on price range
fig_hist_price_filtered = px.histogram(filtered_df_price, x='price', title='Price Distribution (Filtered by Price)')
st.plotly_chart(fig_hist_price_filtered)


