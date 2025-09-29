from asyncio import Task
import asyncio

# Task 3: Handle exceptions in async code
#
# - Goal: run several async fetch operations concurrently, but treat any
#   long-running calls (delay > 5) as failures by raising an exception and
#   handling those exceptions when collecting results.
# - Inputs: inside `async_main()` there are two parallel lists, `urls` and
#   `delays`. Each pair (url, delay) should be scheduled as an independent
#   asynchronous task that calls `fetch_data(url, delay)` defined in this
#   module (you may reuse the implementation from `q_2`).
# - Output: return a list of results where each successful fetch returns the
#   fetched string and failures are represented by the exception instance in
#   the corresponding position. The ordering of results must match the input
#   pairs.
#
# Implementation hints:
# - In `fetch_data(url, delay)`, raise `ValueError` when `delay > 5` to simulate
#   a failed fetch.
# - Use `asyncio.create_task(...)` to schedule each `fetch_data` call and keep
#   the returned Task objects in a list (typed as `list[Task[str]]`).
# - Use `await asyncio.gather(*tasks, return_exceptions=True)` to run all tasks
#   concurrently and collect their results; `return_exceptions=True` will allow
#   gather to return exception objects for tasks that raised.
# - When iterating the gathered results, check whether an item is an
#   exception (e.g., `isinstance(result, Exception)`) and print
#   `Error fetching url: {error}` for failures; otherwise print the successful
#   result string.
#
# Success criteria:
# - Running `python -m unittest testing.test_q3` should validate your
#   implementation for this task.

# TODO: Implement `fetch_data()` and `async_main()` per the spec below.
async def fetch_data(url: str, delay: int) -> str:
    # TODO: Add a logic to raise ValueError if delay > 5
    ...

    # TODO: Copy the `fetch_data()` function to here from q_1.py
    ...


async def async_main():
    urls = ["https://vama.software", "https://vama.services", "https://vintechhk.com"]
    delays = [2, 4, 6]

    tasks: list[Task[str]] = []

    # TODO: Copy the implementation from q_2.py
    ...

    for result in results:
        if isinstance(result, ValueError):
            print(f"Error fetching url: {result}")
        else:
            print(result)

    return results
