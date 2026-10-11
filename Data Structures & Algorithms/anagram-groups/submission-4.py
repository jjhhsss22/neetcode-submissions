class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None:
            return []

        hash_set = dict()
        
        for j, string in enumerate(strs):
            key = [0] * 26

            for char in string:
                key[ord(char) - ord('a')] += 1

            key_tuple = tuple(key)

            if key_tuple in hash_set:
                hash_set[key_tuple].append(j)
            else:
                hash_set[key_tuple] = [j]

        answer = []

        for item in hash_set.values():
            temp = []

            for idx in item:
                temp.append(strs[idx])

            answer.append(temp)

        return answer

                