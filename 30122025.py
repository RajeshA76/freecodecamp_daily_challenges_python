def string_sum(s):
    num = ""
    total = 0
    has_alpha = False
    prev = None

    for char in s:
        if char.isalpha():
            has_alpha = True
            if prev and not prev.isalpha():
                total += int(num)
                num = ""
        else:
            num += char
        prev = char

    if num:
        total += int(num)

    return total if has_alpha else int(s)
