#!/usr/bin/env python
# coding: utf-8

# ## Task 1: Exploratory Data Analysis on Financial News

# In[41]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
import os


# In[ ]:


# Add src directory to path
sys.path.append(str(Path.cwd().parent / "src"))
from plot_utils import save_plot  # Custom plot saving function


# In[ ]:


# Download NLTK resources
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)


# In[ ]:


# Set paths
BASE_DIR = Path.cwd().parent
DATA_DIR = BASE_DIR / "data"
PLOTS_DIR = BASE_DIR / "plots"


# In[42]:


#Load the data
news_df = pd.read_csv(r"C:\Users\jilow\OneDrive\Documents\FIndata\raw_analyst_ratings.csv")


# In[45]:


print("\n Dataset Info:")
news_df.head()


# In[46]:


news_df.info()


# In[ ]:


# Data Preparation
# Parse dates and add features
news_df['date'] = pd.to_datetime(news_df['date'], errors='coerce')
news_df['headline_length'] = news_df['headline'].str.len()


# In[48]:


# Descriptive statistics of headline lengths
print(news_df['headline_length'].describe())
plt.figure(figsize=(8,4))
plt.hist(news_df['headline_length'].dropna(), bins=30)
plt.title("Headline Length Distribution")
plt.xlabel("Characters")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# In[49]:


# Publisher analysis
publisher_counts = news_df['publisher'].value_counts().reset_index()
publisher_counts.columns = ['publisher', 'count']
publisher_counts.head(10)


# In[50]:


plt.figure(figsize=(10,5))
plt.bar(publisher_counts['publisher'][:10], publisher_counts['count'][:10])
plt.xticks(rotation=45)
plt.title("Top 10 Publishers by Article Count")
plt.ylabel("Articles")
plt.tight_layout()
plt.show()


# In[51]:


# Daily publication trend
daily_counts = news_df.set_index('date').resample('D').size()
plt.figure(figsize=(10,4))
daily_counts.plot()
plt.title("Daily Article Publication Frequency")
plt.ylabel("Count")
plt.tight_layout()
plt.show()


# In[52]:


# Time-of-day publication analysis
plt.figure(figsize=(8,4))
news_df['hour'] = news_df['date'].dt.hour
plt.hist(news_df['hour'].dropna(), bins=24, range=(0,24), align='left')
plt.xticks(range(24))
plt.title("Publication Time of Day")
plt.xlabel("Hour")
plt.ylabel("Articles")
plt.tight_layout()
plt.show()


# In[53]:


# Publisher domain analysis
news_df['publisher_domain'] = news_df['publisher'].apply(lambda x: str(x).split('@')[-1] if '@' in str(x) else x)
domain_counts = news_df['publisher_domain'].value_counts().reset_index()
domain_counts.columns = ['domain', 'count']
print(domain_counts.head(10))


# In[54]:


# Text analysis
nltk_stopwords = stopwords.words('english')
cv = CountVectorizer(stop_words=nltk_stopwords, max_features=20)
X = cv.fit_transform(news_df['headline'].fillna(''))
terms = cv.get_feature_names_out()
counts = X.toarray().sum(axis=0)
keywords_df = pd.DataFrame({'term': terms, 'count': counts})
print(keywords_df.sort_values('count', ascending=False).head(10))

