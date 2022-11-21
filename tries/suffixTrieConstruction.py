class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = '*'
        self.buildSuffixTrieFrom(string)
    
    # O(n^2) time | O(n^2) space
    # n is the length of the string from which the suffix trie is constructed
    def buildSuffixTrieFrom(self, string):
        for i in range(len(string)):
            suffix = string[i:]
            node = self.root
            for char in suffix:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node[self.endSymbol] = True

    # O(m) time | O(1) space
    # m is the length of the string being checked
    def contains(self, string):
        node = self.root
        for char in string:
            if char not in node:
                return False
            node = node[char]
        return True if self.endSymbol in node else False
