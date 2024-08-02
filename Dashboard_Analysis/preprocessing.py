import pandas as pd

# Load the dataset
file_path = r'E:\Chandu\Assignment\Resolute\DataSets\Task3-20240717T054225Z-001\Task3\rawdata.xlsx'
data = pd.read_excel(file_path)

# Convert 'date' column to string
data['date_str'] = data['date'].dt.strftime('%Y-%m-%d')

# Concatenate 'date_str' and 'time' columns and convert to datetime
data['datetime'] = pd.to_datetime(data['date_str'] + ' ' + data['time'].astype(str))

# Calculate the total duration for each inside and outside activity
duration_data = data.groupby(['date', 'position'])['sensor'].sum().reset_index()
duration_data.rename(columns={'sensor': 'total_duration'}, inplace=True)

# Calculate the number of picking and placing activities for each date
activity_data = data.groupby(['date', 'activity']).size().reset_index(name='count')

# Save the processed data to CSV for use in Streamlit
duration_data.to_csv('duration_data.csv', index=False)
activity_data.to_csv('activity_data.csv', index=False)