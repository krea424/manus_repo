import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle, Polygon
import matplotlib.patheffects as path_effects

# Crea la directory per i diagrammi BPMN
os.makedirs('/home/ubuntu/finkrea_bpmn/diagrammi', exist_ok=True)

# Colori per i diversi attori
COLORS = {
    'Back Office': '#AED6F1',
    'Collaboratore Commerciale': '#D5F5E3',
    'Responsabile Delibera': '#FADBD8',
    'Ufficio Legale': '#F9E79F',
    'Amministrazione': '#D2B4DE',
    'Cliente': '#F5CBA7',
    'Banche': '#D6EAF8'
}

# Funzione per creare un diagramma BPMN
def create_bpmn_diagram(title, actors, elements, connections, filename):
    # Calcola l'altezza del diagramma in base al numero di attori
    height = len(actors) * 2 + 1
    
    # Crea la figura e l'asse
    fig, ax = plt.subplots(figsize=(16, height))
    
    # Imposta i limiti dell'asse
    ax.set_xlim(0, 20)
    ax.set_ylim(0, height)
    
    # Rimuovi gli assi
    ax.axis('off')
    
    # Aggiungi il titolo
    ax.set_title(title, fontsize=16, fontweight='bold')
    
    # Disegna le swimlanes per ogni attore
    for i, actor in enumerate(actors):
        y = height - i * 2 - 1
        
        # Disegna la swimlane
        rect = Rectangle((0, y - 1), 20, 2, facecolor=COLORS.get(actor, '#E5E8E8'), 
                         edgecolor='black', alpha=0.5)
        ax.add_patch(rect)
        
        # Aggiungi il nome dell'attore
        ax.text(0.5, y, actor, fontsize=10, fontweight='bold', 
                ha='left', va='center')
    
    # Disegna gli elementi
    for element in elements:
        element_type = element['type']
        x, y = element['position']
        label = element.get('label', '')
        
        if element_type == 'start':
            circle = Circle((x, y), 0.3, facecolor='#2ECC71', edgecolor='black')
            ax.add_patch(circle)
        
        elif element_type == 'end':
            circle = Circle((x, y), 0.3, facecolor='#E74C3C', edgecolor='black')
            ax.add_patch(circle)
        
        elif element_type == 'task':
            rect = Rectangle((x - 1, y - 0.5), 2, 1, facecolor='white', 
                             edgecolor='black', alpha=0.8, 
                             path_effects=[path_effects.withSimplePatchShadow()])
            ax.add_patch(rect)
            ax.text(x, y, label, fontsize=8, ha='center', va='center', wrap=True)
        
        elif element_type == 'gateway':
            diamond = Polygon([[x, y + 0.4], [x + 0.4, y], [x, y - 0.4], [x - 0.4, y]], 
                              facecolor='white', edgecolor='black')
            ax.add_patch(diamond)
            ax.text(x, y, 'X' if element.get('exclusive', True) else '+', 
                    fontsize=10, ha='center', va='center')
            if label:
                ax.text(x, y - 0.6, label, fontsize=7, ha='center', va='center')
    
    # Disegna le connessioni
    for connection in connections:
        start_x, start_y = connection['start']
        end_x, end_y = connection['end']
        label = connection.get('label', '')
        
        # Crea la freccia
        arrow = FancyArrowPatch((start_x, start_y), (end_x, end_y), 
                                arrowstyle='->', color='black', 
                                connectionstyle='arc3,rad=0.1')
        ax.add_patch(arrow)
        
        # Aggiungi l'etichetta alla connessione
        if label:
            # Calcola il punto medio della connessione
            mid_x = (start_x + end_x) / 2
            mid_y = (start_y + end_y) / 2
            
            # Aggiungi un piccolo offset per evitare sovrapposizioni
            offset_x = 0.2 if start_y == end_y else 0
            offset_y = 0.2 if start_x == end_x else 0
            
            ax.text(mid_x + offset_x, mid_y + offset_y, label, 
                    fontsize=7, ha='center', va='center', 
                    bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))
    
    # Salva il diagramma
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    
    return filename

# Genera il diagramma BPMN per il macro-processo "Acquisizione Lead"
def generate_acquisizione_lead_bpmn():
    title = "Processo BPMN: Acquisizione Lead - Finkrea S.r.l."
    
    actors = [
        "Collaboratore Commerciale",
        "Back Office",
        "Cliente"
    ]
    
    elements = [
        {'type': 'start', 'position': (1, 9)},
        {'type': 'task', 'position': (3, 9), 'label': 'Gestione campagne marketing'},
        {'type': 'task', 'position': (6, 9), 'label': 'Generazione lead'},
        {'type': 'task', 'position': (9, 9), 'label': 'Primo contatto telefonico'},
        {'type': 'gateway', 'position': (12, 9), 'label': 'Cliente interessato?'},
        {'type': 'task', 'position': (15, 9), 'label': 'Fissare appuntamento'},
        {'type': 'task', 'position': (15, 5), 'label': 'Ricevere conferma appuntamento'},
        {'type': 'task', 'position': (18, 9), 'label': 'Preparare materiale per appuntamento'},
        {'type': 'end', 'position': (19, 9)},
        {'type': 'end', 'position': (12, 7), 'label': 'Fine - Lead non qualificato'}
    ]
    
    connections = [
        {'start': (1, 9), 'end': (3, 9)},
        {'start': (3, 9), 'end': (6, 9)},
        {'start': (6, 9), 'end': (9, 9)},
        {'start': (9, 9), 'end': (12, 9)},
        {'start': (12, 9), 'end': (15, 9), 'label': 'Sì'},
        {'start': (12, 9), 'end': (12, 7), 'label': 'No'},
        {'start': (15, 9), 'end': (15, 5)},
        {'start': (15, 5), 'end': (18, 9)},
        {'start': (18, 9), 'end': (19, 9)}
    ]
    
    return create_bpmn_diagram(title, actors, elements, connections, 
                              '/home/ubuntu/finkrea_bpmn/diagrammi/acquisizione_lead.png')

# Genera il diagramma BPMN per il macro-processo "Analisi Preliminare"
def generate_analisi_preliminare_bpmn():
    title = "Processo BPMN: Analisi Preliminare - Finkrea S.r.l."
    
    actors = [
        "Collaboratore Commerciale",
        "Responsabile Delibera",
        "Back Office",
        "Cliente"
    ]
    
    elements = [
        {'type': 'start', 'position': (1, 9)},
        {'type': 'task', 'position': (3, 9), 'label': 'Colloquio conoscitivo'},
        {'type': 'task', 'position': (3, 7), 'label': 'Fornire informazioni e documenti'},
        {'type': 'task', 'position': (6, 9), 'label': 'Raccolta esigenze cliente'},
        {'type': 'task', 'position': (6, 5), 'label': 'Supporto analisi preliminare'},
        {'type': 'task', 'position': (9, 7), 'label': 'Pre-valutazione fattibilità'},
        {'type': 'gateway', 'position': (12, 7), 'label': 'Richiesta fattibile?'},
        {'type': 'task', 'position': (15, 7), 'label': 'Presentazione soluzioni'},
        {'type': 'gateway', 'position': (15, 5), 'label': 'Cliente accetta?'},
        {'type': 'task', 'position': (18, 5), 'label': 'Avvio istruttoria pratica'},
        {'type': 'end', 'position': (19, 5)},
        {'type': 'end', 'position': (12, 3), 'label': 'Fine - Richiesta non fattibile'},
        {'type': 'end', 'position': (15, 3), 'label': 'Fine - Cliente non interessato'}
    ]
    
    connections = [
        {'start': (1, 9), 'end': (3, 9)},
        {'start': (3, 9), 'end': (3, 7)},
        {'start': (3, 7), 'end': (6, 9)},
        {'start': (6, 9), 'end': (6, 5)},
        {'start': (6, 5), 'end': (9, 7)},
        {'start': (9, 7), 'end': (12, 7)},
        {'start': (12, 7), 'end': (15, 7), 'label': 'Sì'},
        {'start': (12, 7), 'end': (12, 3), 'label': 'No'},
        {'start': (15, 7), 'end': (15, 5)},
        {'start': (15, 5), 'end': (18, 5), 'label': 'Sì'},
        {'start': (15, 5), 'end': (15, 3), 'label': 'No'},
        {'start': (18, 5), 'end': (19, 5)}
    ]
    
    return create_bpmn_diagram(title, actors, elements, connections, 
                              '/home/ubuntu/finkrea_bpmn/diagrammi/analisi_preliminare.png')

# Genera il diagramma BPMN per il macro-processo "Istruttoria Pratica"
def generate_istruttoria_pratica_bpmn():
    title = "Processo BPMN: Istruttoria Pratica - Finkrea S.r.l."
    
    actors = [
        "Collaboratore Commerciale",
        "Back Office",
        "Responsabile Delibera",
        "Ufficio Legale",
        "Cliente"
    ]
    
    elements = [
        {'type': 'start', 'position': (1, 11)},
        {'type': 'task', 'position': (3, 11), 'label': 'Richiesta documenti al cliente'},
        {'type': 'task', 'position': (3, 3), 'label': 'Fornire documentazione richiesta'},
        {'type': 'gateway', 'position': (6, 11), 'label': 'Documenti ricevuti?'},
        {'type': 'task', 'position': (6, 9), 'label': 'Verifica completezza documentale'},
        {'type': 'gateway', 'position': (9, 9), 'label': 'Documentazione completa?'},
        {'type': 'task', 'position': (9, 7), 'label': 'Verifica conformità normativa'},
        {'type': 'task', 'position': (12, 9), 'label': 'Preparazione fascicolo'},
        {'type': 'task', 'position': (12, 5), 'label': 'Supervisione istruttoria'},
        {'type': 'task', 'position': (15, 9), 'label': 'Controllo finale fascicolo'},
        {'type': 'end', 'position': (18, 9)},
        {'type': 'task', 'position': (6, 13), 'label': 'Sollecito documenti mancanti'}
    ]
    
    connections = [
        {'start': (1, 11), 'end': (3, 11)},
        {'start': (3, 11), 'end': (3, 3)},
        {'start': (3, 3), 'end': (6, 11)},
        {'start': (6, 11), 'end': (6, 9), 'label': 'Sì'},
        {'start': (6, 11), 'end': (6, 13), 'label': 'No'},
        {'start': (6, 13), 'end': (3, 11)},
        {'start': (6, 9), 'end': (9, 9)},
        {'start': (9, 9), 'end': (9, 7), 'label': 'Sì'},
        {'start': (9, 9), 'end': (3, 11), 'label': 'No'},
        {'start': (9, 7), 'end': (12, 9)},
        {'start': (12, 9), 'end': (12, 5)},
        {'start': (12, 5), 'end': (15, 9)},
        {'start': (15, 9), 'end': (18, 9)}
    ]
    
    return create_bpmn_diagram(title, actors, elements, connections, 
                              '/home/ubuntu/finkrea_bpmn/diagrammi/istruttoria_pratica.png')

# Genera il diagramma BPMN per il macro-processo "Delibera"
def generate_delibera_bpmn():
    title = "Processo BPMN: Delibera - Finkrea S.r.l."
    
    actors = [
        "Back Office",
        "Responsabile Delibera",
        "Banche",
        "Collaboratore Commerciale",
        "Cliente"
    ]
    
    elements = [
        {'type': 'start', 'position': (1, 9)},
        {'type': 'task', 'position': (3, 9), 'label': 'Invio pratica a istituto di credito'},
        {'type': 'task', 'position': (3, 5), 'label': 'Valutazione pratica'},
        {'type': 'task', 'position': (6, 9), 'label': 'Monitoraggio stato pratica'},
        {'type': 'gateway', 'position': (9, 9), 'label': 'Richiesta integrazioni?'},
        {'type': 'task', 'position': (9, 11), 'label': 'Richiesta documenti aggiuntivi'},
        {'type': 'task', 'position': (9, 3), 'label': 'Fornire documenti aggiuntivi'},
        {'type': 'task', 'position': (12, 9), 'label': 'Ricezione esito delibera'},
        {'type': 'gateway', 'position': (15, 9), 'label': 'Esito positivo?'},
        {'type': 'task', 'position': (15, 7), 'label': 'Comunicazione esito al cliente'},
        {'type': 'task', 'position': (18, 9), 'label': 'Avvio fase erogazione'},
        {'type': 'end', 'position': (19, 9)},
        {'type': 'end', 'position': (15, 5), 'label': 'Fine - Pratica rifiutata'}
    ]
    
    connections = [
        {'start': (1, 9), 'end': (3, 9)},
        {'start': (3, 9), 'end': (3, 5)},
        {'start': (3, 5), 'end': (6, 9)},
        {'start': (6, 9), 'end': (9, 9)},
        {'start': (9, 9), 'end': (9, 11), 'label': 'Sì'},
        {'start': (9, 11), 'end': (9, 3)},
        {'start': (9, 3), 'end': (3, 9)},
        {'start': (9, 9), 'end': (12, 9), 'label': 'No'},
        {'start': (12, 9), 'end': (15, 9)},
        {'start': (15, 9), 'end': (15, 7), 'label': 'No'},
        {'start': (15, 7), 'end': (15, 5)},
        {'start': (15, 9), 'end': (18, 9), 'label': 'Sì'},
        {'start': (18, 9), 'end': (19, 9)}
    ]
    
    return create_bpmn_diagram(title, actors, elements, connections, 
                              '/home/ubuntu/finkrea_bpmn/diagrammi/delibera.png')

# Genera il diagramma BPMN per il macro-processo "Erogazione"
def generate_erogazione_bpmn():
    title = "Processo BPMN: Erogazione - Finkrea S.r.l."
    
    actors = [
        "Back Office",
        "Ufficio Legale",
        "Responsabile Delibera",
        "Collaboratore Commerciale",
        "Amministrazione",
        "Banche",
        "Cliente"
    ]
    
    elements = [
        {'type': 'start', 'position': (1, 13)},
        {'type': 'task', 'position': (3, 13), 'label': 'Preparazione contrattualistica'},
        {'type': 'task', 'position': (3, 11), 'label': 'Verifica conformità contratti'},
        {'type': 'task', 'position': (6, 13), 'label': 'Approvazione documenti finali'},
        {'type': 'task', 'position': (6, 9), 'label': 'Organizzazione incontro per firma'},
        {'type': 'task', 'position': (6, 3), 'label': 'Firma contratti'},
        {'type': 'task', 'position': (9, 9), 'label': 'Invio contratti firmati'},
        {'type': 'task', 'position': (9, 5), 'label': 'Erogazione finanziamento'},
        {'type': 'task', 'position': (12, 9), 'label': 'Verifica avvenuta erogazione'},
        {'type': 'task', 'position': (12, 7), 'label': 'Registrazione erogazione'},
        {'type': 'task', 'position': (15, 9), 'label': 'Comunicazione al cliente'},
        {'type': 'end', 'position': (18, 9)}
    ]
    
    connections = [
        {'start': (1, 13), 'end': (3, 13)},
        {'start': (3, 13), 'end': (3, 11)},
        {'start': (3, 11), 'end': (6, 13)},
        {'start': (6, 13), 'end': (6, 9)},
        {'start': (6, 9), 'end': (6, 3)},
        {'start': (6, 3), 'end': (9, 9)},
        {'start': (9, 9), 'end': (9, 5)},
        {'start': (9, 5), 'end': (12, 9)},
        {'start': (12, 9), 'end': (12, 7)},
        {'start': (12, 7), 'end': (15, 9)},
        {'start': (15, 9), 'end': (18, 9)}
    ]
    
    return create_bpmn_diagram(title, actors, elements, connections, 
                              '/home/ubuntu/finkrea_bpmn/diagrammi/erogazione.png')

# Genera il diagramma BPMN per il macro-processo "Gestione Post-Erogazione"
def generate_post_erogazione_bpmn():
    title = "Processo BPMN: Gestione Post-Erogazione - Finkrea S.r.l."
    
    actors = [
        "Amministrazione",
        "Back Office",
        "Collaboratore Commerciale",
        "Responsabile Delibera",
        "Ufficio Legale",
        "Cliente"
    ]
    
    elements = [
        {'type': 'start', 'position': (1, 11)},
        {'type': 'task', 'position': (3, 11), 'label': 'Emissione fatture'},
        {'type': 'task', 'position': (6, 11), 'label': 'Registrazione pagamenti'},
        {'type': 'task', 'position': (6, 9), 'label': 'Archiviazione pratica completa'},
        {'type': 'task', 'position': (9, 7), 'label': 'Follow-up cliente'},
        {'type': 'gateway', 'position': (12, 7), 'label': 'Richieste post-vendita?'},
        {'type': 'task', 'position': (12, 5), 'label': 'Gestione richiesta assistenza'},
        {'type': 'gateway', 'position': (15, 5), 'label': 'Tipo richiesta?'},
        {'type': 'task', 'position': (15, 9), 'label': 'Supporto amministrativo'},
        {'type': 'task', 'position': (15, 3), 'label': 'Supporto legale/contrattuale'},
        {'type': 'task', 'position': (18, 7), 'label': 'Chiusura pratica post-vendita'},
        {'type': 'end', 'position': (19, 7)}
    ]
    
    connections = [
        {'start': (1, 11), 'end': (3, 11)},
        {'start': (3, 11), 'end': (6, 11)},
        {'start': (6, 11), 'end': (6, 9)},
        {'start': (6, 9), 'end': (9, 7)},
        {'start': (9, 7), 'end': (12, 7)},
        {'start': (12, 7), 'end': (12, 5), 'label': 'Sì'},
        {'start': (12, 7), 'end': (18, 7), 'label': 'No'},
        {'start': (12, 5), 'end': (15, 5)},
        {'start': (15, 5), 'end': (15, 9), 'label': 'Amministrativa'},
        {'start': (15, 5), 'end': (15, 3), 'label': 'Legale'},
        {'start': (15, 9), 'end': (18, 7)},
        {'start': (15, 3), 'end': (18, 7)},
        {'start': (18, 7), 'end': (19, 7)}
    ]
    
    return create_bpmn_diagram(title, actors, elements, connections, 
                              '/home/ubuntu/finkrea_bpmn/diagrammi/post_erogazione.png')

# Genera il diagramma BPMN per il processo completo
def generate_processo_completo_bpmn():
    title = "Processo BPMN Completo - Finkrea S.r.l."
    
    actors = [
        "Collaboratore Commerciale",
        "Back Office",
        "Responsabile Delibera",
        "Ufficio Legale",
        "Amministrazione",
        "Banche",
        "Cliente"
    ]
    
    elements = [
        {'type': 'start', 'position': (1, 13)},
        {'type': 'task', 'position': (3, 13), 'label': 'Acquisizione Lead'},
        {'type': 'task', 'position': (6, 13), 'label': 'Analisi Preliminare'},
        {'type': 'gateway', 'position': (9, 13), 'label': 'Richiesta fattibile?'},
        {'type': 'task', 'position': (12, 13), 'label': 'Istruttoria Pratica'},
        {'type': 'task', 'position': (15, 13), 'label': 'Delibera'},
        {'type': 'gateway', 'position': (18, 13), 'label': 'Esito positivo?'},
        {'type': 'task', 'position': (18, 11), 'label': 'Erogazione'},
        {'type': 'task', 'position': (18, 9), 'label': 'Gestione Post-Erogazione'},
        {'type': 'end', 'position': (19, 9)},
        {'type': 'end', 'position': (9, 11), 'label': 'Fine - Richiesta non fattibile'},
        {'type': 'end', 'position': (18, 15), 'label': 'Fine - Pratica rifiutata'}
    ]
    
    connections = [
        {'start': (1, 13), 'end': (3, 13)},
        {'start': (3, 13), 'end': (6, 13)},
        {'start': (6, 13), 'end': (9, 13)},
        {'start': (9, 13), 'end': (12, 13), 'label': 'Sì'},
        {'start': (9, 13), 'end': (9, 11), 'label': 'No'},
        {'start': (12, 13), 'end': (15, 13)},
        {'start': (15, 13), 'end': (18, 13)},
        {'start': (18, 13), 'end': (18, 11), 'label': 'Sì'},
        {'start': (18, 13), 'end': (18, 15), 'label': 'No'},
        {'start': (18, 11), 'end': (18, 9)},
        {'start': (18, 9), 'end': (19, 9)}
    ]
    
    return create_bpmn_diagram(title, actors, elements, connections, 
                              '/home/ubuntu/finkrea_bpmn/diagrammi/processo_completo.png')

# Genera tutti i diagrammi BPMN
def generate_all_bpmn_diagrams():
    acquisizione_lead = generate_acquisizione_lead_bpmn()
    analisi_preliminare = generate_analisi_preliminare_bpmn()
    istruttoria_pratica = generate_istruttoria_pratica_bpmn()
    delibera = generate_delibera_bpmn()
    erogazione = generate_erogazione_bpmn()
    post_erogazione = generate_post_erogazione_bpmn()
    processo_completo = generate_processo_completo_bpmn()
    
    return {
        'acquisizione_lead': acquisizione_lead,
        'analisi_preliminare': analisi_preliminare,
        'istruttoria_pratica': istruttoria_pratica,
        'delibera': delibera,
        'erogazione': erogazione,
        'post_erogazione': post_erogazione,
        'processo_completo': processo_completo
    }

# Esegui la generazione dei diagrammi
if __name__ == "__main__":
    print("Generazione diagrammi BPMN per Finkrea S.r.l. in corso...")
    diagrams = generate_all_bpmn_diagrams()
    print("Diagrammi BPMN generati con successo:")
    for name, path in diagrams.items():
        print(f"- {name}: {path}")
