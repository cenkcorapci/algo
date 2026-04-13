from typing import List


def solve(nums: List[int], target: int) -> List[int]:
    seen = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index
    return []


def main() -> None:
    nums = [2, 7, 11, 15]
    target = 9
    print(solve(nums, target))


if __name__ == "__main__":
    main()

