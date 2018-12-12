'''
Given an array of integers, return indices of the two numbers such that they add
up to a specific target.
You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

###time complexity O(n^2)
class Solution:
    def twoSum(self, num, target):
        tmp = {}
        for i in range(len(num)):
            print(i)
            if target - num[i] in tmp:
                return(tmp[target - num[i]], i)
            else:
                tmp[num[i]] = i;

if __name__ == '__main__':
    num = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(num,target))