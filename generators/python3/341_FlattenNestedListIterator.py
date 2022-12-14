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
Ref: https://leetcode.com/problems/flatten-nested-list-iterator/solutions/80247/Python-Generators-solution/comments/164433/
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
