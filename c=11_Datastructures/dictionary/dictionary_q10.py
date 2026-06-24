# Combine two dicts, adding values for common keys. 


d1 = {"a": 5, "b": 3}
d2 = {"b": 4, "c": 2}

result = d1.copy()

for key, value in d2.items():
    result[key] = result.get(key, 0) + value

print(result)