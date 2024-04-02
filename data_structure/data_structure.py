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

from enum import Enum

ErrorType = Enum('ErrorType', [
    'OUT_OF_BOUNDARY'
])


# print array
#
def print_array(array: list):
    outline = ""
    for i in range(len(array)):
        if i < len(array) - 1:
            outline += str(array[i]) + ","
        else:
            outline += str(array[i])

    print(outline)


# print errors
#
def print_error(error: ErrorType):
    if error == ErrorType.OUT_OF_BOUNDARY:
        print("out of boundary!!")
    else:
        print("unknown error!!")


# check boundary
#
def is_out_of_boundary(index: int, array: list) -> bool:
    if index < 0 or index >= len(array):
        print_error(ErrorType.OUT_OF_BOUNDARY)
        return True
    return False


# initial array
#
def init_array(n: int) -> list:
    return [0] * n


# insert array
def insert_array(value: int, index: int, array: list) -> list:
    if is_out_of_boundary(index, array):
        return []
    temp_array = init_array(1 + len(array))

    for i in range(len(array)):
        temp_array[i] = array[i]
    i = len(array)

    while i > index:
        temp_array[i] = temp_array[i-1]
        i = i - 1

    temp_array[index] = value

    return temp_array


# delete
#

def delete_array(index: int, array: int) -> list:

    if is_out_of_boundary(index, array):
        return []

    temp_array = init_array(len(array) - 1)
    if len(temp_array) == 0:
        return temp_array

    for i in range(len(array)):
        if i < index:
            temp_array[i] = array[i]
        else:
            temp_array[i-1] = array[i]

    return temp_array


# test

arr = init_array(5)
for i in range(len(arr)):
    arr[i] = i

print_array(insert_array(9, 1, arr))

print_array(insert_array(-1, 4, arr))

arr1 = init_array(1)
arr1[0] = 8

print_array(insert_array(10, 0, arr1))

print_array(delete_array(0, arr1))
