def to_screaming_snake_case(variable_name):
    if "_" in variable_name:
        result = variable_name.split("_")
    elif "-" in variable_name:
        result = variable_name.split("-")
    else:
        result = []
        word = variable_name[0]
        for char in variable_name[1:]:
            if char.isupper():
                result.append(word)
                word = char
            else:
                word += char
        result.append(word)
    return "_".join(result).upper()