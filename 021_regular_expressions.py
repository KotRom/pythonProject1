import re
text_to_search = '''
123123123
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaH
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
-23*555*5555
800-555-1234
900-555-1235
988-555-5312
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
Mr. O`Rilley
abc

ball mall hall wall tall
333-333-3333333333
'''
sentence = 'Start a sentence Start and then bring \n it to an end bring'
#print('\tTab')
#print(f'\tTab')
#print(r'\t\nTab') #r' - sytraja stroka
#pattern = re.compile(r'M(rs|r|s)')
#pattern = re.compile(r'M(rs|r|s)\.? [A-Z](`[A-Z][a-z]*|[a-z]*)')
pattern = re.compile(r'M(rs|r|s)\.? [A-Z](`[A-Z]\w*|[a-z]*)')
#pattern = re.compile(r'\d\d\d-\d\d\d-[1-35-9]\d\d\d')
#pattern = re.compile(r'[abx]')
#pattern = re.compile(r'[^89]\d\d-\d\d\d-\d\d\d\d')
#pattern = re.compile(r'[^wh]al')
#pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
#pattern = re.compile(r'[\d{3,9}')
matches = pattern.finditer(text_to_search) #sozdajit vse sovpadenija po shablony v itteriruemyj objekt
#matches = pattern.finditer(sentence) #sozdajit vse sovpadenija po shablony v itteriruemyj objekt
print(pattern)
#print(type(pattern))
for match in matches:
    print(match)

