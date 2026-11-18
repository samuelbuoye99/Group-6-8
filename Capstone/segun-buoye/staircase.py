def staircase(n):
    result = []

    def explore(path, nums, start):
        if sum(path) == n:
            result.append(path[:])
            return

        for i in range(start, len(nums)):
            if nums[i] + sum(path) > n:
                continue
            path.append(nums[i])
            explore(path, nums, i)
            path.pop()

    explore([], [1, 2, 3], 0)
    return result

print(staircase(4))