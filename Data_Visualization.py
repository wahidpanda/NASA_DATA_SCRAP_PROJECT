
import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from io import StringIO

# Existing code to scrape planetary data
table = [[j.text.replace(u'\xa0', '').replace(',', '').replace('*', '') for j in i.findAll('td')] for i in BeautifulSoup(requests.get('https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html').content, 'lxml').find('table').findAll('tr')]
tablehead = [i.pop(0) for i in table]
dataframe = pd.DataFrame(dict(zip(tablehead, table)))
dataframe.to_csv('planetdata.csv', index=False)

# New feature: Fetch data for confirmed planets in the Kepler field
confirmed_planets_url = 'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=exoplanets&format=ipac&where=pl_kepflag=1'
response = requests.get(confirmed_planets_url)
confirmed_planets_data = pd.read_csv(io.StringIO(response.content.decode('utf-8')), sep='\s+', comment='#')

# Plotting
plt.figure(figsize=(10, 6))

# Plot a simple bar chart to show the count of confirmed planets in the Kepler field
confirmed_planets_count = confirmed_planets_data.shape[0]  # Number of rows gives the count of confirmed planets
plt.bar(['Confirmed Planets in Kepler Field'], [confirmed_planets_count], color='skyblue')

plt.ylabel('Count')
plt.title('Confirmed Planets in Kepler Field')

plt.show()
