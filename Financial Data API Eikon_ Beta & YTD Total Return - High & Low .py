#!/usr/bin/env python
# coding: utf-8

# ## Financial Data in Python 
# 
# 
# ### Author: Ignacio González Bohórquez 
# 
# What is being explained in this Notebook: 
# 
# Remember to follow on instagram @codewithnacho 
# 
# - Methods: timeseries ,retrieving news and  plots 
# 
# - Beta & YTD Total Return
# 
# - High & Low 

# In[35]:


pip install eikon


# In[37]:


pip install cufflinks


# In[39]:


import numpy as np 
import pandas as pd 
import cufflinks as cf 
import configparser as cp 
import eikon as ek 
import sys


# In[41]:


ek.set_app_key("Yourownkey")


# In[74]:


Amazon_stock = ek.get_timeseries("AMZN.O", fields="*", start_date="2019-01-01", end_date="2020-07-08")


# In[81]:


Amazon_stock.iplot(kind="lines")


# In[52]:


Amazon_stock["CLOSE"].iplot()


# In[55]:


ek.get_news_headlines("R:AMZN.O", date_from = "2020-07-08T13:00:00", date_to="2020-07-08T22:00:00", count = 5)


# In[65]:


Amazon_stock_1 = ek.get_timeseries("AMZN.O", fields="CLOSE", start_date="2019-01-01", end_date="2020-07-08")


# In[66]:


Amazon_stock_1 


# In[95]:


Amazon_stock_1["DROP SIZE"]= Amazon_stock_1.pct_change()


# In[96]:


Amazon_stock_1


# In[72]:


Amazon_stock_2 = Amazon_stock_1["DROP SIZE"]*100


# In[157]:


Amazon_stock_2


# In[159]:


Portfolio = ["GOOG.O", "AMZN.O", "IBM", "TSLA.O"]


# In[165]:


Portfolio_1 = ek.get_timeseries(Portfolio, fields="CLOSE", start_date="2020-01-01",end_date="2020-07-09")


# In[167]:


Portfolio_1.iplot()


# In[169]:


data_grid, err = ek.get_data(["GOOG.O", "AMZN.O", "IBM", "TSLA.O"], ["TR.TotalReturnYTD", "TR.WACCBeta", "YRHIGH", "YRLOW"])


# In[171]:


data_grid


# In[176]:


data_grid.set_index("Instrument")[["YTD Total Return", "Beta"]].iplot(kind="bar",subplots=True)


# In[178]:


Portfolio_1.describe()


# In[239]:


Portfolio


# In[241]:


ek.get_symbology(Portfolio, from_symbol_type = "RIC", to_symbol_type = "ISIN")


# In[243]:


data_grid.set_index("Instrument")[["YRHIGH", "YRLOW"]].iplot(kind="bar")


# In[246]:


Portfolio[1]


# In[248]:


Noticias = ek.get_news_headlines("R:%s PRODUCTION IN ENGLISH" % Portfolio[1], date_from="2020-01-01", date_to="2020-07-10", count = 10)


# In[250]:


Noticias 


# In[252]:


Titulares_Amazon_reciente = ek.get_news_headlines('AMZN.O')


# In[255]:


Portfolio


# In[254]:


Titulares_Amazon_reciente

