#!/usr/bin/env python3

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        SUMS = {}

        def dig(node, level):
            try:
                SUMS[level] += node.val
            except KeyError:
                SUMS[level] = node.val

            level += 1

            if node.left:
                dig(node.left, level)
            if node.right:
                dig(node.right, level)

        dig(root, 0)

        if k > len(SUMS):
            return -1

        return sorted(list(SUMS.values()), reverse=True)[k-1]

