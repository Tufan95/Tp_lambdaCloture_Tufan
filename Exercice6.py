def filterMap(filter_func, map_func, lst):
    return [map_func(x) for x in lst if filter_func(x)]

words = ["hello", "", "world", "python", "", "lambda"]
result = filterMap(lambda x: x != "", lambda x:
x.upper(), words)

print(result)