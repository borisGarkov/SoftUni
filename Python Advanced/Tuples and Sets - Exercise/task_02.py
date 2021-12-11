elements = [int(el) for el in input().split()]
n, m = elements
n_set = set()
m_set = set()

for _ in range(n):
    line = input()
    n_set.add(line)

for _ in range(m):
    line = input()
    m_set.add(line)

print("\n".join(n_set & m_set))
