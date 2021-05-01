

from typing import List, Tuple
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

    def get_root(self, ind: int) -> int:
        counter= 0
        while ind != self.ids[ind]:
            ind = self.ids[ind]
            counter += 1
        return ind, counter

    def union(self, p: int, q: int) -> None:

        assert p < self.num and q < self.num
        p_root, p_counter = self.get_root(p)
        q_root, q_counter  = self.get_root(q)
        if p_root == q_root: return None
        if p_counter < q_counter:
            self.ids[p_root] = q_root
        else:
            self.ids[q_root] = p_root

    def connected(self, p: int, q: int) -> bool:
        assert p < self.num and q < self.num
        return self.get_root[p] == self.get_root[q]

    def connection_number(self) -> int:
        roots = np.array([self.get_root(i) for i in range(self.num)])
        return np.unique(roots).shape[0]

    def __str__(self) -> str:
        return str([(id, v) for id, v in enumerate(self.ids)])
