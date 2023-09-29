# MULTIPROCESSING IN PYTHON

## Multiprocessing:
- It is the ability of a system to run two or more process at the same time but in different memory space.
- We can run two or more thread in one processor.

### Steps in muliprocessing:
#### step 1 :
- Import module in the program :

    import multiprocessing

- This is the predefined module which can be used when we execute the multiprocessing.

#### step 2 :
- Create a multiprocessing in the program :

    p = multiprocessing.Process(target, args)

- p is a variable , which stores the processor id.
- The target is the function executed by processor and args is the parameter to be passed in the 
  processor function.

#### step 3 :
- Start a processor in the program :

    p.start()

- To start a processor the predefined function start() is used.

#### step 4 :
- When the processor starts, the current program starts executing. 
- To stop the current program till the processor is completed the predefined function join() is used.

    p.join()

- If we are not using join() method the program will be completed before the processor is fully executed.

## Example for processor:

import multiprocessing
import time

def print_square(num):
    print (num * num)
    time.sleep(2)
    print("First processor is done\n")

def print_cube(num):
    print (num * num * num)
    time.sleep(2)
    print("Second processor is done\n")


if __name__ =="__main__":

        p1 = multiprocessing.Process(target = print_square, args=(10,))
        p2 = multiprocessing.Process(target = print_cube, args=(10,))

        p1.start()
        p1.join()

        p2.start()
        p2.join()

        print("Done")

## Communication between processors using queue:
- The main purpose of queue is to communicate between processors.
- The producer processor can put the information in the queue and the consumer
  processor gets the information from the queue.
- put() is a function used to put the information in the queue.
- get() is a function used to get the information from the queue.

### Example of multiprocessor comunication using queue:
from multiprocessing import Process, Queue
def processor1(q):
    q.put("Hai")

def processor2(q):
    print(q.get())
    
if __name__ == '__main__': 
    q = Queue()
    p1 = Process(target = processor1, args= (q,))
    p2 = Process(target = processor2, args = (q,))
    p1.start()
    p2.start()






