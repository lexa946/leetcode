from copy import copy
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 0: return []
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1, 1]]

        layers = [[1], [1, 1]]
        for i in range(2, numRows):
            layer_prev = copy(layers[i - 1])
            layer_new = [1]
            while layer_prev:
                last_item = layer_prev.pop()
                if layer_prev:
                    layer_new.append(last_item+layer_prev[-1])
                else:
                    layer_new.append(last_item)
            layers.append(layer_new)

        return layers


sol = Solution()
print(sol.generate(5))
