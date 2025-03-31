from collections import defaultdict
edge_list = [
    (0,1),
    (1,3),
    (3,4),
    (4,7),
    (7,2),
    (0,2),
    (2,5),
    (2,6)
]

N = 8
# Adjacency Matrix
adj_matrix = [[0 for _ in range(N)] for _ in range(N)]
for u,v in edge_list:
    adj_matrix[u][v] = 1

# print(adj_matrix)

# Adjacency List
adj_list = defaultdict(list)

for u,v in edge_list:
    adj_list[u].append(v)

print(adj_list)

#dfs using recursion

