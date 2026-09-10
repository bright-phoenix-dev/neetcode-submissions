from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt=Counter(nums)
        most_freq_list=cnt.most_common()
        return [item[0] for item in most_freq_list[:k]]