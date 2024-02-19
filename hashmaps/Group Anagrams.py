from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map = {}
        result = []
        ##go through each of the words and check if its an anagram 
        anagram_map = defaultdict(list)
        for s in strs:
            ##going to use the sort method to compare each index with letters in ascending order
            sorted_s = tuple(sorted(s)) ## need to convert this to a tuple so that the data type is immutable
            anagram_map[sorted_s].append(s) ##at the key with sorted letters, append the word that matches
            ##then map on the values seperated by their keys
        for value in anagram_map.values():
            result.append(value) ##then append these results to the results array
        return result 
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        