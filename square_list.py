def square_list(nums):
    """
    Squares all contents of a list and mutates it with the new values.
        
    Arguments: 
        nums (list of ints): The list of integers that the function will modify.
        
    Returns:
        none
    """
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


#list_of_nums = [0, 1, 2, 3, 4, 5, 6]
#square_list(list_of_nums)
#print(list_of_nums)