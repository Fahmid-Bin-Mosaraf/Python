# Merged dictionary
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = dict1 | dict2
print(merged_dict)


# Update dictionary
dict3 = {'a': 1, 'b': 2}
dict4 = {'b': 3, 'c': 4}

dict3.update(dict4)

print(dict3)