import time
import logging

logging.basicConfig(
    filename="test.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def retry(func, retries=3, delay=1):
    def wrapper(*args, **kwargs):
        for i in range(retries):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                logging.error(f"Retry {i}: {e}")
                time.sleep(delay)
        raise Exception("Max retries reached")
    return wrapper