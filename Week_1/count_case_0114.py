def case_counter(text):
    uppercase_count = 0
    lowercase_count = 0

    for every_character in text:
        if every_character.isupper():
            uppercase_count += 1
        elif every_character.islower():
            lowercase_count += 1
        else:
            pass
    return uppercase_count, lowercase_count

text = input("Please input anything:")
uppercase, lowercase = case_counter(text)
print(f"Uppercase count: {uppercase}")
print(f"Lowercase count: {lowercase}")