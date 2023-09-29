# THREAD IN PYTHON

## Thread:
- It is a single program that is executed in a memory.

## Multithreading :
- Multiple programs running concurrently or parallely in the same memory space.

### Steps in multithreading:
#### step 1 :
- Import module in the program :

    import threading

- This is the predefined module which can be used when we execute the thread.

#### step 2 :
- Create a thread in the program :

    t = threading.Thread(target, args)

- To create a thread we have to create a object, t is the variable used to store the thread id.
- The target is the function executed by thread and args is the parameter to be passed in the 
  thread function.

#### step 3 :
- Start a thread in the program :

    t.start()

- To start a thread the predefined function start() is used.

#### step 4 :
- When the thread starts, the current program starts executing. 
- To stop the current program till the thread is completed the predefined function join() is used.

    t.join()

- If we are not using join() method the program will be completed before the thread is fully executed.

## Example for Threading:

import threading
import time

def print_square(num):
    print (num * num)
    time.sleep(2)
    print("thread is done\n")


if __name__ =="__main__":

        t = threading.Thread(target = print_square, args=(10,))
        t.start()
        t.join()

        print("Done")



