import sys
sys.setrecursionlimit(10**6)

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

class State:
    def __init__(self):
        self.next = {}
        self.link = -1
        self.length = 0

class suffixAutomaton:
    def __init__(self):
        self.states = [State()]
        self.last = 0
    
    def extend(self, c):
        st = self.states

        cur = len(st)
        st.append(State())
        st[cur].length = st[self.last].length + 1

        p = self.last

        # ---(1)遷移を張る---
        while p != -1 and c not in st[p].next:
            st[p].next[c] = cur
            p = st[p].link

        if p == -1:
            st[cur].link = 0
        else:
            q = st[p].next[c]
            if st[p].length + 1 == st[q].length:
                st[cur].link = q
            else:
                # ---(2)clone---
                clone = len(st)
                st.append(State())
                st[clone].next = st[q].next.copy()
                st[clone].length = st[p].length + 1
                st[clone].link = st[q].link
            
                # 既存遷移を書き換える
                while p != -1 and st[p].next[c] == q:
                    st[p].next[c] = clone
                    p = st[p].link
                
                st[q].link = clone
                st[cur].link = clone
        
        self.last = cur
    
    def build(self, s):
        for c in s:
            self.extend(c)
    
    def is_substring(self, t):
        state = 0
        st = self.states
        for c in t:
            if c not in st[state].next:
                return False
            state = st[state].next[c]
        return True

# sam = suffixAutomaton()
# sam.build("banana")

# print(len(sam.states))
# print(sam.is_substring("nan"))
# print(sam.is_substring("abc"))

def compute_win_states(sam):
    n = len(sam.states)
    win = [None] * n 

    def dfs(v):
        if win[v] is not None:
            return win[v]
        
        # 遷移先がない場合、負け
        if not sam.states[v].next:
            win[v] = False # type: ignore
            return False
        
        for _, u in sam.states[v].next.items():
            if not dfs(u):
                win[v] = True # type: ignore
                return True
                # 遷移先に負けがある場合、勝ち
        win[v] = False # type: ignore
        return False
        # 遷移先がすべて勝ちの場合、負け
    
    for v in range(n):
        dfs(v)
    return win

T = int(input())
for _ in range(T):
    S = str(input())
    sam = suffixAutomaton()
    sam.build(S)

    win = compute_win_states(sam)

    if win[0]:
        print("Alice")
    else:
        print("Bob")