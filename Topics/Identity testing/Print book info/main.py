def strip_input(user_input):
    if user_input is None:
        return None
    return user_input.split(":", 1)[-1].lstrip()


def print_book_info(title, author=None, year=None):
    title = strip_input(title)
    author = strip_input(author)
    year = strip_input(year)

    output = [f'"{title}"', "was written", f"by {author}", f"in {year}"]

    if isinstance(author, str) and isinstance(year, str):
        print(" ". join(output))
    elif isinstance(author, str):
        print(" ".join(output[:3]))
    elif isinstance(year, str):
        print(f"{output[0]} {output[1]} {output[3]}")
    else:
        print(output[0])
