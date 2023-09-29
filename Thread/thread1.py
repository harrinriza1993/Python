import threading
import time

def print_square(num):
    print (num * num)
    time.sleep(2)
    print("first thread is done\n")

def print_cube(num):
    print(num * num * num)
    time.sleep(2)
    print("second thread is done\n")

if __name__ =="__main__":

        t1 = threading.Thread(target = print_square, args=(10,))
        t2 = threading.Thread(target = print_cube, args=(10,))
        t1.start()
        t1.join()
        t2.start()
        t2.join()

        print("Done")


