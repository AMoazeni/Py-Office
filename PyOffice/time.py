import time

t_start = time.time()

for i in range(100000):
    i+=1

t_end = time.time()

t_total = t_end - t_start

print ('Time: {0:.3f}s'.format(t_total))