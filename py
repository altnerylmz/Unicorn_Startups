import pandas as pd 

df = pd.read_csv(r"C:\Users\HP Spectre\Downloads\unicorns.csv")

df.head()

df.tail()

df.shape

df.columns

df.duplicated().sum()

df.isnull().sum()

df['Investors'] = df['Investors'].fillna('Not Available')


df.isnull().sum()

df

df.info()

df.nunique()

import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


df["Country"].unique()

df["Country"].value_counts()

plt.figure(figsize=(15,6))
sns.countplot(df['Country'], data = df,
 palette = 'hls')
plt.xticks(rotation = 80)
plt.show()

df["Industry"].unique()

df["Industry"].value_counts()

df1 = df["Industry"].value_counts()

df1.to_frame()

df1 = df1.reset_index()

df1

df1 = df1.rename(columns = {'index':'Industry', 'Industry':'Count'})


df1

plt.figure(figsize=(15,6))
sns.barplot(x = df1['Industry'].head(10), y = df1['Count'].head(20), data = df1,
 palette = 'hls')
plt.xticks(rotation = 90)
plt.show()


df.columns

df[['Currency', 'Value']] = df['Valuation ($B)'].str.extract(r'([^\d]*)([\d,\.]+)')

df

df['Date Joined'] = pd.to_datetime(df['Date Joined'])


df['Year'] = df['Date Joined'].dt.year

df["Year"].unique()

df["Year"].value_counts()

plt.figure(figsize=(15,6))
sns.countplot(df['Year'], data = df,
 palette = 'hls')
plt.xticks(rotation = 90)
plt.show()

df.info()

df['Value'] = df['Value'].astype(float)


df.sort_values(by='Value', ascending=False, inplace=True)


plt.figure(figsize=(15,6))
sns.barplot(x = df['Company'].head(50), y = df['Value'].head(50), data = df,
 palette = 'hls')
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(15,6))
sns.lineplot(x = df['Company'].head(50), y = df['Value'].head(50), data = df,
 palette = 'hls')
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(15,6))
sns.scatterplot(x = df['Company'].head(50), y = df['Value'].head(50), data = df,
 palette = 'hls')
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(15,6))
sns.barplot(x = df['Year'], y = df['Value'], data = df,
 palette = 'hls')
plt.xticks(rotation = 90)
plt.show()

df.columns

df["Investors"].nunique()

plt.figure(figsize=(15,6))
sns.lineplot(x = df['Investors'].head(10), y = df['Value'].head(10), data = df,
 palette = 'hls')
plt.xticks(rotation = 90)
plt.show()

