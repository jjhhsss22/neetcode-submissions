class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = dict()

        for number in nums:
            if number in hash:
                hash[number] += 1
            else:
                hash[number] = 1

        sorted_freq = sorted(hash, key = hash.get, reverse=True)

        return sorted_freq[:k]
            

        