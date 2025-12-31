class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for k in list(set(nums1)):
            if k in list(set(nums2)):
                result.append(k)

        return result
        
