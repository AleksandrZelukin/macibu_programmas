def sortArray(self, nums: List[int]) -> List[int]:
    i_lower_bound , upper_bound = min(nums), max(nums)
    lower_bound = i_lower_bound
    if i_lower_bound < 0:
        lb = abs(i_lower_bound)
        nums = [item + lb for item in nums]
        lower_bound , upper_bound = min(nums), max(nums)
    
    counter_nums = [0]*(upper_bound-lower_bound+1)
    for item in nums:
        counter_nums[item-lower_bound] += 1
    pos = 0
    for idx, item in enumerate(counter_nums):
        num = idx + lower_bound
        for i in range(item):
            nums[pos] = num
            pos += 1
    if i_lower_bound < 0:
        lb = abs(i_lower_bound)
        nums = [item - lb for item in nums]
    return nums
