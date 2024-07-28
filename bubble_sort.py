# The bubble sort is the basic starter sorting algorithm because it's possibly the easiest to understand .
# So we're going to go through it here 
# This algorithm uses boolean values to track the sorted values and if the sorted boolean value doesn't change , we break out of the loop 

def bubble_sort(list_a):
    for i in range(len(list_a)):
        tracker = False
        # We created this to help track if they're any changes . If it doesn't make any sense , don't worry because it'll make sense later in the program ]
        for j in range(len(list_a)-i-1):
            # So what this range(len(list_a)-i-1) does , is shorten the length of the portion that needs to be sorted .
            # After the first iteration , the biggest value becomes the last value
            if list_a[j] > list_a[j+1]:
                list_a[j],list_a[j+1] = list_a[j+1],list_a[j]
                tracker = True
            if not tracker:
                break
    return list_a 

    """
    e.g [2,1,4,8,7,10]
    FIRST ITERATION
    The outer loop starts at 2 
    In the inner loop , it's range(6-0-1) = range(5) , So basically there're gonna be 5 switches 
    With 0 and 1 indexes , 1 and 2 indexes , 2 and 3 indexes , 3 and 4 indexes , 4 and 5 indexes
    With the end of the first iteration , [1,2,4,7,8,10]
    The tracker becomes true and on to the next iteration !!!

    SECOND ITERATION

    Since there's nothing to compare , the tracker which was true becomes false due to no switches 
    And then the loop breaks out and we return the list 


    """