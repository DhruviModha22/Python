dict_list = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 30}]
sorted_dict_list = sorted(dict_list, key=lambda x: x['age'])
print(sorted_dict_list)