def reverse_list(nums):
    """
    Reverses the order of items in a list by mutating it.
        
    Arguments: 
        nums (list of ints): The list that the function will reverse.
        
    Returns:
        none
    """
    set_list = []
    set_index = 0
    for i in range(len(nums) - 1, -1, -1):
        set_list.append(None)
        set_list[set_index] = nums[i]
        set_index += 1
    for i in range(len(nums)):
        nums[i] = set_list[i]


#list_nums = [1, 2, 3, 4, 5]
#reverse_list(list_nums)
#print(list_nums)