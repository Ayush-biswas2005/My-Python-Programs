#**Dictionary Merge**: Write a function that merges two dictionaries. If both dictionaries have the same key, sum their values.
a = {'a': 1, 'b': 2, 'c': 3}
b = {'b': 3, 'c': 4, 'd': 5}
for key in b:
    if key in a:
        a[key] += b[key]
    else:
        a[key] = b[key]
print(a)