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
# dictionary_items = bollettino_covid.items()
# for item in dictionary_items:
#   print(item)

newurl=bollettino_covid['data'][:-9].replace('-','')  #sostituisco il trattino del formato data per avere 20211229
datetime_object = datetime.strptime(newurl, '%Y%m%d').date() #trasformo la stringa newurl in data
newurl = datetime_object - timedelta(days=1) #sottraggo un giorno alla data definita in newurl
newurl=str(newurl)[:10].replace('-','') #tolgo il trattino divisore del formato aaaa-mm-gg

url2 = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-'
url2=url2+newurl+'.csv' #unisco la parte dell'url alla data del giorno precedente per avere il nuovo url
data = pd.read_csv(url2)  #leggo il csv dal url del giorno precedente
tamponi_prec=(int(data['tamponi']))  #prendo il numero di tamponi del giorno precedente
positivita=bollettino_covid['nuovi_positivi']/(bollettino_covid['tamponi']-tamponi_prec) #calcolo il tasso di positività nuovi/(differenza oggi e ieri dei tamponi)
positivita_percentage = "{:.2%}".format(positivita)     #trasformo il decimale in percentuale prima di stampare il risultato
deceduti_prec=(int(data['deceduti']))  #prendo il numero di decessi del giorno precedente

#dati regionali
url3='https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-latest.csv'
data2 = pd.read_csv(url3)
#regioni = str(data2['denominazione_regione'])
df= pd.DataFrame(data2)
#print(df.iloc[10]) #printa i dati del Molise che ha ID 10

scelta_regione = input("Per consultare i dati regionali del bollettino covid inserisci il nome della regione:\n")
scelta_regione = scelta_regione.capitalize() #trasforma la prima lettera in maiuscola per far funzionare la ricerca nel csv

list_region=df['denominazione_regione'].values.tolist() #original list
# initializing substring scelta_regione
res = [i for i in list_region if scelta_regione in i] # using list comprehension to get string with substring 

try:   #ho messo try and except per catturare l'errore di digitazione o regione non trovata
    scelta_regione=res[0] #trasforma res da lista a stringa

    regione = df.loc[df['denominazione_regione']==scelta_regione] # regione = df.loc[df['denominazione_regione'].str.contains("Molise", case = False)] #modo alternativo di scrivere la formula
    print(df.iloc[regione['denominazione_regione'].head().index.values[0]]) #modifica del print(df.iloc[10]) del commento sopra con il nome regione selezionato dall'utente
    # nuovi_positivi_regione = regione['nuovi_positivi'].values[0] #You can turn your 1x1 dataframe into a numpy array, then access the first and only value of that array
    url4=url3[:-10]+newurl+'.csv'
    data3 = pd.read_csv(url4)  #riscrivo data2 con il nuovo url modficicato
    df2= pd.DataFrame(data3)   #nuovo dataframe con dati url del giorno precedente per tutte le regioni
    regione_prec = df2.loc[df2['denominazione_regione']==scelta_regione]  #dataframe con i dati della regione richiesta del giorno precedente
    tamponi_regione=(regione_prec['tamponi']).values[0]             # tamponi giorno precedente regione richiesta
    positivita_reg=regione['nuovi_positivi'].values[0]/(regione['tamponi'].values[0]-tamponi_regione) #calcolo il tasso di positività nuovi/(differenza oggi e ieri dei tamponi)
    positivita_reg_percentage = "{:.2%}".format(positivita_reg)     #trasformo il decimale in percentuale prima di stampare il risultato
    
    
    print('\nI nuovi positivi in', regione['denominazione_regione'].values[0], 'per il giorno', regione['data'].values[0][:-9], 'sono', regione['nuovi_positivi'].values[0])
    # modo alternativo: print('\nI nuovi positivi in Molise per il giorno', bollettino_covid['data'][:-9], 'sono', df.iloc[10]['nuovi_positivi'])
    print('Il numero di tamponi è pari a', regione['tamponi'].values[0]-tamponi_regione)
    print('Il tasso di positività è pari a', positivita_reg_percentage)
    print('Il numero di ingressi dalla terapia intensiva è', regione['terapia_intensiva'].values[0]-regione_prec['terapia_intensiva'].values[0])
    print('Il numero di decessi è', regione['deceduti'].values[0]-regione_prec['deceduti'].values[0])
    
except IndexError:
    print('Nome della regione errato')

nazionale=input("\nVuoi consultare il bollettino covid nazionale Si/No: ")
if nazionale == 'si' or nazionale == 'yes' or nazionale == 's' or nazionale == 'y':
    print('\nI nuovi positivi in Italia per il giorno', bollettino_covid['data'][:-9], 'sono', bollettino_covid['nuovi_positivi'])
    print('Il numero di tamponi è pari a', bollettino_covid['tamponi']-tamponi_prec)
    print('Il tasso di positività è pari a', positivita_percentage)
    print('Il numero di ingressi dalla terapia intensiva è', bollettino_covid['terapia_intensiva']-data['terapia_intensiva'].values[0])
    print('Il numero di decessi è', bollettino_covid['deceduti']-deceduti_prec)
    print('\nseguite il progetto su https://github.com/Pymai73/bollettino_covid_giornaliero')
elif nazionale == 'no' or nazionale == 'n':
    print('\nArrivederci. Continua a seguire il progetto su Github: https://github.com/Pymai73/bollettino_covid_giornaliero')
else:
    print('\nScelta non corretta. Continua a seguire il progetto su Github: https://github.com/Pymai73/bollettino_covid_giornaliero')
