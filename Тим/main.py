from multiprocessing import Process
def print_func(fruit='Mango'):
    print('The fruits is : ', fruit)
if __name__ == "__main__":
    names = ['apple', 'orange', 'pineapple']
    procs = []
    proc = Process(target=print_func)
    procs.append(proc)
    proc.start()
    for name in names:
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()