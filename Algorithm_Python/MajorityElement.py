class MajorityElement:
    def getMaroityElement(self, nums: list) -> int:
        majority = {}
        count = 0
        for num in nums:
            if num in majority:
                majority[num] += 1
            else:
                majority[num] = 1

        for value in majority.values():  # or index for i in range(len(majority))
            if value > count:           # majority[i]
                count = value

        return count


instance = MajorityElement()
print(instance.getMaroityElement([2, 2, 1, 1, 1, 2, 2]))
