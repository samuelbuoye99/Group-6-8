def letter_case(s):
    results = []
    current = []

    def build(i):
        # Base case: Every character has been processed
        if i == len(s):
            results.append("".join(current))
            return

        char = s[i]

        # Digits have only one option
        if char.isdigit():
            current.append(char)
            build(i + 1)
            current.pop()

        # Letters have two options
        else:
            for option in [char.lower(), char.upper()]:
                current.append(option)
                build(i + 1)
                current.pop()

    build(0)
    return results

print(letter_case(""))
# [""]

print(letter_case("12"))
# ["12"]

print(letter_case("3z4"))
# ["3z4", "3Z4"]

print(letter_case("a1b2"))
# ["a1b2", "a1B2", "A1b2", "A1B2"]

def letter_case_even_upper(s):
    results = []
    current = []

    def build(i, uppercase_count):
        if i == len(s):
            if uppercase_count % 2 == 0:
                results.append("".join(current))
            return

        char = s[i]

        if char.isdigit():
            current.append(char)
            build(i + 1, uppercase_count)
            current.pop()

        else:
            # Lowercase option
            current.append(char.lower())
            build(i + 1, uppercase_count)
            current.pop()

            # Uppercase option
            current.append(char.upper())
            build(i + 1, uppercase_count + 1)
            current.pop()

    build(0, 0)
    return results

print(letter_case_even_upper("a1b2"))