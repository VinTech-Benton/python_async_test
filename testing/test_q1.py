import asyncio
import unittest

from src.questions.q_1 import fetch_data


class TestQ1(unittest.TestCase):
    def test_fetch_data(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        url = "http://example.com"
        delay = 1

        try:
            result = loop.run_until_complete(fetch_data(url, delay))
        except Exception:
            self.fail("fetch_data failed.")
        finally:
            loop.close()

        self.assertEqual(result, f"Data from {url} after {delay} seconds")


if __name__ == "__main__":
    unittest.main()
