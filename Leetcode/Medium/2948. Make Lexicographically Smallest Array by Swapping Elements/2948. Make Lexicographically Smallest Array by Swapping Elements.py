class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        """
        swap smaller number to the front always
        only swap when abs diff between 2 nums <= limit

        every number -> swap with the smallest number on the right and this number must be less than current number
        """

        num_to_group = defaultdict(int)
        groups = defaultdict(deque)

        sorted_nums = sorted(nums)
        group_idx = 0
        n = len(nums)

        for i in range(n):
            if i == 0:
                groups[group_idx].append(sorted_nums[i])
            else:
                if sorted_nums[i] - sorted_nums[i - 1] > limit:
                    group_idx += 1
                groups[group_idx].append(sorted_nums[i])
            num_to_group[sorted_nums[i]] = group_idx

        res = []
        for i in range(n):
            curr_group = groups[num_to_group[nums[i]]]
            res.append(curr_group.popleft())
        return res
                    