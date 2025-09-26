import asyncio

# Task 1: A simple async function
# Fix a function 'fetch_data()' that takes a url (string) and delay (int) as parameters.
# The function should:
# - Print "Fetching data from {url}", with the actual url replaced
# - Correctly execute asyncio.sleep(delay)
# - Return the execution result as string


# TODO: Fix the `fetch_data` function so that it will work as an async function.
def fetch_data(url: str, delay: int) -> str:
    print("Fetching data from {url}")
    asyncio.sleep(delay)
    return "Data from {url} after {delay} seconds"
