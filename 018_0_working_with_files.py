# 'r' read
# 'a' append
# 'w' write
# 'x' create
# 'r+' read and write
file = open('loren_text.txt', 'r', encoding='UTF8')
#print(file.name)
#print(file.mode)
#print(file.closed) proverka na zakryt li file

#data = file.read()
#data = file.readlines() stroki v spisik
#data = file.readline() schityvaet stroku
#data1 = file.readline()
#print(data)
#print(data1)

#for x in file:
#    print(x)

#data = file.read(100) #chitaet opredeleennoe kolichestvo simvolov

size_to_read = 100
data = file.read(size_to_read)
while len(data) != 0:
    print(len(data))
    data = file.read(size_to_read)
print(data)
file.seek(110)
data1 = file.read(size_to_read)
print(data1)

file.write()


file.close()
print(file.closed)

