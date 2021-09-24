import time



start = time.time()
print(start)
print(time.asctime()) #vyvodit prosto stroku so vremenem
print(time.gmtime())
print(type(time.gmtime()))
gm_time = time.gmtime()
print(gm_time[0:2])

print('hello')
time.sleep(5)
print('good bye')

stop = time.time()
print(f'time left {stop-start} seconds')