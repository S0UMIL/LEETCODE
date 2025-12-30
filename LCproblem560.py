hashmap={0:1}#first condition to make sure subarrays before the curr_sum-k condition also are included which add up to the sum.
count=0
currn_sum=0
for num in nums:
    currn_sum+=num#updating current sum as going from left to right
    if currn_sum-k in hashmap:#2nd conditon checks if there is any other subarray which fulfills the condition of sum , by simply using the currentsum - k = value , this value if matches to any index value , we can be sure that another subarray exists.
        count+=hashmap[currn_sum-k]
    hashmap[currn_sum]=hashmap.get(currn_sum,0)+1
return count
