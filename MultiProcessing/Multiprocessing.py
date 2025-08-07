#Processes that run in parallel
#CPU-Bound Tasks tasks that areheavy
#parallel Execution
import multiprocessing
import multiprocessing.process
import time
def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"square:{i*i}")
        
def cube_numbers():
       for i in range(5):
            time.sleep(1.5)
            print(f"cube:{i*i*i}")


if __name__=="__main__":
#create 2 processes

 p1=multiprocessing.process(target=square_numbers)
 p2=multiprocessing.process(target=cube_numbers)  
 t=time.time()
 p1.start()
 p2.start()                 

#wait process to complete
 p1.join()
 p2.join()


 finished_time=time.time()-t  
 print(finished_time)  