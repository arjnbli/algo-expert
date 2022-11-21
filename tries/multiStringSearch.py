# O(b * s + n * s) time | O(n * s) space
# b is the length of the big string
# s is the length of the biggest string in the smallStrings array
# n is the number of strings in the smallStrings array
def multiStringSearch(bigString, smallStrings):
    # Write your code here.
    isContained = {smallString: False for smallString in smallStrings}
    trie = Trie(smallStrings)

    for i in range(len(bigString)):
        node = trie.root
        for j in range(i, len(bigString)):
            if trie.endSymbol in node:
                isContained[node[trie.endSymbol]] = True
            if bigString[j] not in node:
                break
            node = node[bigString[j]]
        if trie.endSymbol in node:
            isContained[node[trie.endSymbol]] = True

    return [isContained[smallString] for smallString in smallStrings]

class Trie:
    def __init__(self, array, endSymbol='*'):
        self.root = {}
        self.endSymbol = endSymbol
        self.buildTrieFrom(array)
    
    # O(n * s) time | O(n * s) space
    # n is the number of strings in the string array and s is
    # the length of the longest string in the string array
    def buildTrieFrom(self, stringArray):
        for string in stringArray:
            node = self.root
            for char in string:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node[self.endSymbol] = string
