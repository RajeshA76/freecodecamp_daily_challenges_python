def has_consonant_count(text, target):
    count = 0
    vowels = {'a','e','i','o','u'}
    for char in text:
        if char.isalpha() and  char.lower() not in vowels:
            count += 1
    if count == target:
        return True
    else:
        return False