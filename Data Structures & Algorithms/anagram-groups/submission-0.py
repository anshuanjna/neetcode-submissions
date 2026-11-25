class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hash map has key-value pairs 
        dict_ = {}
        for word in strs:
            key = "".join(sorted(word))

            if key not in dict_:
                dict_[key] = []

            dict_[key].append(word)
        
        return list(dict_.values())




        