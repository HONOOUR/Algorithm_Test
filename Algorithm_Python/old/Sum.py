# sort
# first num from range(list)
# second = start++
# third = end--
# sum = first + second + third
# if (sum < target) -> second++
# if (sum > target) -> third--
class sum:
    def threeSum(self, nums, target: int):
        results = [[]]
        nums.sort()

        for first in range(len(nums)-2):
            if first > 0 and nums[first] == nums[first-1]:
                continue

            second = first+1
            third = len(nums)-1
            while second < third:
                sum = nums[first] + nums[second] + nums[third]
                if sum < target:
                    second += 1
                elif sum > target:
                    third -= 1
                else:
                    results.append([nums[first], nums[second], nums[third]])

                    while second < third and nums[second] == nums[second+1]:
                        second += 1
                    while second < third and nums[third] == nums[third-1]:
                        third -= 1

                    second += 1
                    third -= 1

        return results


instance = sum()
answer = instance.threeSum([-3, -4, -5, -1, -1, -1, 0,
                            0, 0, 1, 1, 1, 3, 3, 5, 4, 4], 0)
