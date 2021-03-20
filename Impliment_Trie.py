# Trie (we pronounce "try") or prefix tree is a tree data structure used to retrieve a key in a strings dataset. There are various applications of this very efficient data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() initializes the trie object.
# void insert(String word) inserts the string word to the trie.
# boolean search(String word) returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
 

# Constraints:

# 1 <= word.length, prefix.length <= 2000
# word and prefix consist of lowercase English letters.
# At most 3 * 104 calls will be made to insert, search, and startsWith.

class TrieNode:
    
    def __init__(self, val=0, isWord=False):
        self.val = val
        self.isWord = isWord
        self.children = {}

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = self.head
        i = 0
        while i < len(word) and word[i] in cur.children:
            cur = cur.children[word[i]]
            i += 1
        while i < len(word):
            cur.children[word[i]] = TrieNode(word[i])
            cur = cur.children[word[i]]
            i += 1
            
        cur.isWord = True
        
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        
        cur = self.head
        for char in word:
            if char not in cur.children:
                return False
            else:
                cur = cur.children[char]
                
        return cur.isWord
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
        cur = self.head
        
        for i in range(len(prefix)):
            if prefix[i] in cur.children:
                cur = cur.children[prefix[i]]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)