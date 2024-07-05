import datetime 
import multiprocessing
import random 
import time 

def differentCounting(now): 
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    print(now) 
now = 0 
wait = 0 
if __name__ == "__main__": 
   wait = random.randint(0, 1) 
   time.sleep(wait) 
   one = multiprocessing.Process(target = differentCounting(now)) 
   wait = random.randint(0, 1) 
   time.sleep(wait) 
   two = multiprocessing.Process(target = differentCounting(now)) 
   wait = random.randint(0, 1) 
   time.sleep(wait) 
   three = multiprocessing.Process(target = differentCounting(now)) 