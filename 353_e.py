class TrieTree:
    class Node:
        def __init__(self):
            self.children = [-1] * 26
            self.through = 0
    
    def __init__(self):
        self.nodes = [self.Node()]
        self.count = 0
    
    def add_word(self, word):
        node = self.nodes[0]
        for char in word:
            char = ord(char) - ord("a")
            if node.children[char] == -1:
                node.children[char] = len(self.nodes)
                self.nodes.append(self.Node())
            k = node.children[char]
            node = self.nodes[k]
            self.count += node.through
            node.through += 1
    
    def check(self):
        for node in self.nodes:
            print(node.children)

Trie = TrieTree()

N = int(input())
S = list(map(str, input().split()))
for i in range(N):
    Trie.add_word(S[i])

print(Trie.count)