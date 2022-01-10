# Bollettino covid giornaliero
## Riepilogo bollettino covid giornaliero per la zona Italia

Esordisco dicendo che non sono un grande esperto di python ma ho deciso di condividere questo semplice programma che eseguito giornalmente restituisce il numero di nuovi positivi, il numero di tamponi totali della giornata e il tasso di positività. L'ho creato perché da molti mesi cercavo giornalmente questi tre dati sul web e così ho deciso di automatizzare e semplificare la consultazione.

I dati di partenza sono quelli ufficiali pubblicati dal repository del [Dipartimento della Protezione civile](https://github.com/pcm-dpc/COVID-19). 
Il file aggiornerà i dati secondo gli orari pubblicati nella pagina sopra menzionata.

Ho iniziato questo percorso con la speranza di poter creare una skill per Alexa che possa leggere l'output delle ultime tre righe del codice: nuovi casi, tamponi, tasso di positività ma non essendo un grande esperto e non avendo trovato una guida nemmeno in lingua inglese che possa aiutarmi step by step nella creazione, spero qualcuno con le competenze giuste voglia darmi qualche suggerimento o qualche guida da seguire.

## Librerie 
<code>- urlopen from urllib.request</code>

<code>- pandas</code>

<code>- datetime and timedelta from datetime</code>

## Utilizzo
Assicuratevi di avere una connessione ad internet affiché il programma possa reperire i dati aggregati italiani e lanciate semplicemente il file da un promt dei comandi (cmd) o aprendolo tramite python.
  
## Come funziona il codice
Il codice apre il file *json* con l'andamento nazionale giornaliero del covid19 in Italia e lo salva come dizionario. Prende la stringa dal *timestamp* del *repository* e la porta nel formato *aaaammgg* e tramite **datetime** lo trasforma in data sottraendo un giorno (**timedelta**) per ricomporre in seguito il link all'url della pagina con i dati del giorno precedente. I dati del giorno precedente sono in formato *csv* e quindi tramite **pandas** vengono aperti ed estratto il numero di tamponi totali del giorno precedente. Tale numero servirà a calcolare il numero di tamponi giornalieri per differenza con il numero di tamponi del giorno precedente. Infine tramite semplici formule viene calcolato il tasso di positività e trasformato in percentuale. Le ultime tre righe printano questi valori di riepilogo.
<p align="center"><sub><sup>OUTPUT EXAMPLE</sup></sub>
<p align="center"><img src="https://i.ibb.co/nMq5PPX/cmd.png&s=50" width="500" height="500"></p></center>

## Aggiornamenti
- Aggiunto il calcolo del numero dei decessi giornalieri *01/01/2022*
- Disponibile modalità embedded (tramite *Trinket*) per il vostro sito web incollando il seguente codice HTML sul vostro sito:
```
<<iframe src="https://trinket.io/embed/python3/45015a74e4?outputOnly=true&runOption=run&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
```
- Link diretto alla consultazione [bollettino covid giornaliero](https://pcwizard-italia.blogspot.com/2022/01/riepilogo-bollettino-covid-giornaliero.html)
- Aggiunto nuovo programma "bollettinoo_covid-regioni.py" che permette di consultare i dati di riepilogo a livello regionale e nazionale
<hr>
*Autore: [@Pymai73](https://github.com/Pymai73)*
