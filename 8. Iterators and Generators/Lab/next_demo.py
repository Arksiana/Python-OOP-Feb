ll = [1, 2, 3, 4, 5]

for x in ll:
    print(x)

print([[x + 1] for x in ll])
ll_iter_1 = iter(ll)
ll_iter_2 = iter(ll)
# print(ll_iter_1)
# print(next(ll_iter_1))
# print(next(ll_iter_1))
# print(next(ll_iter_1))
# print(next(ll_iter))
# print(next(ll_iter))
# print(next(ll_iter))

while True:
    try:
        print(next(ll_iter_1))
    except StopIteration:
        break


class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.end:
            raise StopIteration
        value = self.value
        self.value += 1
        return value


for x in custom_range(1, 10):
    print(x)