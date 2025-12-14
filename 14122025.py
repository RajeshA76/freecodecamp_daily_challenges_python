def title_case(title):
    words = title.split(" ")
    for index in range(len(words)):
        words[index] = words[index].capitalize()
    return " ".join(words)

