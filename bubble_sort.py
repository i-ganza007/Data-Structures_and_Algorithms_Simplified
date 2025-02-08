# The bubble sort is the basic starter sorting algorithm because it's possibly the easiest to understand .
# So we're going to go through it here 
# This algorithm uses boolean values to track the sorted values and if the sorted boolean value doesn't change , we break out of the loop 

def bubblesort(arr):
    length = len(arr) -1
    sort = False
    
    while not sort:
        sort = True
        for i in range(length):
            if arr[i] < arr[i+1]:
                sort = False
                arr[i],arr[i+1] = arr[i+1],arr[i]

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
