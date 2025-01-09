import time


# that's the decorator
def timeit(func):
    def wrapper(*args, **kwargs):
        # what time is it before executing the function decorated
        start_time = time.perf_counter()

        # call the original function (the one decorated)
        result = func(*args, **kwargs)

        # what time is it now?
        stop_time = time.perf_counter()

        # print function name and time it took (stop-start)
        print(f"{func.__name__}() took {stop_time-start_time}s")

        # don't forget to return the result of the original function :)
        return result

    # it returns a function that can take any number of arguments
    return wrapper


if __name__ == "__main__":

    @timeit
    def pause(n):
        print(f"going to sleep for {n} seconds...")
        time.sleep(n)
        print("Awake now!")

    @timeit
    def mySuperFunc(a, b, c):
        print("enter mySuperFunc...")
        time.sleep(1)
        print("leave mySuperFunc...")
        return a + b + c

    print(40 * "-")
    print("pause test")
    pause(3)

    print(40 * "-")
    print("mySuperFunc test")
    x = mySuperFunc(6, 15, 21) / 2
    print("Half-truth = ", x)
