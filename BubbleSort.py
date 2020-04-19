nums = [2,3,4,6,7,1,36,7,9,1,3]

def sort(nums):
    for i in range(len(nums)-1,0,-1):  #reverse order
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j]= nums[j+1]
                nums[j+1] = temp


sort(nums)
print(nums)
