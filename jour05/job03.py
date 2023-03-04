def string_len(str, count):
    if str == "":
        return count
    else:
        return string_len(str[1:], count + 1)

print(string_len("abc123", 0))