import array
nums = array.array('i',[1,2,3,4,5,6,7])
print(nums[0])
print(nums[-1])

import array
nums = array.array('i',[10,20,30,40,50,60,70])
print(nums[2:5])

import array
nums = array.array('i',[1,2,3,4,5,6,7])
print(nums[-1:-3])

import array
nums = array.array('i',[1,2,3,4,5,6,7])
print(nums[::2])

nums = array.array('i',[5,10,15,20,25,30])
slice_array = array[:4]
total = 0
for num in slice_array:
    total += nums
print("slice  array:", slice_array)

import array
nums = array.array('i',[1,2,3,4,5,6,7])
print(nums[::-1])
