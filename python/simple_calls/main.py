"""
Show of basic, blocking http requests
"""

import math
import time

import requests


def fetch():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    data = response.json()
    return data


def single():
    print(fetch())


class time_it(object):
    def __init__(self, show: bool = True):
        self.show = show

    def __enter__(self):
        self.start_time = time.perf_counter()  # in seconds
        # don't forget return self
        # https://stackoverflow.com/questions/4835611/pythons-with-statement-target-is-unexpectedly-none
        return self

    def format_time(self, seconds: float):
        whole_seconds = math.floor(seconds)
        milliseconds = math.floor((seconds - whole_seconds) * 1000)
        if whole_seconds and milliseconds:
            return f"{whole_seconds}s {milliseconds}ms"

        if whole_seconds:
            return f"{whole_seconds}s"

        if milliseconds:
            return f"{milliseconds}ms"

    def elapsed(self):
        so_far = time.perf_counter()
        return so_far - self.start_time

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.perf_counter()
        self.elapsed_seconds = self.end_time - self.start_time
        if self.show:
            print(self.format_time(self.elapsed_seconds))


if __name__ == "__main__":
    def run():
        with time_it():
            single()

        with time_it(show=False) as clock:
            for _ in range(0, 10):
                single()

            print("Average %s" % clock.format_time(clock.elapsed() / 10))


    run()
