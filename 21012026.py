


def parse_inline_code(markdown):
    result = ""
    l,r = 0,0
    is_code = False
    for k in range(len(markdown)):
        if not is_code and markdown[k] == '`':
            is_code = True
            l = k 
            r = k
        elif is_code and markdown[k] != '`':
            r += 1
        elif is_code and markdown[k] == '`':
            result += f"<code>{markdown[l+1:r+1]}</code>"
            is_code = False
        else:
            result += markdown[k]
    return result

