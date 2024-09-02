from copy import copy
from typing import List


class Solution:
    def generate(self, rowIndex: int) -> List[List[int]]:


        if rowIndex == 0: return [[1]]
        if rowIndex == 1: return [[1], [1, 1]]

        layers = [[1], [1, 1]]
        for i in range(2, rowIndex+1):
            layer_prev = copy(layers[i - 1])
            layer_new = [1]
            while layer_prev:
                last_item = layer_prev.pop()
                if layer_prev:
                    layer_new.append(last_item+layer_prev[-1])
                else:
                    layer_new.append(last_item)
            layers.append(layer_new)

        return layers[rowIndex]


sol = Solution()
print(sol.generate(3))