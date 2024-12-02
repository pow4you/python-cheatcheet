import threading
import math
import numpy as np

start_array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

def threaded_function(batch_data, results):
    for v in batch_data:
        #print(str(v))

        results.append(v+1)




#Treading
results = []

data = start_array
print(np.shape(data))
thread_num = 4

if len(data)>0:
    class_size = math.ceil(len(data)/thread_num)
    classes = [data[x:x+class_size] for x in range(0, len(data), class_size)]

    threads = []
    for i in range(len(classes)):
        results.append([])
        thread = threading.Thread(target=threaded_function,args=(classes[i],results[i], ))
        threads.append(thread)

        print(np.shape(classes[i]))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

results = [item for sublist in results for item in sublist]
print(results)
print(np.shape(results))