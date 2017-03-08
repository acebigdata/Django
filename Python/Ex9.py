import ipdb
ipdb.set_trace()
def arrayCheck(nums):
    for num in set([1,2,3]):
        if num not in nums:
            return False
        else:
            return True
