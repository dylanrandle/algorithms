## implementation of Kosaraju's two-pass algorithm for computing strongly-connected components in a directed graph
def parse_input(raw_in_file):
    with open(raw_in_file) as f:
        raw_in = f.readlines()
    edge_list = []
    for i in range(len(raw_in)):
        if raw_in[i] != '\n':
            edge_list.append(list(map(int, raw_in[i].split())))
    return edge_list

edge_list = parse_input('data/scc.txt')

import numpy as np
def parse_edge_list(edge_list, reverse=False):
    graph = {}
    for elem in edge_list:
        if reverse:
            tail, head = elem[1], elem[0]
        else:
            tail, head = elem[0], elem[1]
        if tail in graph:
            graph[tail]['heads'].append(head)
        else:
            graph[tail] = {'heads': [head], 'explored': False}
    # fill in any missing vertices with empty heads
    max_node = np.amax(edge_list)
    for i in range(1, max_node+1):
        if i not in graph:
            graph[i] = {'heads': [], 'explored': False}
    return graph

graph = parse_edge_list(edge_list)
graph_rev = parse_edge_list(edge_list, reverse=True)

def dfs_loop(G, model, ordering=None):
    n = len(G.keys())
    if not ordering:
        ordering = list(range(n, 0, -1))
    for i in ordering:
        if not G[i]['explored']:
            model['s'] = i
            dfs(G, i, model)

def dfs(G, i, model):
    G[i]['explored'] = True
    model['leader'][i] = model['s']
    for j in G[i]['heads']:
        if not G[j]['explored']:
            dfs(G, j, model)
    model['t'] += 1
    model['f'][i] = model['t']

from collections import Counter
def kosaraju():
    model = {
        't': 0,
        's': None,
        'f': {},
        'leader': {}
    }
    dfs_loop(graph_rev, model)
    dfs_loop(graph, model, ordering=list(reversed(list((model['f'].keys())))))
    leaders = list(model['leader'].values())
    counts = Counter(leaders)
    print('the largest sccs are: %s' % list(sorted(counts.values(), reverse=True))[:5])

import sys
import threading
sys.setrecursionlimit(2 ** 20)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=kosaraju)
thread.start()
