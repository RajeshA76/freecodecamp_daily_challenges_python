def parse_blockquote(markdown):
    markdown_split = markdown.split(">")
    start_text = "<blockquote>"
    end_text = "</blockquote>"
    return start_text + markdown_split[1].strip() + end_text 
