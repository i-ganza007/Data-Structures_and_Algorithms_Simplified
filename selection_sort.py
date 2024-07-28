def selection_sort(list_a):
    for i in range(len(list_a)):
        # This algorithm is done by assigning a minimum value as you go along the list 
        # The first item is by default the minimum value and if a lesser value than the first appears , it's assigned the new minimum value
        # The switch happens later 
        min_value = i
        for j in range(i+1,len(list_a)):
            if list_a[min_value] > list_a[j]:
                min_value = j
        if min_value != i:
            list_a[min_value],list_a[j] = list_a[j],list_a[min_value]
    return list_a