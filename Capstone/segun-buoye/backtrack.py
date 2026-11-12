def binary_string(n):
    result = []

    def explore(path, nums):
        if len(path) == n:
            result.append("".join(path))
            return

        for num in nums:
            path.append(num)
            explore(path, nums)
            path.pop()

    explore([], "01")
    return result


print(binary_string(2))

def binary_no_adjacent(n):
    result = []

    def explore(path, nums):
        if len(path) == n:
            result.append("".join(path))
            return

        for num in nums:
            if path and path[-1] == "1" and num == "1":
                continue
            path.append(num)
            explore(path, nums)
            path.pop()

    explore([], "01")
    return result

print(binary_no_adjacent(2))