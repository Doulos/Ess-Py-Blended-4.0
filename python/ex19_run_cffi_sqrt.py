import time
import math
from _get_sqrt_cffi import ffi, lib

n = 10000000
data = ffi.new("T[]", n)
for i in range(n):
    data[i].input = i + 1

print("calling lib.c_sqrt()...")
t = time.perf_counter()
lib.c_sqrt(data, n)
print(f"took: {time.perf_counter() - t:5.3f}sec")

c_result = [data[i].output for i in range(n)]


def p_sqrt(arg, n):
    for i in range(n):
        arg[i] = math.sqrt(i + 1)


print("calling python version...")
p_result = [None for i in range(n)]
t = time.perf_counter()
p_sqrt(p_result, n)
print(f"took: {time.perf_counter() - t:5.3f}sec")

assert c_result == p_result
print(f"C and Python results are identical... :)")
