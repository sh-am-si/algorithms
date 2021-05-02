import numpy as np

from connectivity_problem.quick_find import QuickFindUF
import connectivity_problem.quick_union
from connectivity_problem.quick_union import QuickUnionUF
from connectivity_problem.compressed_quick_union import CompressedQuickUnionUF
from connectivity_problem.weighted_quick_union import WeightedQuickUnionUF

class PercolationGraphic:

    def __init__(self, num, p) -> None:
        self.num = num
        self.p = p
        self.array = np.zeros(shape=(self.num * self.num, ), dtype=bool)
        self.array[np.random.choice(np.arange(self.num**2), int(self.p * self.num **2), replace=False)] = True
        self.array = self.array.reshape(self.num, self.num)

    def percolates(self) -> bool:

        def next_step(raw1, raw2):
            i = 0
            result = np.zeros(self.num, dtype=bool)
            while i < self.num:
                if raw2[i]:
                    j = i + 1
                    while j < self.num:
                        if not raw2[j]:
                            break
                        j += 1

                    if np.sum(raw1[i:j]):
                        result[i:j] = True
                    i = j + 1
                else:
                    i += 1
            return result

        temp = next_step(self.array[0,:], self.array[1,:])
        # print(1, ' -- ', temp.astype(int))
        i = 2
        while i< self.num:
            if not np.sum(temp):
                break
            temp = next_step(temp, self.array[i,:])
            # print(i, ' -- ',temp.astype(int))
            i += 1
        
        return i == self.num


class Percolation:

    def __init__(self, num, none_zero_num=0) -> None:
        self.num = num
        self.none_zero_num = none_zero_num
        self.p = self.none_zero_num / self.num ** 2

        self.array = np.zeros(shape=(self.num * self.num, ), dtype=bool)
        self.array[np.random.choice(np.arange(self.num**2), self.none_zero_num, replace=False)] = True
        self.array = self.array.reshape(self.num, self.num)


    def percolates(self, alg) -> bool:
        
        # assert isinstance(alg, connectivity_problem.quick_union.QuickUnionUF), f'alg {alg} type {type(alg)}'

        get_index = lambda i, j : i * self.num + j
        algorithm = alg(self.num ** 2 + 2)

        for i in range(self.num-1):
            for j in range(self.num-1):
                if self.array[i,j]:
                    if self.array[i, j+1]:
                        algorithm.union(get_index(i, j), get_index(i, j + 1))
                    if self.array[i + 1, j]:
                        algorithm.union(get_index(i + 1, j), get_index(i, j))

        if self.array[self.num - 1, self.num - 1] and self.array[self.num - 2, self.num -1] :
            algorithm.union(get_index(self.num - 1, self.num - 1), get_index(self.num - 2, self.num - 1))

        for j in range(self.num):
            if self.array[0, j]:
                algorithm.union(get_index(0, j), self.num ** 2)
            if self.array[self.num - 1, j]:
                algorithm.union(get_index(self.num - 1, j), self.num ** 2 + 1)

        return algorithm.connected(self.num ** 2, self.num ** 2 + 1)