# Bollettino covid giornaliero
## Riepilogo bollettino covid giornaliero per la zona Italia

Esordisco dicendo che non sono un grande esperto di python ma ho deciso di condividere questo semplice programma che eseguito giornalmente restituisce il numero di nuovi positivi, il numero di tamponi totali della giornata e il tasso di positività. L'ho creato perché da molti mesi cercavo giornalmente questi tre dati sul web e così ho deciso di automatizzare e semplificare la consultazione.

I dati di partenza sono quelli ufficiali pubblicati dal repository https://github.com/pcm-dpc/COVID-19
Il file aggiornerà i dati secondo gli orari pubblicati sulla pagina sopra menzionata.

Ho iniziato questo percorso con la speranza di poter creare una skill per Alexa che possa leggere l'output delle ultime tre righe del codice: nuovi casi, tamponi, tasso di positività ma non essendo un grande esperto e non avendo trovato una guida nemmeno in lingua inglese che possa aiutarmi step by step nella creazione spero qualcuno con le competenze giuste voglia darmi qualche suggerimento o qualche guida da seguire.

## Librerie richieste
> urlopen from urllib.request
> pandas
> datetime and timedelta from datetime
