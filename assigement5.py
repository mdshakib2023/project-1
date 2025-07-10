#Develop a program that returns the maximum and minimum values from a tuple of numbers.

def max_min(numbers):
    if not numbers:
        return "The tuple is empty."

    max_value = max(numbers)
    min_value = min(numbers)
    return max_value, min_value

# Example usage
numbers = (4, 12, -3, 7, 0, 18, 5)
maximum, minimum = max_min(numbers)

print("Maximum value:", maximum)
print("Minimum value:", minimum)
