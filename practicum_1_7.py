time = 1234565
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("%d:%d:%d:%d" % (day, hour, minutes, seconds))