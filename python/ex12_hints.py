import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        stop_time = time.perf_counter()
        print(f"{func.__name__}() took {stop_time-start_time}s\n")
        return result

    return wrapper


def pause_list(list_n: list[int]) -> str:
    """pause n seconds"""
    for i in range (len(list_n)):
        print(f"going to sleep for {list_n[i]} seconds…")
        time.sleep(list_n[i])
    return "All done"

pause_list([1,2,3])
pause_list([1.0, 2.0, 3])


