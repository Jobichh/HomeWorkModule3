
def calculate_structure_sum(data):
    total_item = 0
    
    def calculate_sum(item):
        nonlocal total_item
        
        if  isinstance(item, (int, float)):
            total_item += item
            
        elif  isinstance(item, (str)):
            total_item += len(item)
            
        elif isinstance(item, (list, tuple, set)):
            for sub_item in item:
                calculate_sum(sub_item)
                
        elif isinstance(item, (dict)):
            for key, value in item.items():
                calculate_sum(key)
                calculate_sum(value)
                
    calculate_sum(data)
    return total_item


data_structure = [

  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])

]


result = calculate_structure_sum(data_structure)
print(result)