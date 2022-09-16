def get_percentage(number, round_digits=None):
    output = round(number * 100, round_digits)
    return f"{output}%"

# print(get_percentage(0.323, 3))
