def binary_strings(n):
    a = 0
    binary = []

    while a <= n:
        current = format(a, 'b')
        binary.append(current)

        a += 1

    return binary

print(binary_strings(0))
print(binary_strings(1))
print(binary_strings(2))
print(len(binary_strings(4)))
