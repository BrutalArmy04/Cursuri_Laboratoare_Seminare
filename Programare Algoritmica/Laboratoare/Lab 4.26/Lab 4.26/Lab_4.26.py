nums = [2, 3, 1]
for i in range (1, len(nums)):
    if nums[i-1]<nums[i]:
        break
else:
    print(sorted(nums))
start = len(nums) - 1
i = len(nums) - 2
while True:
    if nums[start]>nums[i]:
        nums[i], nums[start] = nums[start], nums[i]
        break
    i -= 1
    if i == 0:
        nums[i], nums[len(nums)-1] = nums[len(nums)-1], nums[i]
print(nums)

    

    

