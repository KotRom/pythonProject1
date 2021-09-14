courses = ('history', 'programming', 'Math', 'literature', 'physics')
numbers = [1, 2, 3, 4]

courses = list(courses)
courses[2] = "hello world"
courses = tuple(courses)
print(courses)


empty_tuple = (1, 2, 3)
print(courses + empty_tuple)

print(numbers)
print(tuple(numbers))
print()

empty_list = []
empty_tuple = ()
empty_set = {}
print(type(empty_list))
print(type(empty_set))
print(type(empty_tuple))
