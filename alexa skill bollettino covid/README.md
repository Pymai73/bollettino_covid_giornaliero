Skill Alexa bollettino covid
## Skill Alexa con riepilogo bollettino covid giornaliero per la zona Italia

Dopo la creazione dello script python ho deciso di cimentarmi nella creazione di una skill per Alexa che mi leggesse il piccolo report giornaliero con tutti i numeri del covid in Italia. La skill restituisce:
- il numero di nuovi positivi, 
- il numero di tamponi totali della giornata, 
- il tasso di positività, 
- i nuovi ingressi in terapia intensiva e 
- il numero decessi. 

Come per il file python anche i dati da cui parte la skill sono sono quelli ufficiali pubblicati dal repository del [Dipartimento della Protezione civile](https://github.com/pcm-dpc/COVID-19). 
La skill aggiornerà i dati secondo gli orari pubblicati nella pagina sopra menzionata.

Per la creazione della skill ho utilizzato un [tutorial youtube](https://www.youtube.com/watch?v=G1cDLqhhBsU) e dove non ho trovato nulla ho semplicemente ragionato fino a trovare una soluzione funzionante. Pubblicherò qui il codice sorgente della skill e sul mio blog una guida che ripropone i principali step della creazione della skill. Essendo una prima versione potrebbe non funzionare sempre a dovere e accetto consigli in caso di scoperta di bug.

Non avendo trovato alcuna skill che proponeva questi dati ho deciso di provare per la prima volta a scriverne una. Ho sottoposto a verifica la skill per renderla pubblica e disponibile a tutti ma non ha superato la certificazione perché, cito la loro mail: **Amazon sta limitando le skill sul COVID-19 per assicurarare e "garantire l'accuratezza e la coerenza delle informazioni" che tradotto in parole semplici significa che non hanno nemmeno guardato che i pochi dati di riepilogo provengono dal repository ufficiale del Dipartimento di Protezione Civile e che vengono eseguite pochissime operazioni matematiche solo per calcolare il tasso di positività, il numero di tamponi e i decessi mentre il resto viene semplicemente letto dal repository menzionato**. Quindi fin quando non cambieranno la loro policy chiunque voglia usare la skill deve importarla su sito di Amazon developers.

## Librerie 

<code>- pandas da inserire nel file requirement.txt</code>

<code>- tutte le restanti sono incluse di base nel file lambda_fuctions</code>

## Attivazione della skill (Invocation) 

Per attivare la skill basta dire:

*Alexa, bollettino covid*

oppure 

*Alexa, apri bollettino covid*

oppure

*Alexa, chiedi a bollettino covid il numero di tamponi (il tasso di positività, i decessi, etc.)*

## Tutorial per la creazione della skill
*Italiano:*
Qui trovate i principali step che ho seguito per creare la skill [PC Wizard - Skill Alexa Bollettino Covid](https://pcwizard-italia.blogspot.com/2022/01/skill-alexa-per-avere-il-riepilogo-del.html)

*English:*
Here you will find the main step that I follow to create this skill [PC Wizard - Alexa Skill with the daily covid report for Italy](https://pcwizard-italia.blogspot.com/2022/01/after-creation-of-python-script-i.html)
