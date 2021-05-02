
import numpy as np


class WeightedQuickUnionUF:
    """
    data structure ids[] of size num
    interpretation: ids[i] is parent of i

    ROOT of i is ids[ids[... ids[i] ...]]
    only smaller tree added down below

    Authors suggest to maintain an array size 
    """

    def __init__(self, num: int) -> None:
        self.num = num
        self.ids = np.arange(self.num, dtype=np.int)
        self.sizes = np.ones(shape=(self.num,), dtype=np.int)
        self.roots = None

    def get_root(self, ind: int) -> int:
        while ind != self.ids[ind]:
            ind = self.ids[ind]
        return ind

    def union(self, p: int, q: int) -> None:

        assert p < self.num and q < self.num
        p_root = self.get_root(p)
        q_root = self.get_root(q)
        if p_root == q_root:
            return None
        if self.sizes[p_root] < self.sizes[q_root]:
            self.ids[p_root] = q_root
            self.sizes[q_root] += self.sizes[p_root]
        else:
            self.ids[q_root] = p_root
            self.sizes[p_root] += self.sizes[q_root]

    def connected(self, p: int, q: int) -> bool:
        assert p < self.num and q < self.num
        return self.get_root(p) == self.get_root(q)

    def connection_number(self) -> int:
        self.roots = np.array([self.get_root(i) for i in range(self.num)])
        return np.unique(self.roots).shape[0]

    def __str__(self) -> str:
        return str([(ind, v) for ind, v in enumerate(self.ids)])
