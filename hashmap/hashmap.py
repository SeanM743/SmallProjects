
class Element(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value


class HashMap(object):
    def __init__(self,size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_fun(self,key):
        return key % self.size

    def set(self,key,value):
        
        hash_val = self._hash_fun(key)
        for item in self.table[hash_val]:
            if item.key == key:
                return item.value
        self.table[hash_val].append(Element(key,value))
    
    def get(self, key):
        hindex = self._hash_fun(key)

        for item in self.table[hindex]:
            if item.key == key:
                return item.value
        raise KeyError('Key not found')

    def remove(self,key):
        hindex = self._hash_fun(key)
        for idx,item in enumerate(self.table[hindex]):
            if item.key == key:
                del self.table[hindex][idx]
                return
        raise KeyError('Key not found')
    
    def print_hashmap(self):
        for items in self.table:
            for elements in items:
                print(elements.key,elements.value)

e1 = Element(1,15)
e2 = Element(2,11)
e3 = Element(3,99)

hmap = HashMap(10)

hmap.set(e1.key,e1.value)
hmap.set(e2.key,e2.value)
hmap.set(e3.key,e3.value)

hmap.print_hashmap()

print(hmap.get(2))
hmap.remove(2)
hmap.print_hashmap()
hmap.remove(19)