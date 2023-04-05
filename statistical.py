import pandas as pd

# Load the data
data = pd.read_csv('API_19_DS2_en_csv_v2_5361599.csv', skiprows=4)
data.fillna(0)
# Select the indicators you're interested in
indicators = ['GDP per capita (current US$)', 'Life expectancy at birth, total (years)', 'CO2 emissions (metric tons per capita)']

# Select a few countries to compare
countries = ['United States', 'China', 'India', 'Japan']

# Filter the data by indicators and countries
filtered_data = data[data['Country Name'].isin(countries)][['Country Name', 'Indicator Name', '2019']]

# Pivot the data to have indicators as columns
pivoted_data = filtered_data.pivot(index='Country Name', columns='Indicator Name', values='2019')

# Calculate summary statistics
summary_stats = pivoted_data.describe()

# Calculate correlation coefficients between indicators
correlation_matrix = pivoted_data.corr()

# Calculate mean and median for each indicator
mean_values = pivoted_data.mean()
median_values = pivoted_data.median()

# Print the results
print('Summary statistics:')
print(summary_stats)

print('\nCorrelation coefficients:')
print(correlation_matrix)

print('\nMean values:')
print(mean_values)

print('\nMedian values:')
print(median_values)


