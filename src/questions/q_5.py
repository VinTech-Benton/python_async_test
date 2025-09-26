import asyncio


# Task 5: Async Generator
# Implement an async generator called 'async_data_stream' that:
# - Takes a list of string (e.g., ["item1", "item2", "item3"])
# - Yields each item with a 0.5 second delay between yields
# - In `stream_main()`, use asynchronous for-loop to iterate over this function,
#   - store each item in a list and return the result list


async def async_data_stream(items: list[str]):
    for item in items:
        # HINT: do not modify the line below.
        _item = f"a_{item}"

        # TODO: Implement async_data_stream generator
        ...

        await asyncio.sleep(0.5)


async def stream_main():
    items: list[str] = ["item1", "item2", "item3"]
    results: list[str] = []

    # TODO: Use async for-loop to iterate over async_data_stream
    for item in async_data_stream(items):
        results.append(item)

    return results
