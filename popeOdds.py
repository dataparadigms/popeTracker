# file: popeOdds.py
# date: 2013.02.24
# author:  AJ
# 
# generates simple plot of the possible candidates for next Pope based off 
# of betting lines.

import csv
import datetime
import urllib
import pandas as pd

# read in .csv
url = "https://raw.github.com/dataparadigms/popeTracker/master/odds.csv"
webpage = urllib.urlopen(url)

# convert to pandas data frame
odds = pd.read_csv(webpage, 
  header = None, 
  names=['date','position','name', 'country', 'odds','probability'])

# convert the datetime to an actual date time
odds['date'] = odds['date'].map(
  lambda x: datetime.datetime.strptime(str(x), '%Y%m%d%H%M%S'))

# drop dups
odds = odds.drop_duplicates(cols=['date','name'], take_last=True)

# pivot to get one column per name
data = odds.pivot(index = 'date',
        columns = 'name',
        values = 'probability')

# keep those with a > .1 chance of winning
leaders = data[data > .1]
leaders = leaders.dropna(axis=1, how='all')

# make the plot
leaders.plot(title='Probability of Being the Next Pope', 
  grid=True,
  figsize=(10,10));

