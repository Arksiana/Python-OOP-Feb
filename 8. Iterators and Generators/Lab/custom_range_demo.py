class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self.iterator(self)

    def reverse(self):
        return self.iterator(self)

    class iterator:
        def __init__(self, custom_range_obj):
            self.custom_range_obj = custom_range_obj
            self.value = self.custom_range_obj.start

        def __iter__(self):
            return self

        def __next__(self):
            if self.value > self.custom_range_obj.end:
                raise StopIteration
            value = self.value
            self.value += 1
            return value


cr = custom_range(1, 10)

iter1 = iter(cr)
iter2 = iter(cr)
print(iter1)
for x in iter1:
    print(f'Iter1: {x}')

for x in iter2:
    print(f'Iter2: {x}')

for x in reversed(cr):
    print(x)
