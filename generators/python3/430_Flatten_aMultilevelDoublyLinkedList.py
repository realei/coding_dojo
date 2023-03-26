from typing import Generator


class Solution:
    def flatten(self, head: "Node") -> "Node":
        def preOrder(node: "Node") -> Generator["Node", None, None]:
            while node:
                n = node.next
                yield node
                yield from preOrder(node.child)
                node = n
        
        prev = None
        for node in preOrder(head):
            if prev:
                prev.next = node
                prev.child = None
            node.prev, prev = prev, node
            
        return head
