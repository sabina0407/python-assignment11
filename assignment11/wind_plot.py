import plotly.express as px
import plotly.data as pldata

# Task 3: Interactive Visualizations with Plotly

# Load wind dataset
df = pldata.wind(return_type='pandas')
# First and Last 10 rows
print("First 10 rows:\n",df.head(10), "\n")
print("Last 10 rows:\n",df.tail(10), "\n")

# Clean the data; convert 'strength' column to a float. Use of str.replace() with regex 
df['strength'] = df['strength'].str.replace(r'[^\d.]', '', regex=True).astype(float)

# Create an interactive scatter plot of strength vs. frequency, with colors based on the direction
fig = px.scatter(df, x='strength', y='frequency', color='direction', 
                 title='Wind Strength vs Frequency by Direction', hover_data=['direction'])

# Save and load the HTML file
fig.write_html('wind.html', auto_open=True)