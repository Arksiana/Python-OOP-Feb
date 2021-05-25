# Linear approaching implementation of a hashing

class HashTable:
    """
    Hashable represent a custom dictionary implementation
    where we use two private lists to achieve storing and hashing of
    key-value pairs functionality.
    """

    def __init__(self):
        self.max_capacity = 4
        self.__keys = [None] * self.max_capacity
        self.__values = [None] * self.max_capacity

    def __getitem__(self, key):
        index = self.__keys.index(key)
        return self.__values[index]

    def __setitem__(self, key, value):
        index = self.hash(key)
        self.__keys[index] = key
        self.__values[index] = value

    def __len__(self):
        return len(self.__keys)

    def get(self, key):
        return key

    def check_available_index(self, index):
        """
        Checks there is empty slot on this index
        if not implements the linear approach when there is a
        collision between two hash indexes and returns the next available index.

        :param index: int
        :return: int -> next/current available index
        """
        if index == len(self.__keys):
            self.check_available_index(0)
        if self.__keys[index] is None:
            return index
        return self.check_available_index(index + 1)

    def hash(self, key):
        index = sum([ord(char) for char in key]) % self.max_capacity
        available_index = self.check_available_index(index)
        return available_index


table = HashTable()

table["name"] = "Peter"
table["age"] = 25

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))
