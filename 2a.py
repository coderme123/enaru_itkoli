def insert_sorted(sorted_list, element):

    index = 0
    while index < len(sorted_list) and sorted_list[index] < element:
        index += 1

    
    sorted_list.insert(index, element)

    return sorted_list


sorted_list = [1, 3, 5, 7, 9]
element = 6
print("Original sorted list:", sorted_list)
print("Element to insert:", element)
print("Sorted list after insertion:", insert_sorted(sorted_list, element))
