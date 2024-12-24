import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset’s CSV file into a Pandas DataFrame
cars_df = pd.read_csv('vehicles_us.csv')

# Remove missing values
cars_df.dropna(inplace=True)

# Convert model_year to integer
cars_df['model_year'] = cars_df['model_year'].astype(int)

# Create a header
st.header('Car Sales Data Analysis')

# Create columns for layout
col1, col2 = st.columns([3, 1])

with col2:
    # Create dropdown menu for car type
    car_type = st.selectbox('Select Car Type', cars_df['type'].unique())

# Filter the DataFrame based on car type selection
filtered_df = cars_df[cars_df['type'] == car_type]

# Create a checkbox to show/hide scatter plot
show_scatter = st.checkbox('Show Scatter Plot')

# Create containers for each plot
scatter_container = st.container()
extra_insight_container = st.container()
hist_container = st.container()

# Display the scatter plot at the top
with scatter_container:
    if show_scatter:
        fig_scatter_sales = px.scatter(filtered_df, x='model_year', y='price', title='Car Sales Year to Year')
        st.plotly_chart(fig_scatter_sales)

# Display the extra insight plot in the middle
with extra_insight_container:
    extra_insight = st.selectbox('Select Extra Insight', ['condition', 'cylinders', 'fuel', 'transmission', 'paint_color'])
    fig_scatter_insight = px.scatter(filtered_df, x='model_year', y='price', color=extra_insight, title=f'Price vs Model Year by {extra_insight.capitalize()}', range_y=[0, 100000])
    st.plotly_chart(fig_scatter_insight)

# Display the histogram at the bottom
with hist_container:
    yearly_sales = cars_df.groupby('model_year').size().reset_index(name='total_sales')
    fig_hist = px.histogram(yearly_sales, x='model_year', y='total_sales', title='Total US Sales Yearly')
    st.plotly_chart(fig_hist)

