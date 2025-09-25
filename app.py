# Python Async Programming Test
# This programme is designed to run in Python 3.12

import asyncio
import time

# Task 0: Setup
# Ensure you have Python 3.12 installed
# Create a new Python virtual environment (Pip is preferred)
# Install the assigned packages in requirements.txt


# Task 1: A simple async function
# Fix function 'fetch_data()' that takes a url (string) and delay (int) as parameters.
# The function should:
# - Print "Fetching data from {url}", with the actual url replaced
# - Correctly execute asyncio.sleep(delay)
# - Return the execution result as string
def fetch_data(url: str, delay: int) -> str:
    # TODO: Fix and finish the `fetch_data()` function below.
    print("Fetching data from {url}")
    await asyncio.sleep(delay)
    return "Data from {url} after {delay} seconds"


# Task 2: Run multiple async tasks concurrently
# Write an async function called 'main()' that:
# - Creates a list of `task` objects using asyncio.create_task for `fetch_data()` with different urls and delays
# - Runs all tasks concurrently and collects the results
# - Prints each result
# - Returns the list of results
def main():
    urls = ["https://vama.software", "https://vama.services", "https://vintechhk.com"]
    delays = [2, 4, 6]

    # TODO: Implement main function below
    tasks = ...


# Task 3: Handle exceptions in async code
# Modify the `fetch_data()` function to raise an exception if delay > 5
# In `main()`, use asyncio.gather to run tasks and handle exceptions
# If a task raises an exception, handle it and print "Error fetching from {url}: {error}"

# TODO: Modify `fetch_data()` and `main()` to handle exceptions


# Task 4: Use async context manager
# Create an async context manager called 'AsyncTimer' that:
# - Starts a timer when entering
# - Prints the elapsed time when exiting
# - Use it in `main()` to time the entire operation
# - Without importing any external libraries (e.g., no 'contextlib' or 'timeit')
class AsyncTimer:
    # TODO: Implement AsyncTimer class
    ...


# Task 5: Async Generator
# Implement an async generator called 'async_data_stream' that:
# - Takes a list of string (e.g., ["item1", "item2", "item3"])
# - Yields each item with a 0.5 second delay between yields
# - In `main()`, use asynchronous for-loop to iterate over this function and print each item
def async_data_stream(items: list[str]):
    # TODO: Implement async_data_stream generator
    pass


if __name__ == "__main__":
    # TODO: Call main() to run the program
    pass
