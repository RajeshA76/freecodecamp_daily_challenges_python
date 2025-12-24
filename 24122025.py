import re
def parse_image(markdown):
    pattern = r"\[(.*)\]\((.*)\)"
    match = re.search(pattern,markdown)
    if match:
        alt_text,url = match.groups()
    return f'<img src="{url}" alt="{alt_text}">'