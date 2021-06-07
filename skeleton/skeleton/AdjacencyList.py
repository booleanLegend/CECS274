"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
from ArrayList import ArrayList
from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack


class AdjacencyList(Graph):
    def __init__(self, n: int):
        self.n = n
        self.adj = np.zeros(self.n, object)
        for i in range(self.n):
            self.adj[i] = ArrayList()

    def new_boolean_matrix(self, n):
        return np.zeros(n, np.bool_)

    def new_boolean_array(self, n):
        return np.zeros(n, np.bool_)

    def add_edge(self, i: int, j: int):
        self.adj[i].append(j)

    def remove_edge(self, i: int, j: int):
        for k in range(len(self.adj[i]) - 1):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return

    def has_edge(self, i: int, j: int) -> bool:
        for k in self.adj[i]:
            if k == j:
                return True
        return False

    def out_edges(self, i) -> List:
        return self.adj[i]

    def in_edges(self, i) -> List:
        out = ArrayList()
        for j in range(self.n):
            if self.has_edge(j, i):
                out.append(j)
        return out

    def size(self) -> int:
        # todo
        pass

    def bfs(self, r: int):
        seen = self.new_boolean_array(self.n)
        q = ArrayQueue()
        q.add(r)
        seen[r] = True
        while q.size() > 0:
            i = q.remove()
            ngh = self.out_edges(i)
            for k in range(ngh.size()):
                j = ngh.get(k)
                if not seen[j]:
                    q.add(j)
                    seen[j] = True

    def dfs(self, r: int):
        seen = np.zeros(self.n)
        s = ArrayStack()
        s.push(r)
        while s.size() > 0:
            i = s.pop()
            seen[i] = True
            ngh = self.out_edges(i)
            for j in range(ngh.size()):
                if not seen[ngh.get(j)]:
                    s.push(ngh.get(j))
                else:
                    continue

    def dfs2(self, r1: int, r2: int):
        d = np.zeros(self.n)
        d[r1] = 0
        seen = self.new_boolean_array(self.n)
        s = ArrayStack()
        s.push(r1)
        while s.size() > 0:
            i = s.pop()
            seen[i] = True
            ngh = self.out_edges(i)
            for j in range(0, ngh.size()):
                if not seen[ngh.get(j)]:
                    s.push(ngh.get(j))
                    d[ngh.get(j)] = d[i] + 1
                    if ngh.get(j) == r2:
                        return d[ngh.get(j)]
                else:
                    continue
        return -1

    def bfs2(self, r: int, k: int):
        seen = np.zeros(self.n, np.bool_)
        d = 0
        q = ArrayQueue()
        q.add(r)
        seen[r] = True
        l = [r]
        while q.size() > 0 and d < k:
            i = q.remove()
            ngh = self.out_edges(i)
            for k in range(ngh.size()):
                j = ngh.get(k)
                if not seen[j]:
                    q.add(j)
                    l.append(j)
                    seen[j] = True
            d += 1
        return l

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s
