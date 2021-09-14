
test_list = [1, 2, 3, 4, 5]
print(test_list)
#test_list[1] = "seven"
#print(test_list)
test_list[1:4] = [5, 5, 5, 5, 5] #zamenjaet element v spiske
print(test_list)

courses = ['history', 'programming', 'Math', 'literature', 'physics']
string_sample = "hello world"
courses.append('art') #dobavljaet v konec spiska
print(courses)
print(courses[-1])
print(courses[4])
courses.insert(2, "enfglish") #dobavljaet na vtoroj index - vse indexes sprava menjajutca na +1
print(courses)
print(courses[4])

new_courses = ['art', 'english']
courses.extend(new_courses) #rashirjaet spiskom
print(courses)
courses.extend('english') #rashirjajt integrirovannym objektom razbity na spisok
print(courses)

#courses.remove('enfglish') #udaljaet bez vozvratno
deleted = courses.pop(1)
print(courses)
courses.pop(1) #indexes smeschaetca na odin index
courses.pop() #udaljet v konce spiska

print(courses)
#courses = courses[::-1]
courses.reverse() #spisok anoborot
#courses = reversed(courses)
print(courses)

courses.sort()
print(courses)
print(sorted(courses))
sorted_courses = sorted(courses)
print(sorted_courses)


numbers =[1, 6, 4, 7, -100, 0, 9, 11]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers)) #tolko dlja intrger - dlja chisel
print()
print(min(courses))
print(max(courses))
print()
print("hello world".find("world"))

print()
print(courses.index("english"))

#course = input("plese input corse: ")
#print(courses.index(course))

print('Math' in courses)
print()

print("hello people of earth".split()) #razbivae stroku na spisok po probelu
print("hello, people, of, earth".split()) #razbivae stroku na spisok po probelu
print("hello, people, of, earth".split(", ")) #razbivae stroku na spisok po  zapjaoj


courses_new = ['history', 'programming', 'Math', 'literature', 'physics']
print(courses_new)
print('...'.join(courses_new))
print('...'.join(courses_new[1:4]))
print()
print(courses + numbers)
print()


new_courses = courses
new_courses.pop(0)
courses.pop()
print(courses)
print(new_courses)
print()

new_courses = courses.copy()
new_courses.pop(0)
courses.pop()
print(courses)
print(new_courses)
print()

empty_tuple = ()
empty_tuple2 = tuple() #kartezh
print(numbers)
print(tuple(numbers))
print()



