class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}#hashmap
        for num in nums:#adding frequencies of number in the hashmap
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        buckets=[[] for _ in range(len(nums)+1)]#creating buckets (bucket sort) ie list of lists
        for num,count in freq.items():
            buckets[count].append(num)
        res=[]
        for num, count in range(len(buckets)-1,0,-1):# going from high freq to low freq since we require highest freq either ways
            for num in bucket[count]:#adding numbers into the res list until we have k
                res.append(num)
                if len(res)==k:
                    return res
                
        
