class TrieNode:
    def __init__(self):
        self.children = {}
        self.Word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.Word = True
        
    def search(self, word: str) -> bool:
        def dfs(j, root): #递归传入的起始位置，表示从 word 的哪个字符开始搜索
            cur = root
            for i in range(j, len(word)): #前面的搜过了 所以从j开始搜索
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.Word

        return dfs(0, self.root)
         
