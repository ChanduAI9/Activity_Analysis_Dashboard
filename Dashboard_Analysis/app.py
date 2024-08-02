import streamlit as st
import pandas as pd

duration_data = pd.read_csv('duration_data.csv')
activity_data = pd.read_csv('activity_data.csv')

#  Streamlit app
st.title('Activity Analysis Dashboard')

st.header('Total Duration for Each Inside and Outside Activity')
st.dataframe(duration_data)

st.header('Number of Picking and Placing Activities Done')
st.dataframe(activity_data)
selected_date = st.date_input('Select a date', value=pd.to_datetime(duration_data['date'].iloc[0]))
filtered_duration_data = duration_data[duration_data['date'] == selected_date.strftime('%Y-%m-%d')]
filtered_activity_data = activity_data[activity_data['date'] == selected_date.strftime('%Y-%m-%d')]



# filtered data
st.header(f'Filtered Data for {selected_date.strftime("%Y-%m-%d")}')
st.subheader('Duration Data')
st.dataframe(filtered_duration_data)
st.subheader('Activity Data')
st.dataframe(filtered_activity_data)
