from concurrent.futures import ThreadPoolExecutor

def worker():
    print('Worker')

with ThreadPoolExecutor(max_workers=5) as executor:
    for _ in range(5):
        executor.submit(worker)
