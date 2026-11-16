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