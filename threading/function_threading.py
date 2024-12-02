import threading
import math


start_array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

def threaded_function1(results):
    s = sum(start_array)

    results.append(s)

def threaded_function2(results):
    nsum = 0
    for i in start_array:
        nsum -= i

    results.append(nsum)

def threaded_function3(results):
    s = (min(start_array)+max(start_array))//2

    results.append(s)




#Treading
results = []

data = [threaded_function1,threaded_function2,threaded_function3]


if len(data)>0:

    threads = []
    for i in range(len(data)):
        thread = threading.Thread(target=data[i],args=(results,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

print(results)