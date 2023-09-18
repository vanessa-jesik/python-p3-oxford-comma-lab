def oxford_comma(items):
    if len(items) == 1:
        return "".join(items)
    elif len(items) == 2:
        return " and ".join(items)
    else:
        items[-1] = "and " + items[-1]
        return ", ".join(items)
