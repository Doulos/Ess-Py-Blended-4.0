from stopwatch import timeit
import time  # module needed for sleep()


@timeit
def do_stuff(a, b, c):
    print("enter do_stuff...")
    time.sleep(3)  # sleep for about 3s
    print("leave do_stuff...")
    return a + b + c


print(40 * "-")
x = do_stuff(5, 16, 21)
print("do_stuff() returned: ", x)
