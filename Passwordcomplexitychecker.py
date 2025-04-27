import re


def check_password_strength(password):
    # Define the criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Calculate the strength score
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    # Provide feedback based on the score
    if score == 5:
        strength = "Strong"
    elif 4 <= score < 5:
        strength = "Moderate"
    elif 3 <= score < 4:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Return the results
    return {
        "Length Criteria Met": length_criteria,
        "Uppercase Criteria Met": uppercase_criteria,
        "Lowercase Criteria Met": lowercase_criteria,
        "Digit Criteria Met": digit_criteria,
        "Special Character Criteria Met": special_char_criteria,
        "Strength": strength  # Return the strength as a string
    }


# Example usage
password = input("Enter a password to check its strength: ")
result = check_password_strength(password)

print("\nPassword Strength Feedback:")
for criteria, met in result.items():
    # Print "Yes" for met criteria, otherwise the actual value (which is "Strong", "Moderate", etc.)
    if isinstance(met, bool):
        print(f"{criteria}: {'Yes' if met else 'No'}")
    else:
        print(f"{criteria}: {met}")
