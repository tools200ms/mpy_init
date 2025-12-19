import sys

if sys.implementation.name == 'micropython':
        from micropython import const
else:
    def const(x):
        return x

try:
    import threading
except ImportError:
    # If 'threading' is missing (as it's the case for MicroPython),
    # create 'threading' compatibility object, so
    # basic thread functions can be used like
    # in CPhyton

    import _thread

    class ApiBridge:
        pass

    threading = ApiBridge()

    def thread_wrapper(group=None, target=None, name=None, args=(), kwargs=None, daemon=None):
        if kwargs is not None or daemon is not None:
            raise Exception("Not supported argument")

        t = ApiBridge()
        t.start = lambda: _thread.start_new_thread(target, args)
        return t


    threading.Thread = thread_wrapper
    threading.Lock = _thread.allocate_lock

try:
    from time import perf_counter
except ImportError:
    # If 'time.perf_counter()' is missing (as it is the case for
    # micropython), add wrapper function.
    from time import ticks_us
    perf_counter = lambda: ticks_us() / 1_000_000.0

def cpu_stress_thread(name, result, lock=None):
    # while True:
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

    # release lock if hass been passed:
    if lock != None:
        lock.release()


# 'const()' function to define constants in MicroPython.
PRIME_NUMBER_TOTAL_CNT = const(3600)

print(f"Python implementation: {sys.implementation.name}")

lock1 = threading.Lock()
lock1.acquire()
lock2 = threading.Lock()
lock2.acquire()

result1 = {"value": None}
result2 = {"value": None}
resultm = {'value': None}

thread1 = threading.Thread(target=cpu_stress_thread, args=('Thread-1', result1, lock1))
thread2 = threading.Thread(target=cpu_stress_thread, args=('Thread-2', result2, lock2))

print(f"Waiting for threads to finish job ...")
time_start = perf_counter()
# Start two threads
thread1.start()
thread2.start()
# Start 'MainThread'
cpu_stress_thread('MainThread', resultm)

lock2.acquire()
lock1.acquire()

time_end = perf_counter()

# total time
total_time = time_end - time_start

print(f"Time waited for tasks to finish: {total_time:.2f} sec\n")

last_prime_resm = resultm['value'][-1]
last_prime_res1 = result1['value'][-1]
last_prime_res2 = result2['value'][-1]

print("Last prime number: ")
print(f"\nResultM: {last_prime_resm}\nResult1: {last_prime_res1}\nResult2: {last_prime_res2}")

