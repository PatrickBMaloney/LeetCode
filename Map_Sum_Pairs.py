# Implement the MapSum class:

# MapSum() Initializes the MapSum object.
# void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
# int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.
 

# Example 1:

# Input
# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
# Output
# [null, null, 3, null, 5]

# Explanation
# MapSum mapSum = new MapSum();
# mapSum.insert("apple", 3);  
# mapSum.sum("ap");           // return 3 (apple = 3)
# mapSum.insert("app", 2);    
# mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
 

# Constraints:

# 1 <= key.length, prefix.length <= 50
# key and prefix consist of only lowercase English letters.
# 1 <= val <= 1000
# At most 50 calls will be made to insert and sum.

class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.val = 0


class MapSum:
    head = TrieNode()
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        
    def insert(self, key: str, val: int) -> None:
        cur = self.head
        for char in key:
            if char in cur.children:
                cur = cur.children[char]
            else:
                cur.children[char] = TrieNode()
                cur = cur.children[char]
        cur.val = val

    def sum(self, prefix: str) -> int:
        cur = self.head
        for char in prefix:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return 0
        return self.recSum(cur)
        
    def recSum(self, node: TrieNode) -> int:
        sum = 0
        for key in node.children.keys():
            sum += self.recSum(node.children[key])
        return node.val + sum
        
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)