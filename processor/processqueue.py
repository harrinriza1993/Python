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