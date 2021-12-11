# class Iterator:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.value = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.value > self.end:
#             raise StopIteration
#
#         value = self.value
#         self.value += 1
#         return value
#
#
# iters = Iterator(1, 20)
# for i in iters:
#     print(i)

# def values(n):
#     index = 0
#     while index < n:
#         yield index
#         index += 1
#
#
# gen = values(5)
# for i in gen:
#     print(i)

# class vowels():
#     vowels = {
#         'a', 'b', 'c'
#     }
#
#     def __init__(self, text):
#         self.text = text
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.text):
#             raise StopIteration
#         ch = self.text[self.index]
#         self.index += 1
#         if ch not in self.vowels:
#             return self.__next__()
#
#         return ch


def vowels(text):
    vowels = {
        'a', 'b', 'c'
    }

    for ch in text:
        if ch in vowels:
            return ch


text = vowels("saaad;gjs;ldgjklsdjg;sldbbbb")
for t in text:
    print(t)
