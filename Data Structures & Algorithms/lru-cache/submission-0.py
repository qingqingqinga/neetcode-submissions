
        
class Node:
    def __init__(self,key,val):
        self.key, self.val = key, val
        self.prev, self.next = None, None
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {} # map the key to the node
        
        # create the right and left nodes   left = LRU
        self.left,self.right = Node(0,0),Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self,node):
        prev, nxt = node.prev,node.next
        prev.next,nxt.prev = nxt, prev                #不懂为什么这里不用self

    # insert from the right
    def insert(self,node):      #不懂为什么不用self 以及 nxt = self.right 你总没想到
        prev,nxt = self.right.prev,self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt
        
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = Node(key,value)
            self.insert(self.cache[key])
        else:
            if len(self.cache) >= self.cap: #易错
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key] #看不懂
            new_node = Node(key, value) #为什么要换行
            self.cache[key] = new_node
            self.insert(new_node)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)