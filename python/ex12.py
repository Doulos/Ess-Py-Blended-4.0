import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        stop_time = time.perf_counter()
        print(f"{func.__name__}() took {stop_time-start_time}s\n")
        return result

    return wrapper


@timeit
def do_stuff(a, b, c):
    """do_stuff is like pause() but takes param and return value"""
    print("enter do_stuff...")
    time.sleep(3)  # sleep for about 3s
    print("leave do_stuff...")
    return a + b + c


print(40 * "-")
x = do_stuff(5, 16, 21)
print("do_stuff() returned: ", x)
