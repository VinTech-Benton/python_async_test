from asyncio import Task
import asyncio

from src.questions.q_1 import fetch_data

# Task 2: Run multiple async tasks concurrently
# Write an async function called 'async_main()' that:
# - Creates a list of `task` objects using `asyncio.create_task()` for fetching data from three different URLs with different delays
# - Runs all tasks concurrently and collects the results using `asyncio.gather()`
# - Prints each result
# - Returns the list of results


async def async_main():
    urls = ["https://vama.software", "https://vama.services", "https://vintechhk.com"]
    delays = [2, 4, 6]

    tasks: list[Task[str]] = []

    # TODO: Add tasks to the list
    for url, delay in zip(urls, delays):
        task = ...
        tasks.append(task)

    # TODO: Gather results from all tasks
    results = ...

    for result in results:
        print(result)

    return results
