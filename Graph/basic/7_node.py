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

print(adj_list) #{0: [1, 2], 1: [3], 3: [4], 4: [7], 7: [2], 2: [5, 6]}


#dfs using recursion
seen = set()
start = 0
seen.add(start)

def dfs(node):
    print(node)
    for ng in adj_list[node]:
        if ng not in seen:
            seen.add(ng)
            dfs(ng)

# dfs(start)

#dfs using stack
seen = set()
start = 0
stack = [start]
seen.add(start)
while stack:
    node = stack.pop()
    print(node)
    for ng in adj_list[node]:
        if ng not in seen:
            seen.add(ng)
            stack.append(ng)

# bfs using queue
from collections import deque
visited = set()
start = 0
queue = deque([start])
while queue:
    node = queue.popleft()
    print(node)
    for ng in adj_list[node]:
        if ng not in visited:
            visited.add(ng)
            queue.append(ng)



