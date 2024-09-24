
def remove_special_charecters(text: str) -> str:
    return text.replace(r"/[^a-zA-Z0-9 ]/g", "")


def standardize_text(text: str) -> str:
    return remove_special_charecters(text) \
        .lower()
