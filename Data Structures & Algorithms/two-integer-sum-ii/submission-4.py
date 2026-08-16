from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            s = i + 1
            e = len(numbers) - 1
            search = target - numbers[i]

            while s <= e:
                mid = s + (e - s) // 2
                if numbers[mid] == search:
                    return [i + 1, mid + 1]
                elif numbers[mid] < search:
                    s = mid + 1
                else:
                    e = mid - 1
        return []  # fallback, in case no result is found (not expected in this problem)

