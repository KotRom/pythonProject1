courses = {'history', 'programming', 'math', 'literature', 'physics', 'math'}
numbers = [1, 2, 3, 4]

print(type(courses))
print(courses) #ne mozhet byt dublikatov i net indeksacii - net porjadki i nelzja sortirovat' ili uporjadochit i postojanno menjaet mestami
courses.remove('math')
print(courses)
print()

set1 = {'Math', 'History', 'Programming', 'Physics'}
set2 = {'Art', 'Physics', 'Design', 'History'}
print(set1.intersection(set2))
print(set2.intersection(set1))
print()
print(set1.difference(set2))
print(set2.difference(set1))
print()
print(set1.union(set2))
print()