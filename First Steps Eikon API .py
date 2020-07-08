#!/usr/bin/env python
# coding: utf-8

# Para empezar vamos a instalar la API de eikon y cufflinks antes de importar las librerias 

# In[2]:


pip install eikon


# In[3]:


pip install cufflinks #cufflinks nos va a servir para realizar visualizaciones 


# In[7]:


#Ahora importamos las librerias 
import numpy as np
import pandas as pd
import cufflinks as cf
import configparser as cp 
import sys 
import eikon as ek


# In[9]:


#Despues de haber importado las librerias vamos a obtener la API en nuestro cuaderno tras haber previamente haberla instalado en nuestro dispositivo 

ek.set_app_key("350948032b134e009f4e0dc76b274c3f6642cd16")#me genera error al no haber importado la libreria de eikon 


# In[11]:


#Para empezar a trabajar vamos por ejemplo utilizar la información financiera de Amazon 

Amazon_stock = ek.get_timeseries("AMZN.O", fields="*", start_date="2019-01-01", end_date="2020-07-06")


# In[13]:


Amazon_stock #Y es asi como obtenemos los datos financieros 


# In[17]:


Amazon_stock.describe()#Para ver un summary statistics hacemmos describe de cada columna 


# In[19]:


#Si queremos ver como el precio de cierre a fluctuado a lo largo del tiempo hacemos 

#BUENO ESTO SERÍA TODO POR EL VIDEO DE HOY RECUERDEN SUSCRIBIRSE DARLE LIKE Y COMPARTIRLO :) LOL 

Amazon_stock["CLOSE"].iplot()

