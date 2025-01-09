from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef(
    """
typedef struct {
  double input;
  double output;
} T;

void c_sqrt(T*, int);
"""
)

ffibuilder.set_source(
    "_get_sqrt_cffi", '#include "ex19_sqrt.h"', sources=["ex19_sqrt.c"]
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
