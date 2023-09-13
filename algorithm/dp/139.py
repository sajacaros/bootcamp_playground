from functools import cache
from typing import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def wordSearch(s: str) -> bool:
            # dicts = {word:word[0] for word in wordDict}
            if s in wordDict:
                return True
            for word in wordDict:
                if len(s) < len(word):
                    print(f'word short, {s} : {word}')
                    continue
                if s[0:len(word)] == word:
                    if (len(s) == len(word)) or wordSearch(s[len(word):]):
                        return True
                    else:
                        continue
            return False
        return wordSearch(s)

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(Solution().wordBreak(s, wordDict))

s = "leetcode"
wordDict = ["leet","code"]
print(Solution().wordBreak(s, wordDict))
