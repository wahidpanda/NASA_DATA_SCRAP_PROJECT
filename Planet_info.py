import requests, pandas as pd
from bs4 import BeautifulSoup
table = [[j.text.replace(u'\xa0', '').replace(',', '').replace('*', '')
for j in i.findAll('td')] for i in BeautifulSoup(requests.get('https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html').content, 'lxml').find('table').findAll('tr')]
tablehead = [i.pop(0) for i in table]
dataframe = pd.DataFrame(dict(zip(tablehead, table)))
dataframe.to_csv('solarinfoofplanet.csv', index=False)
