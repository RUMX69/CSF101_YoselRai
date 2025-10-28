nums = [1, 2, 2, 1]

def containsDuplicate(nums):
    seen = set()
    for num in nums:
        
        if num in seen:
            return True
        seen.add(num)
    return False

print(containsDuplicate(nums))


        
    