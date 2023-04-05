import pandas as pd

def read_worldbank_data(filename):
    # Load the data into a Pandas dataframe
    data = pd.read_csv(filename, skiprows=4)

    # replace na with zero
    data.fillna(0)

    # Rename the 'Country Name' column to 'Country'
    data.rename(columns={'Country Name': 'Country'}, inplace=True)

    # Transpose the data to create a dataframe with years as columns
    by_year = data.set_index('Country').T.drop(['Country Code', 'Indicator Name', 'Indicator Code'])

    # Transpose the data again to create a dataframe with countries as columns
    by_country = data.set_index(['Indicator Name', 'Country Code', 'Country']).T.drop(['Indicator Code'])

    return by_year, by_country
# Print the dataframes

df_years, df_countries = read_worldbank_data('API_19_DS2_en_csv_v2_5361599.csv')

# Print the dataframes
print('Dataframe with years as columns:')
print(df_years.head())

print('\nDataframe with countries as columns:')
print(df_countries.head())