"""
This is a collection of useful functions
to be used for graph analysis
"""

### [10 mai 2025] This file is derived from the Master version to be found in the methodology project:
### sciences_historiques_numeriques/histoire_numerique_methodes/analyse_reseaux/network_analysis_functions.py
## Any change must be reported to that Master file


import pprint as pprint
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


### Basic properties of a graph

# MultiGraph: Undirected graphs with self loops and parallel edges
# https://networkx.org/documentation/stable/reference/classes/index.html

def basic_graph_properties(G):

    pprint.pprint({'is_multigraph':G.is_multigraph(), 
        'is_directed':G.is_directed(), 
        'number_of_nodes': G.number_of_nodes(), 
        'number_of_edges':G.number_of_edges(),
         '------' : '------',
        'is connected': nx.is_connected(nx.to_undirected(G)), 
        'components': len(list(nx.connected_components(nx.to_undirected(G)))),
        'density': nx.density(G)}, sort_dicts=False)



### Remove the attributes listed in a Python list from all nodes

# attrs_to_remove : the list of attribute names

def remove_node_attributes(G, attrs_to_remove):
    for node in G.nodes():
        for attr in attrs_to_remove:
            if attr in G.nodes[node]:
                del G.nodes[node][attr]



def describe_violinplot(il, plot_title, figsize=(20, 6)):

    sl_id = pd.Series(il)
    print(sl_id.describe())

    plt.figure(figsize=figsize)
    p = sns.violinplot(data=sl_id, orient='h', cut=0)
    plt.title(plot_title)
    plt.show()

   

###  Describe and plot distribution of integers' list

def describe_plot_integers_distribution(il, plot_title, figsize=(20, 6)):

    sl_id = pd.Series(il)
    print(sl_id.describe())

    ## Distribution of the indegree
    df_l = pd.DataFrame(sl_id.groupby(by=sl_id).size().items())
    df_l.columns=['value', 'number']

    fig, ax = plt.subplots(1,1, figsize=figsize)

    plt.bar(df_l.value, df_l.number)

    # ax.xaxis.get_major_locator().set_params(integer=True)
    plt.xticks(range(min(df_l.value), max(df_l.value)+1));
    ax.yaxis.get_major_locator().set_params(integer=True)
    ax.bar_label(ax.containers[-1])
    plt.xticks(size=8)
    plt.xlabel('Values', size=9)
    plt.yticks(size=8)
    plt.ylabel('Number of values', size=9)
    plt.title(plot_title, size=10)

    plt.margins(x=0.02, y=0.1)

    plt.tight_layout()

    plt.show()            