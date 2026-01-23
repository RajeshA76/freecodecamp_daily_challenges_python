def to_consonant_case(s):
    result = ""
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    for char in s:
        if char in vowels:
            result += char.lower()
        elif char == "-":
            result += "_"
        elif (ord(char) >= 65 and ord(char) <= 122):
            result += char.upper()
        else:
            result += char
    return result
