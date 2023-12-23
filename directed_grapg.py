import networkx as nx
import matplotlib.pyplot as plt
import random

# Define the words and their phonetic representations
words = {}
with open('arpabet_pronunciations_NEW copy.txt', 'r') as f:
    for line in f:
        word, phonetic = line.strip().split(': ')
        words[word] = phonetic

# Define the vowels
vowels = ['AA', 'AE', 'AH', 'AO', 'AW', 'AX', 'AXR', 'AY', 'EH', 'ER', 'EY', 'IH', 'IX', 'IY', 'OW', 'OY', 'UH', 'UW', 'UX']

# Define the consonants
consonants = ['B', 'CH', 'D', 'DH', 'DX', 'EL', 'EM', 'EN', 'F', 'G', 'HH', 'JH', 'K', 'L', 'M', 'N', 'NG', 'NX', 'P', 'Q', 'R', 'S', 'SH', 'T', 'TH', 'V', 'W', 'WH', 'Y', 'Z', 'ZH']

# Create a directed graph
G = nx.DiGraph()

# Create a dictionary to store the weights of the edges
weights = {}

# Iterate over the words and their phonetic representations
for word, phonetic in words.items():
    # Split the phonetic representation into syllables
    syllables = phonetic.split('.')
    for syllable in syllables:
        # Split the syllable into symbols
        symbols = syllable.split('-')
        # Add all symbols to the graph
        for i in range(len(symbols) - 1):
            edge = (symbols[i], symbols[i+1])
            if edge in weights:
                weights[edge] += 1
            else:
                weights[edge] = 1
            G.add_edge(*edge, weight=weights[edge])
        # Add edges from 'Start' to the first symbol and from the last symbol to 'End'
        G.add_edge('Start', symbols[0], weight=weights.get(('Start', symbols[0]), 1))
        G.add_edge(symbols[-1], 'End', weight=weights.get((symbols[-1], 'End'), 1))

# Create a custom layout
def custom_layout(G, vowels):
    pos = {}
    nodes = list(G.nodes())
    nodes.remove('Start')
    nodes.remove('End')
    # Separate the nodes into onset, nucleus, and coda
    onset = [node for node in nodes if G.has_edge('Start', node) and G['Start'][node]['weight'] > 0 and node not in vowels]
    nucleus = [node for node in nodes if node in vowels]
    coda = [node for node in nodes if G.has_edge(node, 'End') and G[node]['End']['weight'] > 0 and node not in vowels]
    # Place the nodes
    for i, node in enumerate(onset):
        pos[node] = [(i+1)/(len(onset)+2), random.uniform(0.1, 0.9)]
    for i, node in enumerate(nucleus):
        pos[node] = [0.5, (i+1)/(len(nucleus)+2)]
    for i, node in enumerate(coda):
        pos[node] = [1-(i+1)/(len(coda)+2), random.uniform(0.1, 0.9)]
    pos['Start'] = [0, 0.5]
    pos['End'] = [1, 0.5]
    return pos

# Draw the graph
pos = custom_layout(G, vowels)

nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, width=[G[u][v]['weight'] for u,v in G.edges()])
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
plt.show()
