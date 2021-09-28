import re
with open('people.txt', 'r', encoding='utf8') as file:
    data = file.read()

    pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    matches = pattern.finditer(data)
    print(type(matches))
    match_list = []
    for match in matches:
        print(match)
        match_list.append((match.group()))

print(match_list)
