from collections import defaultdict, deque
from typing import List
#DFS : parcourir en profondeur le graphe pour check que tout est connecté
# (BFS on priviligie la source, DFS on privilégie les voisins du noeud visité
#dans ce cas, pas de préférence entre BFS et DFS

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # 3. BFS with Deque
        if source == destination:
            return True

        # Adjacency list using dictionary
        graph = defaultdict(list)
        for u,v in edges:
            #bidirectionnal
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        seen.add(source)

        q = deque()
        q.append(source)
        while q:
            #popleft permet de faire le BFS (juste pop fait DFS)
            node = q.popleft()
            if node == destination:
                return True
            for nei_node in graph[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    q.append(nei_node)

        return False
#Time and Space are the same for the 3 methods
#Time : O(N + E)
#Space : O(N + E)

"""
1. DFS with recursion
        if source == destination:
            return True

        # Adjacency list using dictionary
        graph = defaultdict(list)
        for u,v in edges:
            #bidirectionnal
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        seen.add(source)

        def dfs(i):
            if i == destination:
                return True
            for nei_node in graph[i]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    if dfs(nei_node):
                        return True
            #not all nodes found
            return False

        return dfs(source)
"""

"""
2. DFS with stack (iterative)
        if source == destination:
            return True

        # Adjacency list using dictionary
        graph = defaultdict(list)
        for u,v in edges:
            #bidirectionnal
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        seen.add(source)

        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for nei_node in graph[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    stack.append(nei_node)


        return False
"""