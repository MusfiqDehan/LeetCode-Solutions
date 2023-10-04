class MyHashMap:

    def __init__(self):
        self.contents = []

    def put(self, key: int, value: int) -> None:
        found = False
        for c in self.contents:
            if c[0] == key:
                c[1] = value
                found = True
                break
        
        if not found:
            self.contents.append([key, value])

    def get(self, key: int) -> int:
        #print(self.contents)
        for c in self.contents:
            if c[0] == key:
                return c[1]
        return -1

    def remove(self, key: int) -> None:
        index = None
        for i in range(len(self.contents)):
            if self.contents[i][0] == key:
                index = i
                break
        
        if index is None:
            return None
        else:
            self.contents.pop(index)
            return None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)