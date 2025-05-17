# Finkrea S.r.l. - Processo BPMN

Questo repository contiene la documentazione e i diagrammi BPMN (Business Process Model and Notation) per il processo operativo di Finkrea S.r.l., società di mediazione creditizia operante in Italia.

## Struttura del Repository

- **`/diagrams`**: Contiene tutti i diagrammi BPMN in formato PNG
- **`/docs`**: Contiene la documentazione dettagliata del processo e l'analisi degli attori
- **`/src`**: Contiene il codice sorgente per la generazione dei diagrammi BPMN
- **`/website`**: Contiene il sito web statico per la visualizzazione interattiva dei diagrammi e della documentazione

## Panoramica del Processo

Il processo operativo di Finkrea S.r.l. è stato modellato secondo il linguaggio BPMN e si articola in sei macro-processi principali:

1. **Acquisizione Lead**: Identificazione e acquisizione di potenziali clienti
2. **Analisi Preliminare**: Valutazione della fattibilità della richiesta
3. **Istruttoria Pratica**: Raccolta e verifica della documentazione
4. **Delibera**: Ottenimento dell'approvazione dall'istituto di credito
5. **Erogazione**: Finalizzazione del finanziamento
6. **Gestione Post-Erogazione**: Gestione del rapporto post-vendita

## Documentazione

La documentazione completa del processo è disponibile nella cartella `/docs`:

- [`documentazione_processo.md`](docs/documentazione_processo.md): Descrizione dettagliata di tutti i macro-processi e sotto-processi
- [`attori_e_attivita.md`](docs/attori_e_attivita.md): Analisi degli attori coinvolti e delle loro responsabilità

## Diagrammi BPMN

I diagrammi BPMN sono disponibili nella cartella `/diagrams`:

- [`processo_completo.png`](diagrams/processo_completo.png): Visione d'insieme dell'intero processo
- [`acquisizione_lead.png`](diagrams/acquisizione_lead.png): Diagramma del processo di acquisizione lead
- [`analisi_preliminare.png`](diagrams/analisi_preliminare.png): Diagramma del processo di analisi preliminare
- [`istruttoria_pratica.png`](diagrams/istruttoria_pratica.png): Diagramma del processo di istruttoria pratica
- [`delibera.png`](diagrams/delibera.png): Diagramma del processo di delibera
- [`erogazione.png`](diagrams/erogazione.png): Diagramma del processo di erogazione
- [`post_erogazione.png`](diagrams/post_erogazione.png): Diagramma del processo di gestione post-erogazione

## Sito Web

Il sito web statico per la visualizzazione interattiva dei diagrammi e della documentazione è disponibile nella cartella `/website`. È possibile visualizzare il sito aprendo il file `index.html` in un browser web.

## Generazione dei Diagrammi

Il codice sorgente per la generazione dei diagrammi BPMN è disponibile nella cartella `/src`:

- [`bpmn_generator.py`](src/bpmn_generator.py): Script Python per la generazione dei diagrammi BPMN

### Requisiti per la Generazione

Per eseguire lo script di generazione dei diagrammi, sono necessari i seguenti requisiti:

```
matplotlib
networkx
pydotplus
```

### Esecuzione

Per generare i diagrammi BPMN, eseguire il seguente comando:

```bash
python src/bpmn_generator.py
```

## Licenza

Questo progetto è di proprietà di Finkrea S.r.l. e non può essere utilizzato senza autorizzazione.
