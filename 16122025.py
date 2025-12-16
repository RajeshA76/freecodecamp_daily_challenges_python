def has_consonant_count(text, target):
    count = 0
    for char in text:
        if char.isalpha() and  char.lower() not in ['a','e','i','o','u']:
            count += 1
    if count == target:
        return True
    else:
        return False