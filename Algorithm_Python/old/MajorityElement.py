class MajorityElement:
    def getMaroityElement(self, nums: list) -> int:
        majority = {}
        count = 0
        for num in nums:
            if num in majority:
                majority[num] += 1
            else:
                majority[num] = 1

            if majority[num] > len(nums) // 2:
                return num

        return None

    def getMaroityElement_divide_conquer(self, nums: list) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        front_half = self.getMaroityElement_divide_conquer(nums[:half])
        back_half = self.getMaroityElement_divide_conquer(nums[half:])

        return [back_half, front_half][nums.count(
            front_half) > len(nums) // 2]


instance = MajorityElement()
print(instance.getMaroityElement([2, 2, 1, 1, 1, 2, 2]))
print(instance.getMaroityElement_divide_conquer([2, 2, 1, 1, 1, 2, 2]))
