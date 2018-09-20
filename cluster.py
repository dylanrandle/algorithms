## Clustering algorithms

input = [list(map(int, x.split(' '))) for x in open('data/clustering1.txt', 'r').read().split('\n')[1:-1]]

def basic_greedy_max_spacing(input, k):
    num_clusters = len(input)
    while num_clusters > k:
        
