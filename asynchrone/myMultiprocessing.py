from multiprocessing import Process

def worker():
    print('Worker')

if __name__ == '__main__':
    jobs = []
    for _ in range(5):
        p = Process(target=worker)
        jobs.append(p)
        p.start()
