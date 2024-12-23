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

# Create checkboxes for each car to compare model_year and price
for index, row in cars_df.iterrows():
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.checkbox(f"Compare {row['model']} ({row['model_year']}) - ${row['price']}", key=index):
            with col2:
                st.write(f"Model: {row['model']}")
                st.write(f"Model Year: {row['model_year']}")
                st.write(f"Price: ${row['price']}")
                st.write(f"Condition: {row['condition']}")
                st.write(f"Cylinders: {row['cylinders']}")
                st.write(f"Fuel: {row['fuel']}")
                st.write(f"Odometer: {row['odometer']}")
                st.write(f"Transmission: {row['transmission']}")
                st.write(f"Type: {row['type']}")
                st.write(f"Paint Color: {row['paint_color']}")
                st.write(f"Is 4WD: {row['is_4wd']}")
                st.write(f"Date Posted: {row['date_posted']}")
                st.write(f"Days Listed: {row['days_listed']}")

