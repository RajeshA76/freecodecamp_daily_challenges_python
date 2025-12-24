import re
def email_chain_count(subject):
    pattern = r"(fw|fwd|re):"
    matches = re.findall(pattern,subject,re.IGNORECASE)
    return len(matches)