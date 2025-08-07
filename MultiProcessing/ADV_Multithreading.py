#Multithreading with ThreadPool
from concurrent.futures import ThreadPoolExecutor
import time

def Print_numbers(number):
    time.sleep(1)
    return f"NUMBER :{number}"

numbers=[1,2,3,4,5 ] 
with ThreadPoolExecutor(max_workers=3)as executor:
    results=executor.map(Print_numbers,numbers)


for result in results:
    print(result)    