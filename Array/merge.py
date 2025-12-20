class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1      # nums1 ichidagi oxirgi haqiqiy element
        j = n - 1      # nums2 ichidagi oxirgi element
        k = m + n - 1  # nums1 ning eng oxiri (bo‘sh joylar tomoni)

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
            



        
