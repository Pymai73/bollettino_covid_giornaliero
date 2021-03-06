# import urllib library
from urllib.request import urlopen
import pandas as pd
from datetime import datetime, timedelta
  
# import json
import json
# store the URL in url as 
# parameter for urlopen
url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale-latest.json"
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())
bollettino_covid=data_json[0]

# print the json response
dictionary_items = bollettino_covid.items()
for item in dictionary_items:
    print(item)

newurl=bollettino_covid['data'][:-9].replace('-','')  #sostituisco il trattino del formato data per avere 20211229
datetime_object = datetime.strptime(newurl, '%Y%m%d') #trasformo la stringa newurl in data
newurl = datetime_object - timedelta(days=1) #sottraggo un giorno alla data definita in newurl
newurl=str(newurl)[:10].replace('-','') #tolgo il trattino divisore del formato aaaa-mm-gg

url2 = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-'
url2=url2+newurl+'.csv' #unisco la parte dell'url alla data del giorno precedente per avere il nuovo url
data = pd.read_csv(url2)  #leggo il csv dal url del giorno precedente
tamponi_prec=(int(data['tamponi']))  #prendo il numero di tamponi del giorno precedente
positivita=bollettino_covid['nuovi_positivi']/(bollettino_covid['tamponi']-tamponi_prec) #calcolo il tasso di positivit√† nuovi/(differenza oggi e ieri dei tamponi)
positivita_percentage = "{:.2%}".format(positivita)     #trasformo il decimale in percentuale prima di stampare il risultato
deceduti_prec=(int(data['deceduti']))  #prendo il numero di decessi del giorno precedente

print('\nI nuovi positivi in Italia per il giorno', bollettino_covid['data'][:-9], 'sono', bollettino_covid['nuovi_positivi'])
print('Il numero di tamponi √® pari a', bollettino_covid['tamponi']-tamponi_prec)
print('Il tasso di positivit√† √® pari a', positivita_percentage)
if bollettino_covid['terapia_intensiva']-data['terapia_intensiva'].values[0] >= 0:
   print('Il numero di ingressi in terapia intensiva √®', bollettino_covid['terapia_intensiva']-data['terapia_intensiva'].values[0])
else:
   print('Il numero di uscite dalla terapia intensiva √®', bollettino_covid['terapia_intensiva']-data['terapia_intensiva'].values[0])
if bollettino_covid['totale_ospedalizzati']-data['totale_ospedalizzati'].values[0] >= 0:
   print('Il numero di nuovi ospedalizzati √® pari a', bollettino_covid['totale_ospedalizzati']-data['totale_ospedalizzati'].values[0])
else:
   print('Il numero di ospedalizzati √® diminuito di', bollettino_covid['totale_ospedalizzati']-data['totale_ospedalizzati'].values[0])
print('Il numero di decessi √®', bollettino_covid['deceduti']-deceduti_prec)
print('\nseguite il progetto su https://github.com/Pymai73/bollettino_covid_giornaliero')
