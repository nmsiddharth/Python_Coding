nums = [0,1,0,3,12]
n = len(nums)
write_pointer = 0    # Non-zero pointer


for read_pointer in range(len(nums)):
    if nums[read_pointer]!=0:
        nums[write_pointer] = nums[read_pointer]
        write_pointer+=1
        
for i in range(write_pointer,n) :
    nums[i]=0
    

print(nums)           
