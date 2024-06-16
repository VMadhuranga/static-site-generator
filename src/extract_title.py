def extract_title(markdown):
    heading_level, *title = markdown.split("\n")[0].split()
    if "#" in heading_level and len(heading_level) == 1:
        return " ".join(title)
    raise Exception("All pages need a single h1 header")
