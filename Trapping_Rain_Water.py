'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map 
where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''

def trap(height):
    n = len(height)
    amount = 0
    # Monotonic Stack Approach TC O(n), SC O(n)
    '''
    left_max = [0]*n
    right_max = [0]*n

    left_max[0] = height[0]
    for i in range(1,n):
        left_max[i] = max(left_max[i-1],height[i])


    right_max[n-1] = height[n-1]
    for i in range(n-2,-1,-1):
        right_max[i] = max(right_max[i+1],height[i])

    for i in range(n):
        amount += min(left_max[i],right_max[i]) - height[i]
    
    return amount
    '''

    # Two Pointers Approach TC O(n), SC O(1)
    left = 0
    right = n-1
    left_max = -1
    right_max = -1
    while(left < right):
        left_max = max(height[left],left_max)
        right_max = max(height[right],right_max)
        if left_max < right_max:
            amount += left_max - height[left]
            left += 1
        else:
            amount += right_max - height[right]
            right -= 1
    return amount

# Sample Input
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height = height))