def binary_string(n):
    result = []
    def inner(path, nums):
        if len(path) == n:
            result.append("".join(path))
            return

        for num in nums:
            path.append(num)
            inner(path, nums)
            path.pop()

    inner([], "01")
    return result

print(binary_string(2))