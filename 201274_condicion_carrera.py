import threading 
import time
result = 2
  


def operacion(): 
    global result
    result = result*result
  

def resultados(lock): 
    global result
    lock.acquire() 
    operacion() 
    print(result) 
    lock.release() 
  

def main(): 
   
    for y in range(5):
        lock = threading.Lock() 
        sub_proceso = threading.Thread(target=resultados, args=(lock,)) 
        sub_proceso.start() 
        sub_proceso.join() 
    time.sleep(2)
   
  
if __name__ == "__main__": 
    main()
    
    