def user_help():
    return f"Available formatters: {' '.join(formatters)}\nSpecial commands: !help !done"


def user_done(output):
    file = open("output.md", "w")
    file.write(output)
    file.close()


def header():
    while True:
        level = int(input("Level: "))
        if 6 >= level >= 1:
            text = input("Text: ")
            return f"{('#') * level} {text}\n"
        else:
            print("The level should be within the range of 1 to 6")


def plain():
    text = input("Text: ")
    return text


def bold():
    text = input("Text: ")
    return f"**{text}**"


def italic():
    text = input("Text: ")
    return f"*{text}*"


def inline_code():
    text = input("Text: ")
    return f"`{text}`"


def link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"


def new_line():
    return "\n"


def ordered_list():
    while True:
        try:
            number_of_rows = int(input("Number of rows: "))
            if number_of_rows < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print("The number of rows should be greater than zero")

    output_lst = []
    for x in range(number_of_rows):
        user_input = input(f"Row #{x+1}: ")
        output_lst.append(f"{x+1}. {user_input}")
    return "\n".join(row for row in output_lst) + "\n"


def unordered_list():
    while True:
        try:
            number_of_rows = int(input("Number of rows: "))
            if number_of_rows < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print("The number of rows should be greater than zero")

    output_lst = []
    for x in range(number_of_rows):
        user_input = input(f"Row #{x+1}: ")
        output_lst.append(user_input)
    return "\n".join(f"* {row}" for row in output_lst) + "\n"


formatters = {
    "plain": plain, "header": header, "bold": bold, "italic": italic,
    "link": link, "new-line": new_line, "inline-code": inline_code,
    "ordered-list": ordered_list, "unordered-list": unordered_list}


def main():
    output = ""

    while True:
        user_input = input("Choose a formatter: ")
        if user_input in formatters.keys():
            new_input = formatters[user_input]()
            output += new_input
            print(output)
        elif "!help" in user_input:
            print(user_help())
            continue
        elif "!done" in user_input:
            user_done(output)
            break
        else:
            print("Unknown formatting type or command")

if __name__ == "__main__":
    main()
