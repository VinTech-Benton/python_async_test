from asyncio import Task
import asyncio

# Task 3: Handle exceptions in async code
# Modify the `fetch_data()` function to raise an exception if delay > 5
# In `async_main()`, use asyncio.gather to run tasks and handle exceptions
# If a task raises an exception, handle it and print "Error fetching url: {error}"

# TODO: Modify `fetch_data()` and `main()` to handle exceptions

async def fetch_data(url: str, delay: int) -> str:
    # TODO: Modify this function to raise ValueError if delay > 5
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
