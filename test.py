def calculate_variability(password):
    n = len(password)
    if n == 1:  # A single character password has only one variability - itself
        return 1

    # Precompute the number of distinct characters before and after each character
    distinct_before = [0] * n
    distinct_after = [0] * n
    seen_chars_before = set()
    seen_chars_after = set()

    for i in range(n):
        seen_chars_before.add(password[i])
        distinct_before[i] = len(seen_chars_before)

    for i in range(n - 1, -1, -1):
        seen_chars_after.add(password[i])
        distinct_after[i] = len(seen_chars_after)

    # Calculate variability based on distinct characters before and after each character
    variability = 0
    for i in range(n):
        # Subtract 1 to avoid double-counting the character itself
        variability += distinct_before[i] + distinct_after[i] - 1

    # Add 1 for the original string itself
    variability += 1

    return variability


# Test the function with a sample password
# sample_password = "abca" 15
sample_password = "abaa"
variability = calculate_variability(sample_password)
print(f"The variability of the password '{sample_password}' is: {variability}")
