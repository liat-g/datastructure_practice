from collections import defaultdict
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        check = defaultdict(list)
        final = []
        for i in ransomNote:
            ## create hashmap with letters from magazine
            check[i].append(i)
            # print check
        for letter in magazine:
            if check[letter]:
                final.append(letter)
        print final 
        word = ''.join(final)

        if sorted(word) == sorted(ransomNote):
            return True
            

            
        
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        