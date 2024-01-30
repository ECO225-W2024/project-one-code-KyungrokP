#!/usr/bin/env python
# coding: utf-8

# # How are different characteristics of Business affect the average DCA loan amount? 
# ---------------------------------

# ##  Table of Contents 
# ### 1. [Introduction](#Introduction)
# ### 2. [Data Cleaning and Summaries](#data_cleaning)
# ### 3. [Summary Statistics Tables](#summary_statistics_tables)
# ### 4. [Plots, Histograms and Figures ](#plots_and_figures)
# ### 5. [Conclusion](#Conclusion)     
# ### 6. [Weakness and Next steps](#final_paragraph)

# ----------------------------------------------------------------------------------------------

# ## Introduction
# ----------------------------------

# ## Data Cleaning and Summaries  <a name="data_cleaning"></a>

# In[487]:


# Workspace Setup
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# In[457]:


DCA_loan_data = pd.read_csv('Raw_Data.csv') # import raw DCA loan dataset
                                            # from local directory

DCA_loan_data = DCA_loan_data[['Amount (USD)', 'Business Sector', 
                               'Is Woman Owned?', 'Is First Time Borrower?', 
                               'Business Size']] # select the columns according 
                                                 # to the research topic
DCA_loan_data = DCA_loan_data[~DCA_loan_data['Is Woman Owned?']
                              .isin([4,19,86,123,4732,21566])] 
# remove rows which include values which are not 0 or 1

DCA_loan_data = DCA_loan_data[~DCA_loan_data['Is First Time Borrower?']
                              .isin([21,26,170,390])]
# remove rows which include values which are not 0 or 1

DCA_loan_data


# -------------------------------------

# ## Summary Statistics Tables <a name="summary_statistics_tables"></a>

# In[458]:


des = DCA_loan_data.groupby('Is Woman Owned?').size()
des = pd.DataFrame(des)
des = des.rename(columns = {0:'Count'})
des


# In[459]:


des2 = DCA_loan_data.groupby('Is First Time Borrower?').size()
des2 = pd.DataFrame(des2)
des2 = des2.rename(columns = {0:'Count'})
des2


# In[460]:


des3 = DCA_loan_data['Amount (USD)'].mean()
des4 = DCA_loan_data['Amount (USD)'].std()
des5 = pd.DataFrame({'Mean':[des3], 'Standard Deviation':[des4]})
des5 = des5.rename(index = {0:'Amount (USD)'})
des5


# In[461]:


des6 = DCA_loan_data.groupby('Business Size').size()
des6 = pd.DataFrame(des6)
des6 = des6.rename(columns = {0:'Count'})
des6 = des6.reindex(['1--5','6--10', '11--50', '51--100', '>100'])
des6


# In[462]:


des7 = DCA_loan_data.groupby('Business Sector').size()
des7 = pd.DataFrame(des7)
des7 = des7.rename(columns = {0:'Count'})
des7


# ----------------------------------------------------

# ## Plots, Histograms and Figures <a name="plots_and_figures"></a>

# In[484]:


boxplt1 = DCA_loan_data.boxplot(column = 'Amount (USD)', 
                                by = 'Is Woman Owned?', showfliers=False)
#ax.suptitle('what is happening')
boxplt1.set_xlabel('x data')
boxplt1.set_ylabel('y data')
boxplt1.set_title('Hi')
plt.suptitle('')


# In[486]:


boxplt2 = DCA_loan_data.boxplot(column = 'Amount (USD)',
                                by = 'Is First Time Borrower?', showfliers = False)
boxplt2.set_xlabel('x data')
boxplt2.set_ylabel('y data')
boxplt2.set_title('whatup')
plt.suptitle('')


# In[465]:


df_summary = df.groupby(['Is Woman Owned?', 
                         'Business Sector', 'Business Size']).agg(
    {'Amount (USD)': [np.sum, pd.Series.count, np.mean, np.std]})

df_summary.columns = ['Sum', 'Count', 'Mean', 'Std']
df_summary = df_summary.reindex(['1--5','6--10', '11--50', 
                                 '51--100', '>100'], level=2)
df_summary


# In[490]:


df2 = df_summary.groupby(['Business Sector', 
                          'Business Size'])['Mean'].diff()
df2 = pd.DataFrame(df2)
df2 = df2.reset_index()
df2 = df2.drop('Is Woman Owned?', axis = 1)
df2 = df2.dropna()
df2.set_index('Business Sector', inplace=True)
df2=df2.rename(columns = {'Mean':'Difference in Mean Loan Amount(USD)'})
df2.head()


# In[467]:


df_summary2 = df.groupby(['Is First Time Borrower?', 
                          'Business Sector', 'Business Size']).agg(
    {'Amount (USD)': [np.sum, pd.Series.count, np.mean, np.std]})

df_summary2.columns = ['Sum of Loan(USD)', 'Count', 
                       'Average Loan Amount(USD)', 'Standard Deviation(USD)']
df_summary2 = df_summary2.reindex(['1--5','6--10', 
                                   '11--50', '51--100', '>100'], level=2)
df_summary2


# In[491]:


df3 = df_summary2.groupby(['Business Sector', 
                           'Business Size'])['Average Loan Amount(USD)'].diff()
df3 = pd.DataFrame(df3)
df3 = df3.reset_index()
df3 = df3.drop('Is First Time Borrower?', axis = 1)
df3 = df3.dropna()
df3.set_index('Business Sector', inplace=True)
df3 = df3.rename(columns = {'Average Loan Amount(USD)':
                            'Difference in Mean Loan Amount(USD)'})
df3.head()


# In[492]:


df3 = df3.reset_index()

ax1 = df3.set_index(['Business Sector', 
                     'Business Size'])['Difference in Mean Loan Amount(USD)'].nlargest(5).plot.bar()

ax1.set_title('test title')
ax1.set_xlabel('x data')
ax1.set_ylabel('y data')


# In[475]:


ax2 = df3.set_index(['Business Sector', 'Business Size'])['Difference in Mean Loan Amount(USD)'].nsmallest(5).plot.bar()
ax2.set_title('test title')
ax2.set_xlabel('x data')
ax2.set_ylabel('y data')


# ----------------------------------------------------

# ## Conclusion

# In[ ]:





# In[ ]:





# ## Weakness and Next steps <a name="final_paragraph"></a>

# In[ ]:




