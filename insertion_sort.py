def insertion_sort(list_a):
    for i in range(1,len(list_a)):
        values = list_a[i]
        while list_a[i-1] > values and i>0:
            list_a[i-1],list_a[i] = list_a[i],list_a[i-1]
            i = i-1
    return list_a