nums = [1,2,3,4,5]

# def reverse(nums):
#     list.reverse(nums)
#     print(nums)
# reverse(nums)

def check(nums):
    start = 0
    end = len(nums)-1
    
    while start<=end:
        nums[start], nums[end] = nums[end], nums[start]
        start+=1
        end-=1
    print(nums)
check(nums)        