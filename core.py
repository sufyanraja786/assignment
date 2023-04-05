import matplotlib.pyplot as plt


# Select the population growth and energy consumption columns for a few countries
from main import df_years
print(df_years)
countries = ['USA', 'China', 'India']
indicators = ['Population growth (annual %)','Energy use (kg of oil equivalent per capita)']
df_pop_energy = df_years.loc[indicators, countries]


# Compute the correlation matrix
corr_matrix = df_pop_energy.corr()
print(corr_matrix)


#One pyplot graph

# Create a scatter plot of population growth vs. energy consumption for each country
fig, axs = plt.subplots(1, len(countries), figsize=(12, 4))

for i, country in enumerate(countries):
    axs[i].scatter(df_pop_energy.loc['Population growth (annual %)', country], df_pop_energy.loc['Energy use (kg of oil equivalent per capita)', country])
    axs[i].set_xlabel('Population growth (annual %)')
    axs[i].set_ylabel('Energy use (kg of oil equivalent per capita)')
    axs[i].set_title(country)

plt.show()
