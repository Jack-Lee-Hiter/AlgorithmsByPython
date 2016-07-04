# 用Python实现hash表
# hash的查找操作时间复杂度O(1)
# hash每个位置被称为slot槽。可以使用list实现hash,每个slot对应一个key,存放元素

# 按照正常的字母在ASCII中的顺序mod tablesize构造hash
def hash(astring, tablesize):
    sum = 0
    for pos in astring:
        sum = sum + ord(pos)

    return sum%tablesize

print(hash('cat', 11))  # cat在hash中的位置,hash table长度11

# 改进hash, 让每一位的字母乘以该字母在字串中的位置然后mod
def hash2(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum += (pos+1) * ord(astring[pos])
    return sum%tablesize

print(hash2('cat', 11))

# 冲突解决:分离链--冲突位置排成一个链; linear probing发生冲突去下一个位置

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, self.size)

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data         # 替换相同索引对应的项目
            else:
                if None not in self.slots and key not in self.slots:
                    # 判断hash是否已经满了, 必须添加key not in self.slots, 否则修改已有hash值会直接返回-1
                    print('sorry, there is not enough slots for you!')
                    return -1
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key%size

    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

H = HashTable()
H[54] = 'cat'
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"
print(H[20])
print(H.slots)
print(H.data)
print(H[99])
H[21] = "elephant"
H[22] = "sheep"
H[23] = "fish"
print(H.data)
H[20] = 'monkey'
print(H.data)