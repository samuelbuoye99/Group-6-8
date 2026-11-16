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