from asyncio import Task
import asyncio

from src.questions.q_1 import fetch_data
# Task 2: Run multiple async tasks concurrently
# 
# - Goal: start several async fetch operations concurrently and collect their results.
# - Inputs: inside this function we have two parallel lists, `urls` and `delays`.
#   Each pair (url, delay) should be scheduled as an independent asynchronous task
#   that calls `fetch_data(url, delay)` imported from `q_1`.
# - Output: return a list of results (list[str]) from each `fetch_data` call in the
#   same order as the input pairs.
#
# Implementation hints:
# - Use `asyncio.create_task(...)` to schedule each `fetch_data` call and keep
#   the returned Task objects in a list (typed as `list[Task[str]]`).
# - Use `await asyncio.gather(*tasks)` to run all tasks concurrently and collect
#   their results.
#
# Success criteria:
# - Run `python -m unittest testing.test_q2` to validate your implementation.


async def async_main():
    urls = ["https://vama.software", "https://vama.services", "https://vintechhk.com"]
    delays = [2, 4, 6]

    tasks: list[Task[str]] = []

    for url, delay in zip(urls, delays):
        # TODO: Add tasks to the list
        task = ...
        tasks.append(task)

    # TODO: Gather results from all tasks
    results = ...

    for result in results:
        print(result)

    return results
