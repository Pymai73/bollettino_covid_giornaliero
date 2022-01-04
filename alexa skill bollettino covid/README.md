Skill Alexa bollettino covid
## Skill Alexa con riepilogo bollettino covid giornaliero per la zona Italia

Dopo la creazione dello script python ho deciso di cimentarmi nella creazione di una skill per Alexa che mi leggesse il piccolo report giornaliero con tutti i numeri del covid in Italia. La skill restituisce il numero di nuovi positivi, il numero di tamponi totali della giornata, il tasso di positività, i nuovi ingressi in terapia intensiva e il numero decessi. Non avendo trovato alcuna skill che proponeva questi dati ho deciso di provare per la prima volta a scrivere la skill.

Come per il file python anche i dati da cui oarte la skill sono sono quelli ufficiali pubblicati dal repository del [Dipartimento della Protezione civile](https://github.com/pcm-dpc/COVID-19). 
La skill aggiornerà i dati secondo gli orari pubblicati nella pagina sopra menzionata.

Per la creazione della skill ho utilizzato alcuni tutorial youtube e dove non ho trovato nulla ho semplicemente ragionato fino a trovare una soluzione funzionante. Pubblicherò qui il codice sorgente della skill e vorrei realizzare una guida che ripropone i principali step della creazione della skill. Essendo una prima versione potrebbe non funzionare sempre a dovere e accetto consigli in caso di scoperta di bug.

## Librerie 
<code>- urlopen from urllib.request</code>

<code>- pandas</code>

<code>- datetime and timedelta from datetime</code>
