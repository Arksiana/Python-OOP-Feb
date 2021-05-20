# def first_n(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
#
#
# sum_first_n = sum(first_n(5))
# print(sum_first_n)
#
#


def values_gen(n):
    index = 0
    while index < n:
        yield index
        index += 1


gen = values_gen(5)
print(gen)
for x in gen:
    print(x)
