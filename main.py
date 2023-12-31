# Challenge 1: 12-hour time to 24-hour time Convertor

def convert_to_24_hour(hour, minute, period):
    if period == "am":
        if hour == 12:
            hour = 0
    elif period == "pm":
        if hour != 12:
            hour += 12
    
    return f"{hour:02d}{minute:02d}"
pass



# Challenge 2: Exactly two positive numbers

def exactly_two_positive(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    
    return positive_count == 2

# Examples
print(exactly_two_positive(3, -5, 8))   # True
print(exactly_two_positive(-2, 9, -1))   # False
pass



# Challenge 3: Consonant value calculator

def solve(s):
    consonant_values = []
    current_value = 0
    
    for characters in s:
        if characters in "bcdfghjklmnpqrstvwxyz":
            current_value += ord(characters) - ord('a') + 1
        else:
            consonant_values.append(current_value)
            current_value = 0
    
    consonant_values.append(current_value)
    
    return max(consonant_values)
pass


