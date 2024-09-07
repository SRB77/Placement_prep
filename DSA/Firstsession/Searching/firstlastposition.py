# https://my.newtonschool.co/playground/code/ot3kzhy3f6mf (first and last postion).
def searchRange(nums, target):
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        first_position = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first_position = mid
                right = mid - 1  # Look for a potential earlier occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return first_position

    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        last_position = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last_position = mid
                left = mid + 1  # Look for a potential later occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return last_position

    # Find the first and last positions of the target
    first = findFirst(nums, target)
    last = findLast(nums, target)

    return [first, last]

    