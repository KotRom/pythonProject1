# 'r' - read
# 'a' - append
# 'w' - write
# 'x' - create
# 'r+' - read and write

with open('text_files/random-dice.jpg', 'rb') as read_file:
    with open('text_files/random-dice2.jpg', 'wb') as write_file:
        chunk_size = 4096
        data = read_file.read(chunk_size)
        while len(data) > 0:
            write_file.write(data)
            data = read_file.read(chunk_size)
