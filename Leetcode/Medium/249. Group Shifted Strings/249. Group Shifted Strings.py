class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """

        bcd abc zab

        az az   z
        """

        def form_key(string):
            if len(string) == 1: return "a"
            key = []
            for i in range(1, len(string)):
                a, b = string[i - 1], string[i]
                key.append((ord(b) - ord(a)) % 26)
                
            return tuple(key)

        hash_map = {}

        for string in strings:
            key = form_key(string)
            if key not in hash_map:
                hash_map[key] = [string]
            else:
                hash_map[key].append(string)
        
        return list(hash_map.values())
