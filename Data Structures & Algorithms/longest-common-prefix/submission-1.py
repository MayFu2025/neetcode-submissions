class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        match strs:
            case []:
                return ""
            case [single]:
                return single
            case [first, *rest]:
                a = self.longestCommonPrefix(rest)
                result = ""
                for i in range(min(len(first), len(a))):
                    print(i)
                    if first[i] != a[i]:
                        break
                    else:
                        result = result + first[i]
                return result
        