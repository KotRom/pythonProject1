print("Hello Roman"[1:4])
print("Hello Roman"[0:4])

string_sample = "Hello Roman Roman"
print(len(string_sample))
print((string_sample[12]))
print(string_sample[-7:-12])
print(string_sample[6:11])
print(string_sample[-5:])
print(string_sample[:5])

# [START:FINISH:STEP]
print(string_sample[::-1])
print(string_sample[1:7:1])

string_sample6 = str(1234567890)
print(len(string_sample6))

print("world" in string_sample)
print("Roman" in string_sample)

german_sample = "der Fluß"
print((german_sample.upper()))
print((german_sample.lower()))
print((german_sample.casefold()))
print("HELLO" in string_sample.upper().lower())

user_surname = "KoTeNjov"
user_name = "RoMaN"
print("Hello " + user_name + " " + user_surname)
user_name = user_name.capitalize()
user_surname = user_surname.capitalize()
print("Hello " + user_name + " " + user_surname)

print(string_sample.replace("Roman", "Oleg", 1))

# print(string_sample.split())
# a, b, c = string_sample.split()
# print(a)
# print(b)
# print(c)

a = "Hello"
b = "world"
print(a, b, 2021)
print(a + b, 2021)
print(a + b + str(2021))

salary = 1000
my_name = "Roman"
my_surname = "Kotenjov"

sample = "{name} salary is {sal}"
print(sample.format(name=my_name, sal=salary))

print(f"{user_name.capitalize()} {user_surname}´s salary is {salary * 0.78:.2f}")