class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one = 0,0
        res = 0
        diff_index = {} #diff -> index => count[1]=count[0] -> index

        for index,value in enumerate(nums):
            if value == 0:
                zero += 1
            else:
                one += 1
            
            if (one-zero) not in diff_index:
                diff_index[one-zero] = index
            
            if one == zero:
                res = one+zero
            else:
                new_index = diff_index[one-zero]
                res = max(res,index-new_index)
        return res

        # #111000
        # How to know to shrink window or increase? Not possible so that approach wont' hold
        # Not every result would start at beginning
        # 11100 -> here the result would be 1100 len(1100) Answer 4


        # We will find the position of the first one and then verify count[1] == count[0]

        # map each index to pair(count[0], count[1])
        # use difference between counts for lookup


'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        numsSum = []
        hashMap = {0:0,1:0} #key,value pair with key = number, value 
        sum = 0
        for num in nums:
            sum+=num
            numsSum.append(sum)
            if sum not in hashmap:
                hashmap[sum] = 1
            else: 
                hashmap[sum] = hashmap.get(sum)+1

            if  
'''


        