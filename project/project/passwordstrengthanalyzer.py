import re
import random
import string

def analyze_password(password):
    score = 0
    feedback = []

    # Check Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check Complexity
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    # Determine Overall Strength
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def suggest_strong_password(length=12):
    """Generates a random, strong password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the generated password meets all criteria
    while True:
        pwd = ''.join(random.choice(characters) for _ in range(length))
        if (any(c.islower() for c in pwd) and 
            any(c.isupper() for c in pwd) and 
            any(c.isdigit() for c in pwd) and 
            any(c in string.punctuation for c in pwd)):
            return pwd

# --- Example Usage ---
user_input = input("Enter a password to test: ")
strength, tips = analyze_password(user_input)

print(f"\nPassword Strength: **{strength}**")

if tips:
    print("How to improve:")
    for tip in tips:
        print(f"- {tip}")
    
    suggestion = suggest_strong_password()
    print(f"\nHere is a stronger alternative you could use: {suggestion}")