import time
import functools


def retry(times=3, delay=1, exceptions=(Exception,)):
    """
    Retry decorator for flaky operations
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    print(f"[RETRY] Attempt {attempt + 1}/{times} failed: {e}")
                    time.sleep(delay)

            raise last_exception
        return wrapper
    return decorator


def wait_until(condition_func, timeout=5, interval=0.2):
    """
    Wait until condition is True
    """
    start = time.time()
    while time.time() - start < timeout:
        if condition_func():
            return True
        time.sleep(interval)
    return False