class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        answer = []
        buckets = {}
        for i in range(len(groupSizes)):
            k = groupSizes[i]
            if k not in buckets:
                    buckets[k] = []
            buckets[k].append(i)
            if len(buckets[k]) == k: 
                answer.append(buckets[k])
                buckets[k] = []
        return answer


        
        
