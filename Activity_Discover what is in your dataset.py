
# Import libraries and packages

import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset into a DataFrame
companies = pd.read_csv("Unicorn_Companies.csv")


# Display the first 10 rows of the data
companies[:10]


# Get information
companies.info()


# Step 1: Use pd.to_datetime() to convert Date Joined column to datetime 
# Step 2: Update the column with the converted values
companies['Date Joined'] = pd.to_datetime(companies['Date Joined'])


# Step 1: Use .dt.year to extract year component from Date Joined column
# Step 2: Add the result as a new column named Year Joined to the DataFrame
companies['Year Joined'] = companies['Date Joined'].dt.year


# Sample the data
companies_sampled = companies.sample(n = 50, random_state = 1)
companies_sampled[:5]

# Visualize the longest time it took companies to reach unicorn status for each industry represented in the sample. 

# Prepare data for plotting
companies_sampled['Years to Unicorn'] = companies_sampled['Year Joined'] - companies_sampled['Year Founded']
sampled_plot = (companies_sampled.groupby('Industry')
                .max('Years to Unicorn')
                .sort_values(by = 'Years to Unicorn')
                .reset_index()
               )

# Create bar plot
# with the various industries as the categories of the bars
# and the time it took to reach unicorn status as the height of the bars
''
plt.bar(x = sampled_plot['Industry'], height = sampled_plot['Years to Unicorn'])
plt.plot()
# Set title
plt.title('Maximum Years to Billion Dollar Valuation from Random Sample (n=50)')
plt.xlabel('Industry')
plt.ylabel('Years')
# Rotate labels on the x-axis as a way to avoid overlap in the positions of the text
plt.xticks(rotation = 45, horizontalalignment = 'right')
# Display the plot
plt.show()


# Visualize unicorn companies' maximum valuation for each industry represented in the sample.

# Create a column representing company valuation as numeric data 
# Start by getting rid of the first ($) and last (B) index in the string
y=[]
for x in companies_sampled['Valuation']:
    y.append(int(x[1:-1]))
    
companies_sampled.insert(2, 'Numeric Valuation (Billions)', y)


# Create bar plot
sampled_plot = (companies_sampled[['Industry', 'Numeric Valuation (Billions)']]
                .groupby('Industry')
                .max()
                .sort_values(by = 'Numeric Valuation (Billions)', ascending = False)
                .reset_index()
               )

plt.bar(sampled_plot['Industry'], sampled_plot['Numeric Valuation (Billions)'])
plt.title('Biggest Companies by Valuation (Sample, n = 50)')
plt.xlabel('Industry')
plt.ylabel("Valuation ($ Billions)")
plt.xticks(rotation = 45, horizontalalignment = 'right')
plt.show()
