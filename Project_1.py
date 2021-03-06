#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import matplotlib


# In[2]:


# Store filepath in a variable
# Please note to that you need to change this path if different from the actual path 

file_one = "../Resources/CO2Emission.csv"
file_two = "../Resources/CO2GDP.csv"
file_three = "../Resources/CO2POP.csv"
file_four = "../Resources/Countries2.csv"
file_five = "../Resources/allcountries.csv"


# In[3]:


# Read our Data file with the pandas library
# Not every CSV requires an encoding, but be aware this can come up

# CO2 emission 
file_one_df = pd.read_csv(file_one, encoding="ISO-8859-1")

# CO2 emission per GDP
file_two_df = pd.read_csv(file_two, encoding="ISO-8859-1")

# CO2 emission per capita
file_three_df = pd.read_csv(file_three, encoding="ISO-8859-1")

# Map data
allcountries_df = pd.read_csv(file_five, encoding="ISO-8859-1")

Countries_df = pd.read_csv(file_four, encoding="ISO-8859-1")


# In[4]:


# Show just the header
allcountries_df


# In[5]:


# Show just the header

file_two_df.head()


# In[6]:


# Show just the header
file_three_df.head()


# In[7]:


file_one_df.count()


# In[8]:


file_two_df.count()


# In[9]:


# Clean up the input files by dropping row with no data

file_one_df = file_one_df.dropna(0,how='any')

file_two_df = file_two_df.dropna(0,how='any')

file_three_df = file_three_df.dropna(0,how='any')


# In[10]:


# Test number of rows

file_one_df.count()


# In[11]:


# Name of the desired coulumns in the csv files

columns = [
    "1991",
    "1992",
    "1993",
    "1994",
    "1995",
    "1996",
    "1997",
    "1998",
    "1999",
    "2000",
    "2001",
    "2002",
    "2003",
    "2004",
    "2005",
    "2006",
    "2007",
    "2008",
    "2009",
    "2010",
    "2011",
    "2012",
    "2013",
    "2014",
    "2015",
    "2016",
    "2017",
    "2018",
    "2019"    
]

# Creat data frame for Canada. df_1, df_2, df_3 represent CO2, CO2/GDP, and CO2/Pop
Canada_df_1 = file_one_df.loc[file_one_df["Region/Country/Economy"] == "Canada", columns]
Canada_df_2 = file_two_df.loc[file_two_df["Region/Country/Economy"] == "Canada", columns]
Canada_df_3 = file_three_df.loc[file_three_df["Region/Country/Economy"] == "Canada", columns]

# Creat data frame for US. df_1, df_2, df_3 represent CO2, CO2/GDP, and CO2/Pop
US_df_1 = file_one_df.loc[file_one_df["Region/Country/Economy"] == "United States", columns]
US_df_2 = file_two_df.loc[file_two_df["Region/Country/Economy"] == "United States", columns]
US_df_3 = file_three_df.loc[file_three_df["Region/Country/Economy"] == "United States", columns]

# Creat data frame for UK. df_1, df_2, df_3 represent CO2, CO2/GDP, and CO2/Pop
UK_df_1 = file_one_df.loc[file_one_df["Region/Country/Economy"] == "United Kingdom", columns]
UK_df_2 = file_two_df.loc[file_two_df["Region/Country/Economy"] == "United Kingdom", columns]
UK_df_3 = file_three_df.loc[file_three_df["Region/Country/Economy"] == "United Kingdom", columns]


# Creat data frame for Germany. df_1, df_2, df_3 represent CO2, CO2/GDP, and CO2/Pop
Germany_df_1 = file_one_df.loc[file_one_df["Region/Country/Economy"] == "Germany", columns]
Germany_df_2 = file_two_df.loc[file_two_df["Region/Country/Economy"] == "Germany", columns]
Germany_df_3 = file_three_df.loc[file_three_df["Region/Country/Economy"] == "Germany", columns]


# Creat data frame for Japan. df_1, df_2, df_3 represent CO2, CO2/GDP, and CO2/Pop
Japan_df_1 = file_one_df.loc[file_one_df["Region/Country/Economy"] == "Japan", columns]
Japan_df_2 = file_two_df.loc[file_two_df["Region/Country/Economy"] == "Japan", columns]
Japan_df_3 = file_three_df.loc[file_three_df["Region/Country/Economy"] == "Japan", columns]


# Creat data frame for Italy. df_1, df_2, df_3 represent CO2, CO2/GDP, and CO2/Pop
Italy_df_1 = file_one_df.loc[file_one_df["Region/Country/Economy"] == "Italy", columns]
Italy_df_2 = file_two_df.loc[file_two_df["Region/Country/Economy"] == "Italy", columns]
Italy_df_3 = file_three_df.loc[file_three_df["Region/Country/Economy"] == "Italy", columns]


# Creat data frame for France. df_1, df_2, df_3 represent CO2, CO2/GDP, and CO2/Pop
France_df_1 = file_one_df.loc[file_one_df["Region/Country/Economy"] == "France", columns]
France_df_2 = file_two_df.loc[file_two_df["Region/Country/Economy"] == "France", columns]
France_df_3 = file_three_df.loc[file_three_df["Region/Country/Economy"] == "France", columns]


# Creat data frame for China. df_1, df_2, df_3 represent CO2, CO2/GDP, and CO2/Pop
China_df_1 = file_one_df.loc[file_one_df["Region/Country/Economy"] == "People's Rep. of China", columns]
China_df_2 = file_two_df.loc[file_two_df["Region/Country/Economy"] == "People's Rep. of China", columns]
China_df_3 = file_three_df.loc[file_three_df["Region/Country/Economy"] == "People's Rep. of China", columns]



# Creat data frame for Russia. df_1, df_2, df_3 represent CO2, CO2/GDP, and CO2/Pop
Russia_df_1 = file_one_df.loc[file_one_df["Region/Country/Economy"] == "Russian Federation", columns]
Russia_df_2 = file_two_df.loc[file_two_df["Region/Country/Economy"] == "Russian Federation", columns]
Russia_df_3 = file_three_df.loc[file_three_df["Region/Country/Economy"] == "Russian Federation", columns]

Canada_df_1


# In[12]:


# Test the data frames
# Canada_df_2.head()
# UK_df_3.head() 
# Germany_df.head() 
# Japan_df.head() 
China_df_3.head() 
# France_df.head() 
# China_df.head() 
# Russia_df.head() 
# US_df.head()
# Canada_df_1.head()


# In[13]:


# Change the name of rows to give them an appropriate name 


Canada_df_1_New = Canada_df_1.rename(index = {0:'CO2Emission'})
Canada_df_2_New = Canada_df_2.rename(index = {0:'CO2/GDP'})
Canada_df_3_New = Canada_df_3.rename(index = {0:'CO2/POP'})

US_df_1_New = US_df_1.rename(index = {3:'CO2Emission'})
US_df_2_New = US_df_2.rename(index = {3:'CO2/GDP'})
US_df_3_New = US_df_3.rename(index = {3:'CO2/POP'})

UK_df_1_New = UK_df_1.rename(index = {37:'CO2Emission'})
UK_df_2_New = UK_df_2.rename(index = {37:'CO2/GDP'})
UK_df_3_New = UK_df_3.rename(index = {37:'CO2/POP'})

Germany_df_1_New = Germany_df_1.rename(index = {18:'CO2Emission'})
Germany_df_2_New = Germany_df_2.rename(index = {18:'CO2/GDP'})
Germany_df_3_New = Germany_df_3.rename(index = {18:'CO2/POP'})

Japan_df_1_New = Japan_df_1.rename(index = {7:'CO2Emission'})
Japan_df_2_New = Japan_df_2.rename(index = {7:'CO2/GDP'})
Japan_df_3_New = Japan_df_3.rename(index = {7:'CO2/POP'})

Italy_df_1_New = Italy_df_1.rename(index = {23:'CO2Emission'})
Italy_df_2_New = Italy_df_2.rename(index = {23:'CO2/GDP'})
Italy_df_3_New = Italy_df_3.rename(index = {23:'CO2/POP'})

France_df_1_New = France_df_1.rename(index = {17:'CO2Emission'})
France_df_2_New = France_df_2.rename(index = {17:'CO2/GDP'})
France_df_3_New = France_df_3.rename(index = {17:'CO2/POP'})

China_df_1_New = China_df_1.rename(index = {119:'CO2Emission'})
China_df_2_New = China_df_2.rename(index = {119:'CO2/GDP'})
China_df_3_New = China_df_3.rename(index = {119:'CO2/POP'})



Russia_df_1_New = Russia_df_1.rename(index = {57:'CO2Emission'})
Russia_df_2_New = Russia_df_2.rename(index = {57:'CO2/GDP'})
Russia_df_3_New = Russia_df_3.rename(index = {57:'CO2/POP'})

China_df_3_New


# In[14]:


# Transpose the dataframes


Canada_df_1=Canada_df_1_New.T
Canada_df_2=Canada_df_2_New.T
Canada_df_3= Canada_df_3_New.T

US_df_1= US_df_1_New.T
US_df_2= US_df_2_New.T
US_df_3= US_df_3_New.T

UK_df_1= UK_df_1_New.T
UK_df_2= UK_df_2_New.T
UK_df_3= UK_df_3_New.T


Germany_df_1= Germany_df_1_New.T
Germany_df_2= Germany_df_2_New.T
Germany_df_3= Germany_df_3_New.T

Japan_df_1= Japan_df_1_New.T
Japan_df_2= Japan_df_2_New.T
Japan_df_3= Japan_df_3_New.T

Italy_df_1= Italy_df_1_New.T
Italy_df_2= Italy_df_2_New.T
Italy_df_3= Italy_df_3_New.T

France_df_1= France_df_1_New.T
France_df_2= France_df_2_New.T
France_df_3= France_df_3_New.T

China_df_1= China_df_1_New.T
China_df_2= China_df_2_New.T
China_df_3= China_df_3_New.T

Russia_df_1 = Russia_df_1_New.T
Russia_df_2 = Russia_df_2_New.T
Russia_df_3 = Russia_df_3_New.T


China_df_3


# In[15]:


# Combine all the information of a country into a single dataframe of the name of that Country 

frames = [Canada_df_1, Canada_df_2, Canada_df_3]
Canada = pd.concat([Canada_df_1, Canada_df_2, Canada_df_3], axis=1)


frames = [US_df_1, US_df_2, US_df_3]
US = pd.concat([US_df_1, US_df_2, US_df_3], axis=1)


frames = [UK_df_1, UK_df_2, UK_df_3]
UK = pd.concat([UK_df_1, UK_df_2, UK_df_3], axis=1)

frames = [Germany_df_1, Germany_df_2, Germany_df_3]
Germany = pd.concat([Germany_df_1, Germany_df_2, Germany_df_3], axis=1)

frames = [Japan_df_1, Japan_df_2, Japan_df_3]
Japan = pd.concat([Japan_df_1,Japan_df_2, Japan_df_3], axis=1)

frames = [Italy_df_1, Italy_df_2, Italy_df_3]
Italy = pd.concat([Italy_df_1,Italy_df_2, Italy_df_3], axis=1)

frames = [France_df_1, France_df_2, France_df_3]
France = pd.concat([France_df_1,France_df_2, France_df_3], axis=1)

frames = [China_df_1, China_df_2, China_df_3]
China = pd.concat([China_df_1,China_df_2, China_df_3], axis=1)

frames = [Russia_df_1, Russia_df_2, Russia_df_3]
Russia = pd.concat([Russia_df_1,Russia_df_2, Russia_df_3], axis=1)

Russia


# In[16]:


Canada['CO2Emission'] = Canada['CO2Emission'].astype(float)
Canada['CO2/GDP'] = Canada['CO2/GDP'].astype(float)
Canada['CO2/POP'] = Canada['CO2/POP'].astype(float)

US['CO2Emission'] = US['CO2Emission'].astype(float)
US['CO2/GDP'] = US['CO2/GDP'].astype(float)
US['CO2/POP'] = US['CO2/POP'].astype(float)

UK['CO2Emission'] = UK['CO2Emission'].astype(float)
UK['CO2/GDP'] = UK['CO2/GDP'].astype(float)
UK['CO2/POP'] = UK['CO2/POP'].astype(float)

Germany['CO2Emission'] = Germany['CO2Emission'].astype(float)
Germany['CO2/GDP'] = Germany['CO2/GDP'].astype(float)
Germany['CO2/POP'] = Germany['CO2/POP'].astype(float)

Japan['CO2Emission'] = Japan['CO2Emission'].astype(float)
Japan['CO2/GDP'] = Japan['CO2/GDP'].astype(float)
Japan['CO2/POP'] = Japan['CO2/POP'].astype(float)


France['CO2Emission'] = France['CO2Emission'].astype(float)
France['CO2/GDP'] = France['CO2/GDP'].astype(float)
France['CO2/POP'] = France['CO2/POP'].astype(float)

China['CO2Emission'] = China['CO2Emission'].astype(float)
China['CO2/GDP'] = China['CO2/GDP'].astype(float)
China['CO2/POP'] = China['CO2/POP'].astype(float)

Russia['CO2Emission'] = Russia['CO2Emission'].astype(float)
Russia['CO2/GDP'] = Russia['CO2/GDP'].astype(float)
Russia['CO2/POP'] = Russia['CO2/POP'].astype(float)

Italy['CO2Emission'] = Italy['CO2Emission'].astype(float)
Italy['CO2/GDP'] = Italy['CO2/GDP'].astype(float)
Italy['CO2/POP'] = Italy['CO2/POP'].astype(float)


# In[17]:


# Split each country's dataframe to two dataframes of before and after Paris agreemnets

Canada_before = Canada.iloc[:24,:] 
Canada_after = Canada.iloc[25:,:]

US_before = US.iloc[:24,:] 
US_after = US.iloc[25:,:]

UK_before = UK.iloc[:24,:] 
UK_after = UK.iloc[25:,:]

Germany_before = Germany.iloc[:24,:] 
Germany_after = Germany.iloc[25:,:]

Japan_before = Japan.iloc[:24,:] 
Japan_after = Japan.iloc[25:,:]

Italy_before = Italy.iloc[:24,:] 
Italy_after = Italy.iloc[25:,:]

France_before = France.iloc[:24,:] 
France_after = France.iloc[25:,:]

Russia_before = Russia.iloc[:24,:] 
Russia_after = Russia.iloc[25:,:]

China_before = China.iloc[:24,:] 
China_after = China.iloc[25:,:]


# In[18]:

'''
    Now, you can calculate the statistics of Total, and before and after Paris agreemnet of each country. 

    For example 
    Canada.mean() gives you the mean of CO2 emission, CO2/GDP, and CO2/POP for the period of 1991-2019
    Canada_before.mean() gives you the mean of CO2 emission, CO2/GDP, and CO2/POP for the period of 1991-2015
    Canada_after.mean() gives you the mean of CO2 emission, CO2/GDP, and CO2/POP for the period of 2016-2019

'''


Canada_after.mean()


# 

# In[19]:


France_before.mean()


# In[20]:


# df = px.data.gapminder().query("year==2007")

df = Countries_df

fig = px.scatter_geo(df, locations="iso_alpha", color="continent ",
                     hover_name="country ", size="pop",
                    animation_frame="year ",
                     projection="equirectangular")
fig.show()


# In[21]:


plotly.offline.plot(fig, filename='C:/Users/aragh\Desktop/canada_offline.html')


# In[22]:


df = allcountries_df

figemission = px.scatter_geo(df, locations="isoalpha", color="continent",
                     hover_name="country", size="co2emission",
                    animation_frame="year",color_continuous_scale=px.colors.cyclical.IceFire,size_max=15, 
                     projection="equirectangular")
figemission.show()
plotly.offline.plot(figemission, filename='../Graphic/emission_offline.html')


# In[23]:


df = allcountries_df

figGDP = px.scatter_geo(df, locations="isoalpha", color="country",
                     hover_name="country", size="co2/gdp",
                    animation_frame="year",
                     projection="equirectangular")
figGDP.show()
plotly.offline.plot(figGDP, filename='../Graphic/GDP_offline.html')


# In[24]:


df = allcountries_df

figPOP = px.scatter_geo(df, locations="isoalpha", color="country",
                     hover_name="country", size="co2/pop",
                    animation_frame="year",
                     projection="equirectangular")
figPOP.show()
plotly.offline.plot(figPOP, filename='../Graphic/POP_offline.html')


# In[25]:


df = allcountries_df

figemission1 = px.choropleth(df, locations="isoalpha", color="co2emission", hover_name="country", animation_frame="year",
                        range_color=[1000,6000])
figemission1.show()
plotly.offline.plot(figemission1,  filename='../Graphic/emission1_offline.html')


# In[26]:


df = allcountries_df

figcountries = px.choropleth(df, locations="isoalpha", color="country", hover_name="country", 
                             range_color=[1000,6000])
figcountries.show()

plotly.offline.plot(figcountries,  filename='../Graphic/countries_offline.html')


# In[41]:


df = allcountries_df

figtrend = px.line(df, x="year", y="co2emission", color="continent", line_group="country", hover_name="country",
        line_shape="spline", render_mode="svg")

figtrend.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    )
)

figtrend.show()
plotly.offline.plot(figtrend,  filename='../Graphic/Trend')


# In[40]:


df = allcountries_df

fig = px.scatter(df, x="co2emission", y="co2/gdp", animation_frame="year", animation_group="country",
           size="co2emission", color="continent", hover_name="country", facet_col="continent",
           log_x=True, size_max=45, range_x=[100,10000], range_y=[0,3])
fig.show()
plotly.offline.plot(fig,  filename='../Graphic/Group')

