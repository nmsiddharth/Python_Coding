height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

def check(height):
    left = 0
    right = len(height)-1
    leftmax = height[left]   # leftmax = 0  ---> left+=1 at last
    rightmax = height[right] # rightmax = 0  ---> right+=1 at last
    res = 0
    
    while left < right:
        if leftmax < rightmax:
            left+=1
            leftmax = max(leftmax,height[left])
            res += leftmax - height[left]
        #   left += 1  ---> when leftmax = 0
        else:
            right -=1
            rightmax = max(rightmax,height[right])
            res+=rightmax - height[right]
        #   right -=1  ---> when rightmax = 0
    print(res)
                           
check(height)                           