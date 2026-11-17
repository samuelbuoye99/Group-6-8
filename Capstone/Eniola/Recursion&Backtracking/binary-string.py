def binary_strings(n):
    results = []
    current = []

    def backtrack():
        # Base case
        if len(current) == n:
            results.append("".join(current))
            return

        # Try both possible characters
        for bit in ["0", "1"]:
            current.append(bit)  # Choose

            backtrack()         # Explore

            current.pop()       # Unchoose

    backtrack()
    return results

print(binary_strings(0))
print(binary_strings(1))
print(binary_strings(2))
print(len(binary_strings(4)))

def binary_no_adjacent_ones(n):
    results = []
    current = []

    def backtrack():
        if len(current) == n:
            results.append("".join(current))
            return

        # Always allowed to append 0
        current.append("0")
        backtrack()
        current.pop()

        # Only append 1 if the previous character isn't 1
        if not current or current[-1] != "1":
            current.append("1")
            backtrack()
            current.pop()

    backtrack()
    return results

print(binary_no_adjacent_ones(0))
# [""]

print(binary_no_adjacent_ones(1))
# ["0", "1"]

print(binary_no_adjacent_ones(2))
# ["00", "01", "10"]

print(binary_no_adjacent_ones(3))
# ["000", "001", "010", "100", "101"]