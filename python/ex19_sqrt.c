#include "ex19_sqrt.h"
#include <math.h>

void c_sqrt(T* arg, int n) {
  for (int i = 0; i < n; i++) {
    arg[i].output = sqrt(arg[i].input);
  }
}
