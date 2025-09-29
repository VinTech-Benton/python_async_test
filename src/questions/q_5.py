import asyncio


# Task 5: Async generator stream
#
# - Goal: implement an asynchronous generator that yields transformed items
#   with a short delay between each yield, and consume it using an
#   asynchronous for-loop.
#
# - Inputs: the generator `async_data_stream` accepts a list of strings
#   (for example, ["item1", "item2", "item3"]). Inside the generator each
#   input `item` is transformed to a new string `_item = f"a_{item}"` which
#   should be yielded to the caller. The consumer function `stream_main()` has
#   a local `items` list to pass into the generator.
#
# - Output: `async_data_stream` yields each transformed item (type: str).
#   `stream_main()` should iterate over the generator using `async for`, collect
#   each yielded value into a `results: list[str]`, and return that list.
#
# Implementation hints:
# - Ensure you yield `_item` (the transformed value) — the test expects the
#   yielded strings to be prefixed with "a_".
#
# Success criteria:
# - Running `python -m unittest testing.test_q5` must pass.


async def async_data_stream(items: list[str]):
    for item in items:
        # NOTICE: you must yield the `_item`, not the `item` variable.
        _item = f"a_{item}"

        # TODO: Implement async_data_stream generator
        ...

        await asyncio.sleep(0.5)


async def stream_main():
    items: list[str] = ["item1", "item2", "item3"]
    results: list[str] = []

    # TODO: Use async for-loop to iterate over async_data_stream
    ...
    # TODO: Append each yielded item to results list
    ...

    return results
