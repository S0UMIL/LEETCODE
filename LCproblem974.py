#my wrong answer:-
        hashmap={0:1}
        curr_sum=0
        count=0
        for num in nums:
            curr_sum += num
            if curr_sum%k in hashmap:
                count+=hashmap[curr_sum%k]
            hashmap[count]=hashmap.get(count,0)+1#adding the wronga thing inside the hashmap suppsoed to add the remainder or the condition in this case . the following conditions below were to lineup with the cases mentioned in the question but failed in other cases
        if count==0:
            return 0
        else:
            return count+1


#2nd attempt accepted:-

        hashmap = {0: 1}
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num
            remainder = curr_sum % k 

            if remainder in hashmap:
                count += hashmap[remainder]

            hashmap[remainder] = hashmap.get(remainder, 0) + 1# adding the remainder condtion in the hashmap rather than count in my previous mistake

        return count


