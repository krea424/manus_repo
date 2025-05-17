# Documentazione Processo Operativo Finkrea S.r.l.

## Introduzione

Il presente documento descrive il processo operativo completo di Finkrea S.r.l., società di mediazione creditizia operante in Italia. Il processo è stato progettato secondo le best practice del settore, in conformità con la normativa vigente e con l'obiettivo di ottimizzare le attività operative dell'azienda.

La documentazione è strutturata in modo da fornire una visione completa del processo, partendo dai macro-processi fino ad arrivare ai dettagli operativi di ciascun sotto-processo, con particolare attenzione alle responsabilità, agli strumenti utilizzati, alla documentazione necessaria e agli aspetti normativi.

## Indice

1. [Panoramica del Processo](#panoramica-del-processo)
2. [Attori e Responsabilità](#attori-e-responsabilità)
3. [Macro-Processi](#macro-processi)
   - [Acquisizione Lead](#acquisizione-lead)
   - [Analisi Preliminare](#analisi-preliminare)
   - [Istruttoria Pratica](#istruttoria-pratica)
   - [Delibera](#delibera)
   - [Erogazione](#erogazione)
   - [Gestione Post-Erogazione](#gestione-post-erogazione)
4. [Strumenti e Software](#strumenti-e-software)
5. [Documentazione e Modulistica](#documentazione-e-modulistica)
6. [Aspetti Normativi](#aspetti-normativi)
7. [Governance e Miglioramento Continuo](#governance-e-miglioramento-continuo)
8. [Glossario](#glossario)

## Panoramica del Processo

Il processo operativo di Finkrea S.r.l. è stato modellato secondo il linguaggio BPMN (Business Process Model and Notation), che permette di rappresentare graficamente i flussi di lavoro, le responsabilità e le interazioni tra i diversi attori coinvolti.

Il processo completo si articola in sei macro-processi principali, che coprono l'intero ciclo di vita della relazione con il cliente, dall'acquisizione del lead fino alla gestione post-erogazione. Ogni macro-processo è ulteriormente suddiviso in sotto-processi, con attività specifiche, ruoli definiti e controlli dedicati.

![Processo BPMN Completo](/home/ubuntu/finkrea_bpmn/diagrammi/processo_completo.png)

## Attori e Responsabilità

Il processo coinvolge diversi attori, ciascuno con responsabilità specifiche. La tabella seguente riassume i principali ruoli e le loro responsabilità generali:

| Attore | Descrizione e Responsabilità Generali |
|--------|---------------------------------------|
| **Back Office** | Gestione documentale, supporto operativo, verifica conformità documentale, comunicazioni con banche partner |
| **Collaboratore Commerciale** | Acquisizione lead, primo contatto con clienti, raccolta documentazione, presentazione offerte |
| **Responsabile Delibera** | Valutazione merito creditizio, approvazione pratiche, gestione rapporti con istituti di credito |
| **Ufficio Legale** | Verifica conformità normativa, gestione contrattualistica, supporto per questioni legali |
| **Amministrazione** | Gestione fatturazione, controllo pagamenti, reportistica finanziaria |
| **Cliente** | Richiesta servizi, fornitura documentazione, accettazione offerte |
| **Banche/Istituti di Credito** | Valutazione richieste, erogazione finanziamenti, comunicazione esiti |

La matrice RACI (Responsible, Accountable, Consulted, Informed) definisce in dettaglio le responsabilità specifiche per ciascuna attività del processo:

| Attività | Back Office | Collaboratore Commerciale | Responsabile Delibera | Ufficio Legale | Amministrazione | Cliente | Banche |
|----------|-------------|---------------------------|------------------------|----------------|-----------------|---------|--------|
| Acquisizione Lead | I | R/A | I | - | - | C | - |
| Analisi Preliminare | C | R | A | C | - | I | - |
| Raccolta Documentazione | C | R | I | - | - | A | - |
| Verifica Documentazione | R | I | A | C | - | I | - |
| Istruttoria Pratica | R | C | A | C | - | I | - |
| Invio Pratica a Banche | R | I | A | - | - | I | C |
| Delibera | I | I | C | - | - | I | R/A |
| Comunicazione Esito | C | R | A | - | - | I | I |
| Erogazione | C | I | A | C | R | I | R |
| Gestione Post-Erogazione | R | C | A | C | R | I | C |
| Fatturazione | C | I | I | - | R/A | I | - |

*Legenda: R = Responsible, A = Accountable, C = Consulted, I = Informed*

## Macro-Processi

### Acquisizione Lead

**Obiettivo**: Identificare e acquisire potenziali clienti interessati ai servizi di mediazione creditizia.

**Input**: Campagne marketing, referral, contatti diretti, richieste web.

**Output**: Lead qualificato e primo appuntamento fissato.

**KPI**: 
- Numero di lead generati/mese
- Tasso di conversione lead-appuntamento
- Costo per lead acquisito

![Processo BPMN Acquisizione Lead](/home/ubuntu/finkrea_bpmn/diagrammi/acquisizione_lead.png)

#### Sotto-processi:

1. **Generazione Lead**
   
   Questa fase iniziale prevede tutte le attività di marketing e comunicazione finalizzate all'acquisizione di potenziali clienti. Il Collaboratore Commerciale è responsabile della gestione delle campagne marketing, della presenza online e delle attività di networking.
   
   *Attività*: Gestione campagne marketing, presenza online, networking
   
   *Ruoli*: Collaboratore Commerciale (R/A)
   
   *Strumenti*: CRM, piattaforme marketing, sito web
   
   *Documentazione*: Schede contatto, form web
   
   *Controlli*: Verifica qualità lead, conformità GDPR
   
   *Tempistiche*: Continuo

2. **Qualificazione Lead**
   
   Una volta acquisito un contatto, è necessario verificarne l'interesse e i requisiti base per procedere. Il Collaboratore Commerciale effettua un primo contatto telefonico per raccogliere informazioni preliminari e valutare l'effettivo interesse del potenziale cliente.
   
   *Attività*: Primo contatto telefonico, verifica interesse e requisiti base
   
   *Ruoli*: Collaboratore Commerciale (R/A)
   
   *Strumenti*: CRM, telefono
   
   *Documentazione*: Scheda cliente preliminare
   
   *Controlli*: Verifica requisiti minimi per procedere
   
   *Tempistiche*: Entro 1 giorno lavorativo dalla generazione lead

3. **Primo Appuntamento**
   
   Se il lead risulta qualificato, si procede con la pianificazione del primo incontro. Il Collaboratore Commerciale organizza l'appuntamento e prepara il materiale informativo necessario.
   
   *Attività*: Fissare e preparare il primo incontro con il cliente
   
   *Ruoli*: Collaboratore Commerciale (R/A), Cliente (I)
   
   *Strumenti*: CRM, calendario, email
   
   *Documentazione*: Agenda appuntamenti, materiale informativo
   
   *Controlli*: Conferma appuntamento
   
   *Tempistiche*: Entro 3 giorni lavorativi dalla qualificazione

### Analisi Preliminare

**Obiettivo**: Valutare la fattibilità della richiesta e raccogliere informazioni dettagliate.

**Input**: Lead qualificato, informazioni preliminari cliente.

**Output**: Profilo cliente completo, identificazione prodotti adeguati.

**KPI**: 
- Tempo medio di analisi preliminare
- Percentuale di pratiche che superano l'analisi preliminare

![Processo BPMN Analisi Preliminare](/home/ubuntu/finkrea_bpmn/diagrammi/analisi_preliminare.png)

#### Sotto-processi:

1. **Colloquio Conoscitivo**
   
   Durante il primo incontro con il cliente, il Collaboratore Commerciale raccoglie informazioni dettagliate sulla situazione finanziaria e sulle esigenze specifiche del cliente. Questo colloquio è fondamentale per comprendere le necessità del cliente e indirizzarlo verso le soluzioni più adeguate.
   
   *Attività*: Incontro con cliente, raccolta esigenze e situazione finanziaria
   
   *Ruoli*: Collaboratore Commerciale (R), Responsabile Delibera (A), Cliente (C)
   
   *Strumenti*: CRM, checklist colloquio
   
   *Documentazione*: Scheda cliente, questionario esigenze
   
   *Controlli*: Verifica coerenza informazioni
   
   *Tempistiche*: Durata media 1 ora

2. **Pre-valutazione Fattibilità**
   
   Sulla base delle informazioni raccolte, si effettua una prima analisi della fattibilità della richiesta. Il Collaboratore Commerciale, con il supporto del Back Office e sotto la supervisione del Responsabile Delibera, valuta la situazione del cliente e le possibili soluzioni finanziarie.
   
   *Attività*: Analisi preliminare situazione cliente e possibili soluzioni
   
   *Ruoli*: Collaboratore Commerciale (R), Responsabile Delibera (A), Back Office (C)
   
   *Strumenti*: Software analisi creditizia, simulatori
   
   *Documentazione*: Report pre-valutazione
   
   *Controlli*: Verifica parametri base di finanziabilità
   
   *Tempistiche*: Entro 2 giorni lavorativi dal colloquio

3. **Presentazione Soluzioni**
   
   Se la pre-valutazione ha esito positivo, il Collaboratore Commerciale presenta al cliente le possibili soluzioni finanziarie, illustrando caratteristiche, condizioni e vantaggi di ciascuna opzione.
   
   *Attività*: Illustrazione al cliente delle possibili soluzioni finanziarie
   
   *Ruoli*: Collaboratore Commerciale (R/A), Cliente (I)
   
   *Strumenti*: Presentazioni, simulatori
   
   *Documentazione*: Proposte preliminari, simulazioni
   
   *Controlli*: Verifica adeguatezza proposte (MIFID)
   
   *Tempistiche*: Entro 3 giorni lavorativi dalla pre-valutazione

### Istruttoria Pratica

**Obiettivo**: Raccogliere e verificare la documentazione necessaria per la valutazione del merito creditizio.

**Input**: Profilo cliente, documentazione preliminare, prodotto scelto.

**Output**: Fascicolo completo e verificato, pronto per la delibera.

**KPI**: 
- Tempo medio di istruttoria
- Percentuale di pratiche con documentazione incompleta
- Tasso di rifiuto per documentazione inadeguata

![Processo BPMN Istruttoria Pratica](/home/ubuntu/finkrea_bpmn/diagrammi/istruttoria_pratica.png)

#### Sotto-processi:

1. **Raccolta Documentazione**
   
   In questa fase si procede alla raccolta di tutta la documentazione necessaria per l'istruttoria della pratica. Il Collaboratore Commerciale richiede al cliente i documenti richiesti in base alla tipologia di finanziamento.
   
   *Attività*: Richiesta e raccolta documenti necessari
   
   *Ruoli*: Collaboratore Commerciale (R), Cliente (I), Back Office (C)
   
   *Strumenti*: CRM, email, checklist documenti
   
   *Documentazione*: Documenti identità, reddituali, patrimoniali, etc.
   
   *Controlli*: Verifica completezza documentale
   
   *Tempistiche*: Entro 5 giorni lavorativi

2. **Verifica Documentale**
   
   Una volta ricevuta la documentazione, il Back Office effettua un controllo accurato per verificarne la completezza, la validità e la conformità normativa. L'Ufficio Legale può essere consultato per aspetti specifici relativi alla conformità.
   
   *Attività*: Controllo accuratezza e validità documenti
   
   *Ruoli*: Back Office (R), Responsabile Delibera (A), Ufficio Legale (C)
   
   *Strumenti*: Software gestione documentale, checklist verifica
   
   *Documentazione*: Report verifica, note integrative
   
   *Controlli*: Antiriciclaggio, conformità normativa
   
   *Tempistiche*: Entro 2 giorni lavorativi dalla ricezione completa

3. **Preparazione Fascicolo**
   
   Completata la verifica documentale, il Back Office organizza tutti i documenti in un fascicolo completo, pronto per essere inviato all'istituto di credito. Il Responsabile Delibera supervisiona questa fase per garantire la qualità del fascicolo.
   
   *Attività*: Organizzazione documenti e preparazione pratica per invio
   
   *Ruoli*: Back Office (R), Responsabile Delibera (A)
   
   *Strumenti*: Software gestione documentale
   
   *Documentazione*: Fascicolo completo, checklist invio
   
   *Controlli*: Verifica finale completezza
   
   *Tempistiche*: Entro 1 giorno lavorativo dalla verifica

### Delibera

**Obiettivo**: Ottenere l'approvazione del finanziamento dall'istituto di credito.

**Input**: Fascicolo completo e verificato.

**Output**: Esito delibera (approvazione, rifiuto, richiesta integrazioni).

**KPI**: 
- Tempo medio di delibera
- Tasso di approvazione
- Percentuale di richieste di integrazione

![Processo BPMN Delibera](/home/ubuntu/finkrea_bpmn/diagrammi/delibera.png)

#### Sotto-processi:

1. **Invio Pratica**
   
   Il fascicolo completo viene trasmesso all'istituto di credito attraverso i canali ufficiali (portali dedicati, PEC, email certificata). Il Back Office si occupa dell'invio, sotto la supervisione del Responsabile Delibera.
   
   *Attività*: Trasmissione fascicolo all'istituto di credito
   
   *Ruoli*: Back Office (R), Responsabile Delibera (A)
   
   *Strumenti*: Portali banche, PEC, email certificata
   
   *Documentazione*: Ricevuta invio, tracking number
   
   *Controlli*: Verifica corretta ricezione
   
   *Tempistiche*: Entro 1 giorno lavorativo dalla preparazione

2. **Monitoraggio Stato Pratica**
   
   Durante la fase di valutazione da parte dell'istituto di credito, il Back Office monitora regolarmente lo stato di avanzamento della pratica, verificando eventuali richieste di integrazioni o chiarimenti.
   
   *Attività*: Verifica avanzamento presso istituto di credito
   
   *Ruoli*: Back Office (R), Responsabile Delibera (A)
   
   *Strumenti*: Portali banche, CRM, telefono
   
   *Documentazione*: Log stato pratica
   
   *Controlli*: Verifica tempistiche previste
   
   *Tempistiche*: Verifica ogni 3 giorni lavorativi

3. **Gestione Esito**
   
   Alla ricezione dell'esito della delibera, il Responsabile Delibera analizza la risposta dell'istituto di credito e coordina le azioni successive. In caso di esito positivo, si procede con la fase di erogazione; in caso di richiesta di integrazioni, si attiva il processo di raccolta documenti aggiuntivi; in caso di rifiuto, si valutano alternative o si comunica l'esito negativo al cliente.
   
   *Attività*: Ricezione e gestione risposta istituto di credito
   
   *Ruoli*: Responsabile Delibera (A), Back Office (R), Collaboratore Commerciale (I)
   
   *Strumenti*: CRM, email, telefono
   
   *Documentazione*: Comunicazione esito, eventuali richieste integrazione
   
   *Controlli*: Verifica condizioni delibera
   
   *Tempistiche*: Entro 1 giorno lavorativo dalla ricezione esito

### Erogazione

**Obiettivo**: Finalizzare il processo di finanziamento e garantire l'erogazione al cliente.

**Input**: Delibera positiva, documentazione approvata.

**Output**: Finanziamento erogato, documentazione contrattuale completa.

**KPI**: 
- Tempo medio tra delibera ed erogazione
- Percentuale di pratiche erogate sul totale deliberate

![Processo BPMN Erogazione](/home/ubuntu/finkrea_bpmn/diagrammi/erogazione.png)

#### Sotto-processi:

1. **Preparazione Contrattualistica**
   
   Dopo l'approvazione della pratica, il Back Office predispone la documentazione contrattuale finale, che viene verificata dall'Ufficio Legale per garantirne la conformità normativa.
   
   *Attività*: Predisposizione documenti contrattuali finali
   
   *Ruoli*: Back Office (R), Ufficio Legale (C), Responsabile Delibera (A)
   
   *Strumenti*: Software gestione documentale, modelli contrattuali
   
   *Documentazione*: Contratti, modulistica finale
   
   *Controlli*: Verifica conformità normativa
   
   *Tempistiche*: Entro 2 giorni lavorativi dalla delibera

2. **Firma Contratti**
   
   Il Collaboratore Commerciale organizza un incontro con il cliente per la firma di tutti i documenti contrattuali. Durante l'incontro, vengono illustrate al cliente tutte le condizioni contrattuali e raccolte le firme necessarie.
   
   *Attività*: Organizzazione incontro per firma documenti
   
   *Ruoli*: Collaboratore Commerciale (R), Cliente (I), Back Office (C)
   
   *Strumenti*: Agenda, CRM
   
   *Documentazione*: Contratti firmati, ricevute
   
   *Controlli*: Verifica completezza firme e documenti
   
   *Tempistiche*: Entro 5 giorni lavorativi dalla preparazione

3. **Conferma Erogazione**
   
   Dopo la firma dei contratti e l'invio della documentazione all'istituto di credito, il Back Office verifica l'avvenuta erogazione del finanziamento e comunica al cliente l'esito positivo.
   
   *Attività*: Verifica avvenuta erogazione e comunicazione al cliente
   
   *Ruoli*: Back Office (R), Amministrazione (C), Responsabile Delibera (A)
   
   *Strumenti*: Portali banche, CRM, email
   
   *Documentazione*: Conferma erogazione, piano ammortamento definitivo
   
   *Controlli*: Verifica importi e condizioni
   
   *Tempistiche*: Entro 1 giorno lavorativo dall'erogazione

### Gestione Post-Erogazione

**Obiettivo**: Gestire il rapporto post-vendita e garantire la soddisfazione del cliente.

**Input**: Finanziamento erogato, documentazione contrattuale.

**Output**: Cliente soddisfatto, eventuali servizi aggiuntivi, referral.

**KPI**: 
- Tasso di soddisfazione cliente
- Numero di referral generati
- Tasso di cross-selling

![Processo BPMN Gestione Post-Erogazione](/home/ubuntu/finkrea_bpmn/diagrammi/post_erogazione.png)

#### Sotto-processi:

1. **Fatturazione**
   
   L'Amministrazione si occupa dell'emissione delle fatture per i servizi di mediazione creditizia, in conformità con le condizioni contrattuali e le normative fiscali.
   
   *Attività*: Emissione fatture per servizi di mediazione
   
   *Ruoli*: Amministrazione (R/A), Back Office (C)
   
   *Strumenti*: Software contabilità, CRM
   
   *Documentazione*: Fatture, ricevute pagamento
   
   *Controlli*: Verifica correttezza importi
   
   *Tempistiche*: Entro 5 giorni lavorativi dall'erogazione

2. **Follow-up Cliente**
   
   Il Collaboratore Commerciale contatta il cliente dopo l'erogazione per verificare la soddisfazione e raccogliere eventuali feedback. Questo contatto è importante per mantenere la relazione con il cliente e identificare opportunità di cross-selling o referral.
   
   *Attività*: Contatto post-vendita per verifica soddisfazione
   
   *Ruoli*: Collaboratore Commerciale (R), Back Office (C)
   
   *Strumenti*: CRM, telefono, email
   
   *Documentazione*: Scheda follow-up, questionario soddisfazione
   
   *Controlli*: Verifica problematiche emerse
   
   *Tempistiche*: Entro 15 giorni lavorativi dall'erogazione

3. **Gestione Richieste Post-Vendita**
   
   In caso di richieste specifiche da parte del cliente dopo l'erogazione, il Back Office coordina le attività necessarie per fornire supporto, coinvolgendo le funzioni competenti in base alla tipologia di richiesta.
   
   *Attività*: Supporto per eventuali necessità post-erogazione
   
   *Ruoli*: Back Office (R), Responsabile Delibera (A), Ufficio Legale (C)
   
   *Strumenti*: CRM, ticketing system
   
   *Documentazione*: Ticket assistenza, log interventi
   
   *Controlli*: Monitoraggio tempi risposta
   
   *Tempistiche*: Risposta entro 2 giorni lavorativi dalla richiesta

## Strumenti e Software

Per garantire l'efficienza e la qualità del processo operativo, Finkrea S.r.l. utilizza diversi strumenti e software, ciascuno dedicato a specifiche funzioni:

1. **CRM (Customer Relationship Management)**
   
   Sistema centrale per la gestione di tutte le informazioni relative ai clienti e alle pratiche. Permette di tracciare l'intero ciclo di vita del cliente, dalla fase di lead fino alla gestione post-vendita.
   
   *Funzionalità principali*:
   - Gestione contatti e lead
   - Tracciamento stato pratiche
   - Gestione appuntamenti
   - Archiviazione documentazione cliente
   - Reportistica e analisi

2. **Software Gestione Documentale**
   
   Piattaforma dedicata all'archiviazione e alla gestione di tutti i documenti relativi alle pratiche, con funzionalità avanzate per garantire la sicurezza e la conformità normativa.
   
   *Funzionalità principali*:
   - Archiviazione documenti
   - Gestione versioni
   - Firma digitale
   - Conformità GDPR
   - Ricerca avanzata

3. **Portali Banche**
   
   Accesso ai sistemi informativi degli istituti di credito partner per la gestione delle pratiche, il monitoraggio dello stato di avanzamento e la comunicazione diretta.
   
   *Funzionalità principali*:
   - Caricamento pratiche
   - Monitoraggio stato delibere
   - Download documentazione
   - Comunicazioni ufficiali

4. **Software Analisi Creditizia**
   
   Strumenti specializzati per l'analisi del merito creditizio e la simulazione di diverse soluzioni finanziarie, utili nella fase di pre-valutazione e presentazione delle offerte.
   
   *Funzionalità principali*:
   - Simulazioni finanziamenti
   - Calcolo capacità di credito
   - Analisi preliminare fattibilità
   - Comparazione offerte

5. **Sistema Contabilità**
   
   Software dedicato alla gestione degli aspetti amministrativi e contabili, inclusa la fatturazione e il controllo dei pagamenti.
   
   *Funzionalità principali*:
   - Fatturazione
   - Gestione pagamenti
   - Reportistica finanziaria
   - Controllo di gestione

6. **Sistemi Comunicazione**
   
   Strumenti per la comunicazione interna ed esterna, fondamentali per garantire un flusso efficiente di informazioni tra i diversi attori del processo.
   
   *Funzionalità principali*:
   - Email
   - PEC
   - Telefono
   - Videoconferenza
   - Messaggistica interna

## Documentazione e Modulistica

Il processo operativo di Finkrea S.r.l. richiede l'utilizzo di diversa documentazione e modulistica, organizzata per fasi del processo:

1. **Fase Acquisizione e Analisi**
   
   - Informativa Privacy (GDPR)
   - Questionario MiFID/adeguatezza
   - Scheda raccolta informazioni cliente
   - Mandato di mediazione creditizia
   - Checklist documenti necessari

2. **Fase Istruttoria**
   
   - Checklist documenti per tipologia pratica
   - Documenti identità e codice fiscale
   - Documenti reddituali (buste paga, dichiarazioni redditi)
   - Documenti patrimoniali (estratti conto, visure)
   - Documenti tecnici (perizie, planimetrie)
   - Report verifica documentale
   - Checklist controllo antiriciclaggio

3. **Fase Delibera ed Erogazione**
   
   - Contratto di finanziamento
   - Piano di ammortamento
   - Polizze assicurative collegate
   - Ricevute di pagamento commissioni
   - Checklist controllo pre-erogazione
   - Comunicazione esito delibera

4. **Fase Post-Erogazione**
   
   - Fatture
   - Questionari soddisfazione
   - Documentazione per assistenza post-vendita
   - Schede follow-up
   - Report analisi soddisfazione cliente

## Aspetti Normativi

Il processo operativo di Finkrea S.r.l. è stato progettato nel pieno rispetto della normativa vigente in materia di mediazione creditizia. Di seguito i principali aspetti normativi considerati:

1. **Normativa OAM**
   
   L'Organismo Agenti e Mediatori (OAM) regola l'attività di mediazione creditizia in Italia. Il processo rispetta tutti i requisiti previsti, inclusi:
   
   - Verifica requisiti per esercizio attività
   - Aggiornamento professionale obbligatorio
   - Comunicazioni obbligatorie
   - Rispetto dei limiti operativi

2. **Regolamenti Banca d'Italia**
   
   Il processo è conforme alle disposizioni emanate da Banca d'Italia in materia di:
   
   - Trasparenza bancaria
   - Requisiti patrimoniali
   - Segnalazioni obbligatorie
   - Gestione dei reclami

3. **GDPR (Privacy)**
   
   La gestione dei dati personali dei clienti avviene nel pieno rispetto del Regolamento Generale sulla Protezione dei Dati (GDPR), con particolare attenzione a:
   
   - Consenso informato
   - Diritto all'oblio
   - Sicurezza dati personali
   - Registro trattamenti
   - Data breach management

4. **Normativa Antiriciclaggio**
   
   Il processo include specifici controlli per garantire la conformità alla normativa antiriciclaggio:
   
   - Adeguata verifica clientela
   - Segnalazione operazioni sospette
   - Conservazione documentazione
   - Formazione del personale

5. **Trasparenza e Correttezza**
   
   Particolare attenzione è dedicata alla trasparenza e alla correttezza nei confronti dei clienti:
   
   - Informativa precontrattuale
   - TAEG e condizioni economiche
   - Diritto di recesso
   - Gestione dei reclami
   - Comunicazioni periodiche

## Governance e Miglioramento Continuo

Per garantire l'efficacia e l'efficienza del processo operativo nel tempo, Finkrea S.r.l. adotta un approccio strutturato alla governance e al miglioramento continuo:

1. **Responsabilità di Processo**
   
   - Il Responsabile Delibera è il process owner complessivo
   - Ogni macro-processo ha un responsabile dedicato
   - Riunioni periodiche di coordinamento tra responsabili

2. **Monitoraggio e Misurazione**
   
   - Dashboard KPI aggiornata mensilmente
   - Report trimestrali di performance
   - Analisi tempi medi per fase
   - Monitoraggio tasso di conversione e successo

3. **Gestione delle Non Conformità**
   
   - Registro delle non conformità
   - Analisi cause radice
   - Azioni correttive e preventive
   - Follow-up e verifica efficacia

4. **Formazione e Aggiornamento**
   
   - Piano di formazione annuale
   - Aggiornamento normativo continuo
   - Condivisione best practice
   - Affiancamento e coaching

5. **Revisione del Processo**
   
   - Revisione semestrale del processo
   - Analisi feedback clienti e collaboratori
   - Benchmarking con best practice di settore
   - Implementazione miglioramenti

## Glossario

| Termine | Definizione |
|---------|-------------|
| **Lead** | Potenziale cliente che ha mostrato interesse per i servizi di mediazione creditizia |
| **TAEG** | Tasso Annuo Effettivo Globale, indicatore del costo totale del credito |
| **Delibera** | Decisione dell'istituto di credito in merito alla concessione del finanziamento |
| **OAM** | Organismo Agenti e Mediatori, ente che regola l'attività di mediazione creditizia |
| **Istruttoria** | Fase di raccolta e verifica della documentazione necessaria per la valutazione del merito creditizio |
| **KPI** | Key Performance Indicator, indicatore chiave di prestazione utilizzato per misurare l'efficacia del processo |
| **GDPR** | General Data Protection Regulation, regolamento europeo sulla protezione dei dati personali |
| **Antiriciclaggio** | Normativa volta a prevenire l'utilizzo del sistema finanziario a scopo di riciclaggio |
| **Cross-selling** | Vendita di prodotti o servizi aggiuntivi a clienti esistenti |
| **RACI** | Responsible, Accountable, Consulted, Informed - matrice che definisce le responsabilità nel processo |
| **MiFID** | Markets in Financial Instruments Directive, direttiva europea sui mercati degli strumenti finanziari |
| **PEC** | Posta Elettronica Certificata, sistema di posta elettronica con valore legale |
