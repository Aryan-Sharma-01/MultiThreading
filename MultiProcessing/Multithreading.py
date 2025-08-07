import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Numbers:{i}")

def print_leters():
    for letter in "abcde":
        time.sleep(2)
        print(f"letter:{letter}")   


## Creating 2 threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_leters)

t=time.time()
t1.start()
t2.start()
t1.join()
t2.join()
finished_time=time.time()-t  
print(finished_time) 