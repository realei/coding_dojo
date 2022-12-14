# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

"""
Ref: 
Eng(Python generator):
https://leetcode.com/problems/flatten-nested-list-iterator/solutions/80247/Python-Generators-solution/comments/164433/

CN(DFS//stack):
https://leetcode.cn/problems/flatten-nested-list-iterator/solution/bian-ping-hua-qian-tao-lie-biao-die-dai-ipjzq/

* 嵌套的整型列表是一个树形结构，树上的叶子节点对应一个整数，非叶节点对应一个列表。

* 我们可以用一个栈来代替方法一中的递归过程。具体来说，用一个栈来维护深度优先搜索时，从根节点到当前节点路径上的所有节点。由于非叶节点对应的是一个列表，我们在栈中存储的是指向列表当前遍历的元素的指针（下标）。

Q1: what is `.isInteger()`, `.getInteger()` & `.getList()`?
    Ans: please check above defination of NestedInteger, the input type is `nestedList: [NestedInteger]`
"""
from typing import Generator

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flattenGenerator(nestedList: [NestedInteger]) -> Generator[int, int, int]:

            for val in nestedList:
                # Each element is either an integer or a list
                if val.isInteger(): # scenario 1:element is an integer
                    yield val.getInteger()
                else: # scenario 2: element is an integer
                    for v in flattenGenerator(val.getList()): 
                        yield v

        self.generator = flattenGenerator(nestedList)
    
    def next(self) -> int:

        return self.value
        
    
    def hasNext(self) -> bool:

        try:
            self.value = next(self.generator)
            return True
        except StopIteration:
            return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
