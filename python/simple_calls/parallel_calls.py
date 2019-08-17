"""
Using non async io calls
"""

import multiprocessing as mp
from multiprocessing.pool import ThreadPool

import requests

from simple_calls.time_it_class import time_it


def fetch():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    data = response.json()
    return data


def parallel_processes():
    # heavy weight processes.
    pool = mp.Pool(mp.cpu_count())
    results = [pool.apply(fetch, args=()) for row in [range(0, 10)]]
    pool.close()


def parallel_threads():
    # light weight processes.
    pool = ThreadPool(processes=mp.cpu_count(), )
    results = [pool.apply(fetch, args=()) for row in [range(0, 10)]]
    pool.close()


def parallel_threads_all_at_once(count:int):
    # light weight processes.
    pool = ThreadPool(processes=count, )
    results = [pool.apply(fetch, args=()) for row in [range(0, count)]]
    pool.close()

if __name__ == "__main__":
    def run():
        # notes- processes 2x faster, threads 10x faster, threads all at once 15x faster

        # https://www.machinelearningplus.com/python/parallel-processing-python/
        print("Parallel processes, cpu_count at a time")
        with time_it():
            # this would be fastest if we were cpu bound
            parallel_processes()

        print("Parallel threads, cpu_count at a time")
        with time_it():
            parallel_threads()

        print("10 threads all at one time")
        with time_it():
            # we are io bound... this is going to be fastest
            parallel_threads_all_at_once(10)


    run()
