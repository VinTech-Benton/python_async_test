import asyncio

# Task 1: A simple async function
# 
# Goal: fix a function 'fetch_data()' so that it works as an async function.
# 
# The function should:
# - Print "Fetching data from {url}", ***with the actual url replaced***
# - Correctly execute asyncio.sleep(delay)
# - Return the execution result as string
# 
# Success criteria:
# - Run `python -m unittest testing.test_q1` to validate your implementation.


# TODO: Fix the `fetch_data` function so that it will work as an async function.
def fetch_data(url: str, delay: int) -> str:
    print(f"Fetching data from {url}")
    asyncio.sleep(delay)
    return f"Data from {url} after {delay} seconds"
