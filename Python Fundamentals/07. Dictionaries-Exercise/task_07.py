n_pairs = int(input())
registry = {}

for _ in range(n_pairs):
    name = input()
    grade = float(input())

    if name not in registry:
        registry[name] = [grade]
    else:
        registry[name].append(grade)

sorted_registry = {}
for name, grade in registry.items():
    average_grade = sum(grade) / len(grade)
    sorted_registry[name] = average_grade

sorted_registry = {name: grade for name, grade in sorted_registry.items() if grade >= 4.5}

sorted_registry = dict(sorted(sorted_registry.items(), key=lambda x: x[1], reverse=True))
for name, grade in sorted_registry.items():
    print(f"{name} -> {grade:.2f}")
