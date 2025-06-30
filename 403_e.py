class TrieTree:
    class Node:
        def __init__(self):
            self.child = [-1] * 26
            self.finish = False
            self.word_set = set()
    
    def __init__(self):
        self.nodes = [self.Node()]
        self.Z = set()
    
    def add_prefix(self, prefix):
        k = 0
        for char in prefix:
            char_ind = ord(char) - ord("a")
            node = self.nodes[k]
            if node.child[char_ind] == -1:
                node.child[char_ind] = len(self.nodes)
                self.nodes.append(self.Node())
            k = node.child[char_ind]
        
        node = self.nodes[k]
        node.finish = True
        self.Z |= node.word_set
        node.word_set.clear()
    
    def add_word(self, word, i):
        k = 0
        for char in word:
            char_ind = ord(char) - ord("a")
            node = self.nodes[k]
            if node.child[char_ind] == -1:
                node.child[char_ind] = len(self.nodes)
                self.nodes.append(self.Node())
            node.word_set.add(i)
            if node.finish:
                self.Z.add(i)
            k = node.child[char_ind]
        
        node = self.nodes[k]
        node.word_set.add(i)
        if node.finish:
            self.Z.add(i)

Q = int(input())
trie = TrieTree()
Y_count = 0

for i in range(Q):
    T, S = map(str, input().split())
    if T == "1":
        trie.add_prefix(S)
    else:
        trie.add_word(S, i)
        Y_count += 1
    print(Y_count - len(trie.Z))