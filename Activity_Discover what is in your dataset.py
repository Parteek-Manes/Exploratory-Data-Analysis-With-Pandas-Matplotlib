#!/usr/bin/env python
# coding: utf-8

# # Activity: Discover what is in your dataset

# ## Introduction
# 
# In this activity, you will discover characteristics of a dataset and use visualizations to analyze the data. This will develop and strengthen your skills in **exploratory data analysis (EDA)** and your knowledge of functions that allow you to explore and visualize data. 
# 
# EDA is an essential process in a data science workflow. As a data professional, you will need to conduct this process to better understand the data at hand and determine how it can be used to solve the problem you want to address. This activity will give you an opportunity to practice that process and prepare you for EDA in future projects.
# 
# In this activity, you are a member of an analytics team that provides insights to an investing firm. To help them decide which companies to invest in next, the firm wants insights into **unicorn companies**–companies that are valued at over one billion dollars. The data you will use for this task provides information on over 1,000 unicorn companies, including their industry, country, year founded, and select investors. You will use this information to gain insights into how and when companies reach this prestigious milestone and to make recommendations for next steps to the investing firm.

# ## Step 1: Imports

# ### Import libraries and packages 
# 
# First, import relevant Python libraries and modules. Use the `pandas` library and the `matplotlib.pyplot` module.

# In[53]:


# Import libraries and packages

import pandas as pd
import matplotlib.pyplot as plt


# ### Load the dataset into a DataFrame
# 
# The dataset provided is in the form of a csv file named `Unicorn_Companies.csv` and contains a subset of data on unicorn companies. As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[54]:


# RUN THIS CELL TO IMPORT YOUR DATA.

### YOUR CODE HERE ###
companies = pd.read_csv("Unicorn_Companies.csv")


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to what you learned about [loading data](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/supplement/MdTG2/reference-guide-import-datasets-using-python) in Python.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the function in the `pandas` library that allows you to read data from a csv file and load the data into a DataFrame.
#  
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `read_csv()` function from the `pandas` library. 
# 
# </details>

# ## Step 2: Data exploration

# ### Display the first 10 rows of the data
# 
# Next, explore the dataset and answer questions to guide your exploration and analysis of the data. To begin, display the first 10 rows of the data to get an understanding of how the dataset is structured.

# In[55]:


# Display the first 10 rows of the data

companies[:10]


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to [the content about exploratory data analysis in Python](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/kfl9b/find-stories-using-the-six-exploratory-data-analysis-practices).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the function in the `pandas` library that allows you to get a specific number of rows from the top of a DataFrame.
#  
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `head()` function from the `pandas` library. 
# 
# </details>

# **Question:** What do you think the "Date Joined" column represents?

#  [Write your response here. Double-click (or enter) to edit.]

# **Question:** What do you think the "Select Investors" column represents?

# [Write your response here. Double-click (or enter) to edit.]

# ### Assess the size of the dataset
# 
# Get a sense of how large the dataset is. The `size` property that DataFrames have can help.

# In[56]:


# How large the dataset is

companies.size


# **Question:** What do you notice about the size of the dataset?

# [Write your response here. Double-click (or enter) to edit.]

# ### Determine the shape of the dataset
# 
# Identify the number of rows and columns in the dataset. The `shape` property that DataFrames have can help.

# In[57]:


# Shape of the dataset

companies.shape


# **Question:** What do you notice about the shape of the dataset?

# [Write your response here. Double-click (or enter) to edit.]

# ### Get basic information about the dataset
# 
# To further understand what the dataset entails, get basic information about the dataset, including the data type of values in each column. There is more than one way to approach this task. In this instance, use the `info()` function from `pandas`.

# In[58]:


# Get information

companies.info()


# **Question:** What do you notice about the type of data in the `Year Founded` column? Refer to the output from using `info()` above. Knowing the data type of this variable is helpful because it indicates what types of analysis can be done with that variable, how it can be aggregated with other variables, and so on.

# [Write your response here. Double-click (or enter) to edit.]

# **Question:** What do you notice about the type of data in the `Date Joined` column? Refer to the output from using `info()` above. Knowing the data type of this variable is helpful because it indicates what types of analysis can be done with that variable and how the variable can be transformed to suit specific tasks.

# [Write your response here. Double-click (or enter) to edit.]

# ## Step 3: Statistical tests

# ### Find descriptive statistics
# 
# Find descriptive statistics and structure your dataset. The `describe()` function from the `pandas` library can help. This function generates statistics for the numeric columns in a dataset. 

# In[59]:


# Get descriptive statistics

companies.describe()


# **Question:** Based on the table of descriptive stats generated above, what do you notice about the minimum value in the `Year Founded` column? This is important to know because it helps you understand how early the entries in the data begin.

# [Write your response here. Double-click (or enter) to edit.]

# **Question:** What do you notice about the maximum value in the `Year Founded` column? This is important to know because it helps you understand the most recent year captured by the data. 

# [Write your response here. Double-click (or enter) to edit.]

# ### Convert the `Date Joined` column to datetime
# 
# Use the `to_datetime()` function from the `pandas` library  to convert the `Date Joined` column to datetime. This splits each value into year, month, and date components. This is an important step in data cleaning, as it makes the data in this column easier to use in tasks you may encounter. To name a few examples, you may need to compare "date joined" between companies or determine how long it took a company to become a unicorn. Having "date joined" in datetime form would help you complete such tasks.

# In[60]:


# Step 1: Use pd.to_datetime() to convert Date Joined column to datetime 
# Step 2: Update the column with the converted values

companies['Date Joined'] = pd.to_datetime(companies['Date Joined'])


# In[61]:


# Use .info() to confirm that the update actually took place

companies.info()


# ### Create a `Year Joined` column
# 
# It is common to encounter situations where you will need to compare the year joined with the year founded. The `Date Joined` column does not just have year—it has the year, month, and date. Extract the year component from the `Date Joined` column and add those year components into a new column to keep track of each company's year joined.

# In[62]:


# Step 1: Use .dt.year to extract year component from Date Joined column
# Step 2: Add the result as a new column named Year Joined to the DataFrame

companies['Year Joined'] = companies['Date Joined'].dt.year


# In[63]:


# Use .head() to confirm that the new column did get added

companies


# ## Step 4: Results and evaluation
# 

# ### Take a sample of the data
# 
# It is not necessary to take a sample of the data in order to conduct the visualizations and EDA that follow. But you may encounter scenarios in the future where you will need to take a sample of the data due to time and resource limitations. For the purpose of developing your skills around sampling, take a sample of the data and work with that sample for the next steps of analysis you want to conduct. Use the `sample()` function for this task.
# 
# - Use `sample()` with the `n` parameter set to `50` to randomly sample 50 unicorn companies from the data. Be sure to specify the `random_state` parameter to ensure reproducibility of your work. Save the result to a variable called `companies_sampled`.

# In[64]:


# Sample the data

companies_sampled = companies.sample(n = 50, random_state = 1)
companies_sampled[:5]


# ### Visualize the time it took companies to reach unicorn status
# 
# Visualize the longest time it took companies to reach unicorn status for each industry represented in the sample. To create a bar plot to visualize this, use the `bar()` function from the `matplotlib.pyplot` module. You'll first need to prepare the data.

# In[65]:


# Prepare data for plotting

companies_sampled['Years to Unicorn'] = companies_sampled['Year Joined'] - companies_sampled['Year Founded']
sampled_plot = (companies_sampled.groupby('Industry')
                .max('Years to Unicorn')
                .sort_values(by = 'Years to Unicorn')
                .reset_index()
               )
sampled_plot


# In[66]:


# Create bar plot
# with the various industries as the categories of the bars
# and the time it took to reach unicorn status as the height of the bars
''
plt.bar(x = sampled_plot['Industry'], height = sampled_plot['Years to Unicorn'])
plt.plot()


# Set title

plt.title('Maximum Years to Billion Dollar Valuation from Random Sample (n=50)')

# Set x-axis label

plt.xlabel('Industry')

# Set y-axis label

plt.ylabel('Years')

# Rotate labels on the x-axis as a way to avoid overlap in the positions of the text

plt.xticks(rotation = 45, horizontalalignment = 'right')

# Display the plot

plt.show()


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# To prepare the data for modeling, begin by creating a column that represents the number of years it took each company to reach unicorn status. 
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
#     
# To prepare the data for modeling, group the dataframe by industry and get the maximum value in the newly created column for each industry.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# You can use the `plt.bar()` to create the bar plot, passing in the categories and heights of the bars.
# 
# You can use `plt.title()`, `plt.xlabel()`, and `plt.ylabel()` to set the title, x-axis label, and y-axis label, respectively. 
# 
# You can use `plt.xticks()` to rotate labels on the x-axis of a plot. The parameters `rotation=45, horizontalalignment='right'` can be passed in to rotate the labels by 45 degrees and align the labels to the right. 
# 
# You can use `plt.show()` to display a plot.
# 
# </details>

# **Question:** What do you observe from this bar plot?

# [Write your response here. Double-click (or enter) to edit.]

# ### Visualize the maximum unicorn company valuation per industry
# 
# Visualize unicorn companies' maximum valuation for each industry represented in the sample. To create a bar plot to visualize this, use the `bar()` function from the `matplotlib.pyplot` module. Before plotting, create a new column that represents the companies' valuations as numbers (instead of strings, as they're currently represented). Then, use this new column to plot your data.

# In[67]:


# Create a column representing company valuation as numeric data 
# Start by getting rid of the first ($) and last (B) index in the string

y=[]
for x in companies_sampled['Valuation']:
    
    y.append(int(x[1:-1]))
    
companies_sampled.insert(2, 'Numeric Valuation (Billions)', y)


# In[93]:


# Create bar plot
# with the various industries as the categories of the bars
# and the maximum valuation for each industry as the height of the bars

sampled_plot = (companies_sampled[['Industry', 'Numeric Valuation (Billions)']]
                .groupby('Industry')
                .max()
                .sort_values(by = 'Numeric Valuation (Billions)', ascending = False)
                .reset_index()
               )

plt.bar(sampled_plot['Industry'], sampled_plot['Numeric Valuation (Billions)'])

# Set title

plt.title('Biggest Companies by Valuation (Sample, n = 50)')


# Set x-axis label

plt.xlabel('Industry')

# Set y-axis label

plt.ylabel("Valuation ($ Billions)")

# Rotate labels on the x-axis as a way to avoid overlap in the positions of the text  

plt.xticks(rotation = 45, horizontalalignment = 'right')

# Display the plot

plt.show()


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Repeat the process from the last task, only this time with different variables.
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the function in the `matplotlib.pyplot` module that allows you to create a bar plot, specifying the category and height for each bar. 
# 
# Use the functions in the `matplotlib.pyplot` module that allow you to set the title, x-axis label, and y-axis label of plots. In that module, there are also functions for rotating the labels on the x-axis and displaying the plot. 
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `plt.bar()` to create the bar plot, passing in the categories and heights of the bars.
# 
# Use `plt.title()`, `plt.xlabel()`, and `plt.ylabel()` to set the title, x-axis label, and y-axis label, respectively. 
# 
# Use `plt.xticks()` to rotate labels on the x-axis of a plot. The parameters `rotation=45, horizontalalignment='right'` can be passed in to rotate the labels by 45 degrees and align the labels to the right. 
# 
# Use `plt.show()` to display a plot.
# 
# </details>

# **Question:** What do you observe from this bar plot? 

# [Write your response here. Double-click (or enter) to edit.]

# ## Considerations

# **What are some key takeaways that you learned from this lab?**

# [Write your response here. Double-click (or enter) to edit.]

# **What findings would you share with others?**

# [Write your response here. Double-click (or enter) to edit.]

# **What recommendations would you share with stakeholders based on these findings?**

# [Write your response here. Double-click (or enter) to edit.]

# **References**
# 
# Bhat, M.A. (2022, March). [*Unicorn Companies*](https://www.kaggle.com/datasets/mysarahmadbhat/unicorn-companies). 
# 
# 

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
