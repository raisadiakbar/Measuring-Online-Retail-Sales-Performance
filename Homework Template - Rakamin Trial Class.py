#!/usr/bin/env python
# coding: utf-8

# ### Homework Rakamin Trial Class - Mini Case

# # Mengukur Performa Penjualan Ritel Online

# ## Load Data

# In[33]:


import pandas as pd

data = pd.read_csv("C:\\Users\\mohra\\Downloads\\online_retail_II.csv")
data


# ## Section 1

# ### Create New Feature: Year

# In[34]:


data["InvoiceDate"] = pd.to_datetime(data["InvoiceDate"])
data["Year"] = data["InvoiceDate"].dt.year

data


# ### Filtering Data

# In[35]:


sales = data[(data["Quantity"] > 0) & (~data["Invoice"].str.startswith("C"))]

sales


# ### Create New Feature: Revenue

# In[36]:


sales["Revenue"] = sales["Quantity"] * sales["Price"]

sales


# ### Average of Revenue per Year

# In[37]:


average_per_year = sales.groupby("Year")["Revenue"].mean()

average_per_year


# ### Interpretation

# In[38]:


# Interpretation of Section 1
from IPython.display import Markdown

# Calculate the average revenue per year
average_per_year = sales.groupby("Year")["Revenue"].mean()

# Generate Markdown interpretation
interpretation = "### Interpretation of Section 1\n\n"
interpretation += "The table below shows the average annual revenue for each year:\n\n"
interpretation += "| Year | Average Revenue |\n"
interpretation += "|------|-----------------|\n"

for year, average_revenue in average_revenue_per_year.items():
    interpretation += f"| {year} | {average_revenue:.2f} |\n"

# Display the interpretation in Markdown format
Markdown(interpretation)


# ## Section 2

# ### Filtering Data 

# #### Customers who finished their purchases

# In[39]:


finished = sales.dropna(subset=["Customer ID"])

finished


# #### Customers who canceled their purchases

# In[40]:


canceled = sales[sales['Invoice'].str.startswith('C')]

canceled


# ### Number of Finished and Canceled Transactions Each Year

# In[41]:


finished_transaction = finished.groupby('Year').size()
canceled_transaction = canceled.groupby('Year').size()

finished_transaction


# In[42]:


canceled_transaction


# ### Cancellation Rate

# In[43]:


canceled_rate = (canceled_transaction / (canceled_transaction + finished_transaction) * 100)

canceled_rate


# ### Interpretation

# In[44]:


# Interpretation of Section 2
from IPython.display import Markdown

# Customers who finished their purchases
finished = sales.dropna(subset=["Customer ID"])

# Customers who canceled their purchases
canceled = sales[sales['Invoice'].str.startswith('C')]

# Number of Finished and Canceled Transactions Each Year
finished_transaction = finished.groupby('Year').size()
canceled_transaction = canceled.groupby('Year').size()

# Cancellation Rate
canceled_rate = (canceled_transaction / (canceled_transaction + finished_transaction) * 100)

# Generate Markdown interpretation
interpretation_section2 = "### Interpretation of Section 2\n\n"
interpretation_section2 += "In Section 2, we analyze the transactions of customers who either finished their purchases or canceled them.\n\n"
interpretation_section2 += f"There were {finished_transaction.sum()} unique customers who successfully finished their transactions, "
interpretation_section2 += f"and {canceled_transaction.sum()} unique customers who canceled their purchases during the analyzed period.\n\n"
interpretation_section2 += "The total number of finished transactions and canceled transactions each year are as follows:\n\n"
interpretation_section2 += "| Year | Finished Transactions | Canceled Transactions |\n"
interpretation_section2 += "|------|------------------------|------------------------|\n"

for year in finished_transaction.index:
    interpretation_section2 += f"| {year} | {finished_transaction[year]} | {canceled_transaction.get(year, 0)} |\n"

interpretation_section2 += f"\nThe overall cancellation rate, which represents the percentage of customers who canceled their "
interpretation_section2 += f"orders out of all customers, is {canceled_rate.values[0]:.2f}%."

# Display the interpretation in Markdown format
Markdown(interpretation_section2)


# In[ ]:




