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