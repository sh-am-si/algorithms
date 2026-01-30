import numpy as np


class QuickFindUF:
    def __init__(self, num: int) -> None:
        self.num = num
        self.ids = np.arange(self.num, dtype=np.int)

    def union(self, p: int, q: int) -> None:
        assert p < self.num and q < self.num
        p_id = self.ids[p]
        q_id = self.ids[q]
        self.ids[self.ids == p_id] = q_id

    def connected(self, p: int, q: int) -> bool:
        assert p < self.num and q < self.num
        return self.ids[p] == self.ids[q]

    def connection_number(self) -> int:
        return np.unique(self.ids).shape[0]

    def __str__(self) -> str:
        return str([(ind, v) for ind, v in enumerate(self.ids)])
