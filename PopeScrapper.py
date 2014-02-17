
# In[263]:

import urllib2
import csv
import re
import pytz
from datetime import datetime
from BeautifulSoup import BeautifulSoup 


# In[289]:

# creat utc time stamp
format = '%Y%m%d%H%M%S'
scrapeDT = datetime.now().utcnow().strftime(format)


# In[290]:

page = urllib2.urlopen('http://www.paddypower.com/bet/novelty-betting/current-affairs/pope-betting').read()


# In[291]:

soup = BeautifulSoup(page)


# In[293]:

table = soup.findAll("table", { "class" : "oddsTable" })


# In[294]:

# makes parsed data list

parsed = []
for tb in table:
    td = tb.findAll("td")
    temp = []
    for t in td:
        if t.getText().__len__() > 0:
            temp.append(t.getText())
    if tb.getText().__len__() > 0:
        parsed.append(temp)
print parsed


# Out[294]:

#     [[u'Cardinal Peter Turkson (Ghana)', u'9/4'], [u"Cardinal Sean O'Malley (United States)", u'50/1'], [u'Cardinal Crescenzio Sepe (Italy)', u'100/1'], [u'Archbishop Angelo Scola (Italy)', u'7/2'], [u'Cardinal Albert Malcolm Ranjith (Sri Lanka)', u'50/1'], [u'Archbishop Diarmuid Martin', u'100/1'], [u'Cardinal Marc Ouellet (Canada)', u'5/1'], [u'Cardinal Joao Braz de Aviz (Brazil)', u'50/1'], [u'Cardinal Ivan Dias (India)', u'100/1'], [u'Cardinal Tarcisio Bertone (Italy)', u'6/1'], [u'Archbishop Vincent Nichols (England)', u'50/1'], [u'Cardinal Jaime Lucas Ortega y Alamino (Cuba)', u'100/1'], [u'Cardinal Leonardo Sandri (Argentina)', u'10/1'], [u'Cardinal Juan Luis Cipriani Thorne (Peru)', u'66/1'], [u'Cardinal Thomas Collins (Canada)', u'100/1'], [u'Cardinal Oscar Rodriguez Maradiaga (Honduras)', u'12/1'], [u'Cardinal Andre Vingt-Trois (France)', u'66/1'], [u'Cardinal Silvano Piovanelli (Italy)', u'125/1'], [u'Cardinal Francis Arinze (Nigeria)', u'14/1'], [u'Cardinal Agnostino Vallini (Italy)', u'66/1'], [u'Cardinal Donald Wuerl (United States)', u'125/1'], [u'Cardinal Peter Erdo (Hungary)', u'14/1'], [u'Cardinal Antonio Canizares Llovera (Spain)', u'66/1'], [u'Cardinal Julian Herranz Casado (Spain)', u'125/1'], [u'Cardinal Christoph Schonborn (Austria)', u'16/1'], [u'Cardinal Raymond Burke (United States)', u'66/1'], [u'Archbishop Nicolas de Jesus Lopez Rodriguez (Dominican Republic)', u'150/1'], [u'Cardinal Angelo Bagnasco (Italy)', u'16/1'], [u'Cardinal Timothy Dolan (United States)', u'66/1'], [u"Cardinal Cormac Murphy-O'Connor (UK)", u'150/1'], [u'Cardinal Gianfranco Ravasi (Italy)', u'16/1'], [u'Cardinal George Pell (Australia)', u'80/1'], [u'Cardinal John Njue (Kenya)', u'150/1'], [u'Cardinal Odilo Scherer (Brazil)', u'16/1'], [u'Cardinal Angelo Amato (Italy)', u'80/1'], [u'Cardinal Giacomo Biffi (Italy)', u'150/1'], [u'Cardinal Luis Antonio Tagle (Philippines)', u'16/1'], [u'Cardinal Attilio Nicora (Italy)', u'80/1'], [u'Cardinal Geraldo Majella Agnelo (Brazil)', u'150/1'], [u'Cardinal Jorge Mario Bergoglio (Argentina)', u'25/1'], [u'Cardinal Antonio Maria Rouco Varela (Spain)', u'80/1'], [u'Cardinal Walter Kasper (Germany)', u'150/1'], [u'Cardinal Robert Sarah (French Guinea)', u'33/1'], [u'Cardinal Wilfrid Napier (South Africa)', u'80/1'], [u'Archbishop Gerhard Ludwig Muller (Germany)', u'150/1'], [u'Cardinal Norberto Rivera Carrera (Mexico)', u'33/1'], [u'Cardinal Philippe Barbarin (France)', u'80/1'], [u'Cardinal Francis George (USA)', u'200/1'], [u'Archbishop Piero Marini (Italy)', u'33/1'], [u'Cardinal Daniel DiNardo (USA)', u'100/1'], [u'Cardinal Angelo Sodano (Italy)', u'200/1'], [u'Cardinal Claudio Hummes (Brazil)', u'40/1'], [u'Cardinal Karl Lehmann (Germany)', u'100/1'], [u'Richard Dawkins (UK)', u'666/1'], [u'Cardinal Mauro Piacenza (Italy)', u'40/1'], [u'Cardinal William Levada (United States)', u'100/1'], [u'Father Dougal Maguire (Craggy Island)', u'1000/1'], [u"Cardinal Keith O'Brien (Scotland)", u'50/1'], [u'Cardinal Jose Da Cruz Policarpo (Portugal)', u'100/1'], [u'Bono (Ireland)', u'1000/1'], [u'Cardinal Dionigi Tettamanzi (Italy)', u'50/1']]

# In[298]:

# set titles for valid Catholic Candidates
titles = ['Cardinal','Archbishop','Father']

# regex structure for extracting the country
regex = re.compile("(.*?)\s*\((.*?)\)")

# make a cleaned up data structure
candidates = []
for i in range(len(parsed)):
    temp = []
    if any(parsed[i][0].split()[0] in t for t in titles):
        m1 = regex.match(parsed[i][0])
        if m1 is not None:
            name = m1.group(1)
            country = m1.group(2)
            temp.append(scrapeDT)
            temp.append(name.split(' ',1)[0])
            temp.append(name.split(' ',1)[1])
            temp.append(country)
            temp.append(parsed[i][1])
            temp.append(float(parsed[i][1].split('/')[1]) / 
                        (float(parsed[i][1].split('/')[1]) + float(parsed[i][1].split('/')[0])))
    if temp:
        candidates.append(temp)


# In[304]:

with open("output.csv", "ab") as f:
    writer = csv.writer(f)
    writer.writerows(candidates)

