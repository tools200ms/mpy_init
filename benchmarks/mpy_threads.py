
try:
    import _thread

    class Empty: pass
    threading = Empty()

    def thread_wrapper(group=None, target=None, name=None, args=(), kwargs=None, daemon=None):
        if kwargs is not None or daemon is not None:
            raise Exception("Not supported argument")

        t = Empty()
        t.start = lambda : _thread.start_new_thread(target, args)
        return t

    threading.Thread = thread_wrapper
    threading.Lock = _thread.allocate_lock

except ImportError:
    import threading


import time


if not hasattr(time, 'ticks_ms'):
    time.ticks_ms = lambda : int(time.perf_counter() * 1000)
    time.ticks_diff = lambda t1, t0 : t1 - t0



PRIME_NUMBER_TOTAL_CNT = 12000

def cpu_stress_thread(name, result, lock = None):

    #while True:
    # Very basic CPU-bound task: count prime numbers
    num = 2
    primes = []
    while True:
        if all(num % p != 0 for p in primes):
            primes.append(num)
            if len(primes) == PRIME_NUMBER_TOTAL_CNT:
                break
        num += 1

    result['value'] = primes

    if lock != None:
        lock.release()


# Start second thread
lock1 = threading.Lock()
lock1.acquire()
lock2 = threading.Lock()
lock2.acquire()

t_start = time.ticks_ms()

result1 = {"value": None}
t1 = threading.Thread(target=cpu_stress_thread, args=("Thread-1",result1, lock1))

result2 = {"value": None}
t2 = threading.Thread(target=cpu_stress_thread, args=("Thread-2",result2, lock2))

t1.start()
t2.start()

# Main thread also does work
result0 = {"value": None}
cpu_stress_thread("MainThread", result0)


print("waiting ...")
r_start = time.ticks_ms()
lock2.acquire()
lock1.acquire()
t_end = time.ticks_ms()
# total time
t_time = time.ticks_diff(t_end, t_start)
# resting time
r_time = time.ticks_diff(t_end, r_start)
print(f"Waited for thread: {r_time} ms, total time: {t_time/1000:.4f} sec\nTime % spend on waiting for thread: {100*(r_time/t_time):3.2f}%")

print("Result0: ")
for p in result0['value'][-10:]: print(str(p), end=' ')
print("\nResult1: ")
for p in result1['value'][-10:]: print(str(p), end=' ')
print("\nResult2: ")
for p in result2['value'][-10:]: print(str(p), end=' ')

print("\n")
