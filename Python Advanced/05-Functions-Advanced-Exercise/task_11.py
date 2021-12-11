def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        name = list(name)
        if name[0] in kwargs:
            arg = ''.join(name)
            result[arg] = kwargs[name[0]]
    return result


print(age_assignment("Peter", "George", G=26, P=19))
