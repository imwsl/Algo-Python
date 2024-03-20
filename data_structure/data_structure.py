# data_structure.py
#

# array
# linked list
# stack
# queue
# tree
# graph
# heap
# hash table
#

# linear data structure: array, linked list, stack, queue, hash table
# net data structure: graph
#
#

# array
# initial, insert, delete, traverse, find, extend
# 

# print array
#
def print_array(l: list):
    for i in range(len(l)):
        print(l[i])

# initial array
#
def init_array(n: int) -> list:
    return [0] * n


# insert array
# 
def insert_array(value: int, index: int, array: list):
    if index < 0 or index > len(array):
        print("out of array!")
        return
    
    temp_array = [0] * (len(array) + 1)
    