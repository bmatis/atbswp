def comma_separated_list(list):
    result = ""
    for item in list[:-1]:
        result += item + ", "

    result += "and " + list[-1]
    return result

spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_separated_list(spam))

another_list = ['bob', 'tim', 'alice', 'sven', 'susan', 'reinhard', 'lucy']
print(comma_separated_list(another_list))
